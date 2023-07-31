module "cloud_sql_postgres" {
  source       = "../../modules/cloud_sql"
  project_id   = var.project_id
  db_name      = "db"
  region       = "europe-west2"
  ipv4_enabled = true

  depends_on = [module.project_main]
}
