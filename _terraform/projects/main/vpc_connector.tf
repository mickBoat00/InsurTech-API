module "vpc_connect" {
  source        = "../../modules/vpc_connector"
  project_id    = var.project_id
  region        = "europe-west2"
  name          = "run-connect"
  ip_cidr_range = "10.8.0.0/28"
  network       = "default"
  machine_type  = "e2-micro"
  min_instances = 2
  max_instances = 3

  depends_on = [module.project_main]
}
