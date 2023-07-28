resource "google_secret_manager_secret" "secret-basic" {

  for_each  = var.secrets
  secret_id = each.key

  labels = {
    label = "my-label"
  }

  replication {
    automatic = true
  }
}


resource "google_secret_manager_secret_version" "secret-version-basic" {

  for_each = var.secrets
  secret   = google_secret_manager_secret.secret-basic[each.key].id

  secret_data = each.value
}



output "scrt_vrsion_name_db_host" {
  # value = google_secret_manager_secret_version.secret-version-basic["DATABASE_HOST"].name.secret_id
  value = "DATABASE_HOST"
}
