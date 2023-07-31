module "run_secret" {
  source     = "../../modules/secrets"
  project_id = var.project_id
  secrets = {
    "SECRET_KEY" : "pnocj8u+!1yo8t",
    "DEBUG" : "1",
    "ALLOWED_HOSTS" : "*",
    "GCP_BUCKET_NAME" : module.bucket.bucket_name,
  }
  depends_on = [module.project_main]
}

