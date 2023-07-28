module "cloud_run" {
  source              = "../../modules/cloud_run"
  cloud_run_name      = "working2"
  region              = "europe-west2"
  image               = var.image_tag
  project_id          = var.project_id
  sql_connection_name = module.cloud_sql_postgres.sql_conn_name
  #   secret_key_ref_key = "latest"
  # secret_key_ref_name = data.google_secret_manager_secret_version.db_host.name
  #   secret_key_ref_name = module.cloud_sql_postgres.scrt_vrs_module_value
  depends_on = [module.project_main]
}
