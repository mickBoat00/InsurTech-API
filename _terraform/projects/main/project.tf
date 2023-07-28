module "project_main" {
  source     = "../../modules/project"
  project_id = var.project_id
  enabled_apis = [
    "servicenetworking.googleapis.com",
    "iam.googleapis.com",
    "run.googleapis.com"
  ]
}



