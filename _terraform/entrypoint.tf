module "main" {
  source     = "./projects/main"
  project_id = var.project_id
  enabled_apis = [
    "run.googleapis.com",
    "iam.googleapis.com",
  ]
  image_tag = var.image_tag
}
