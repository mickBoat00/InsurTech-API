data "google_compute_network" "private_network" {
  name    = "default"
  project = var.project_id
}


resource "google_compute_global_address" "private_ip_address" {
  provider = google-beta

  name          = "private-ip-address"
  project       = var.project_id
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = data.google_compute_network.private_network.id
}

resource "google_service_networking_connection" "private_vpc_connection" {
  provider = google-beta

  network                 = data.google_compute_network.private_network.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
}


resource "random_id" "db_name_suffix" {
  byte_length = 4
}

resource "google_sql_database_instance" "instance" {
  provider = google-beta

  name             = "${var.db_name}-${random_id.db_name_suffix.hex}"
  project          = var.project_id
  region           = var.region
  database_version = "POSTGRES_15"

  depends_on = [google_service_networking_connection.private_vpc_connection]

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled                                  = var.ipv4_enabled
      private_network                               = data.google_compute_network.private_network.id
      enable_private_path_for_google_cloud_services = true
    }
  }

  deletion_protection = "false"
}

resource "random_password" "password" {
  length = 12
}

resource "google_sql_database" "database" {
  project  = var.project_id
  name     = "postgres_db"
  instance = google_sql_database_instance.instance.name
}

resource "google_sql_user" "user" {
  name     = "postgres_user"
  project  = var.project_id
  instance = google_sql_database_instance.instance.name
  password = random_password.password.result
}


module "secrets" {
  source     = "../secrets"
  project_id = var.project_id
  secrets = {
    "DATABASE_HOST" : google_sql_database_instance.instance.connection_name
    "DATABASE_NAME" : google_sql_database.database.name
    "DATABASE_PASSWORD" : google_sql_user.user.password
    "DATABASE_PORT" : "5432"
    "DATABASE_USER" : google_sql_user.user.name
  }
}
