module "project_main" {
  source       = "../../modules/project"
  project_id   = var.project_id
  enabled_apis = var.enabled_apis
}



