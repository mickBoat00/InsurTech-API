data "google_project" "my_project" {
  project_id = var.project_id
}

resource "google_project_service" "project" {

  project  = data.google_project.my_project.id
  for_each = toset(var.enabled_apis)
  service  = each.value

  disable_dependent_services = true
}

data "google_compute_default_service_account" "default" {
  project = var.project_id

  depends_on = [google_project_service.project]
}
