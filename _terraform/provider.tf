terraform {
  # required_version = "~> 1.4.6"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.75.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 4.75.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.5.1"
    }
  }
  backend "gcs" {
    bucket = "skillful-radar-387911-tf-state"
    prefix = "files"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}
