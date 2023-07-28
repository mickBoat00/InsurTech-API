module "bucket" {
  source     = "../../modules/cloud_storage"
  project_id = var.project_id
  name       = "${var.project_id}-dj-bucket"
  depends_on = [module.project_main]
}
