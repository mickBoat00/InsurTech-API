
locals {
  extracted_project_id = regex("projects/(.+)", data.google_project.my_project.id)[0]
}


output "gcp_project_id" {
  value = local.extracted_project_id
}


output "default_sa_email" {
  value = data.google_compute_default_service_account.default.email
}
