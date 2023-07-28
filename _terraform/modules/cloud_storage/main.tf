resource "google_storage_bucket" "static" {
  project                     = var.project_id
  name                        = var.name
  location                    = "US"
  force_destroy               = false
  uniform_bucket_level_access = true
  storage_class               = "STANDARD"

  public_access_prevention = "inherited"
}

