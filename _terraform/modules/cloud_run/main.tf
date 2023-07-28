resource "google_cloud_run_service" "default" {
  name     = var.cloud_run_name
  location = var.region
  project  = var.project_id

  template {
    spec {
      containers {
        image = var.image
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "2"
        # "run.googleapis.com/cloudsql-instances" = google_sql_database_instance.instance.connection_name
        # "run.googleapis.com/cloudsql-instances" = var.sql_connection_name
        "run.googleapis.com/client-name" = "terraform"
      }
    }
  }
  autogenerate_revision_name = true
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.default.location
  project  = google_cloud_run_service.default.project
  service  = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}
