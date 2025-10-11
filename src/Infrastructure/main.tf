terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.43.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

# GCS bucket
resource "google_storage_bucket" "bucket-portafolio" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 7
    }
    action {
      type = "Delete"
    }
  }
}

# BigQuery dataset
resource "google_bigquery_dataset" "dataset_portafolio" {
  dataset_id = var.bq_dataset_name
  location   = var.location

}

# BigQuery table, put the path to reach the table in dataset_id
resource "google_bigquery_table" "table_demo" {
  dataset_id          = google_bigquery_dataset.dataset_portafolio.dataset_id
  table_id            = var.bq_table_name
  deletion_protection = false
  schema              = file("schema.json")
}
