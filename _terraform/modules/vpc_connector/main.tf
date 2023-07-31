resource "google_vpc_access_connector" "connector" {
  project       = var.project_id
  region        = var.region
  name          = var.name
  ip_cidr_range = var.ip_cidr_range
  network       = var.network
  machine_type  = var.machine_type
  min_instances = var.min_instances
  max_instances = var.max_instances
}
