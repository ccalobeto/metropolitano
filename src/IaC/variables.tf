variable "credentials" {
  description = "My key credentials file"
  default     = "~/.google/credentials/calobeto-portafolio-creds.json"
}

variable "project" {
  description = "Project"
  default     = "calobeto-portafolio"
}

variable "region" {
  description = "Default region for provider"
  default     = "southamerica-west1"
}

variable "location" {
  description = "Location for BigQuery and GCS"
  default     = "southamerica-west1"
}

variable "bq_dataset_name" {
  description = "BigQuery dataset name"
  default     = "portafolio"
}

variable "bq_table_name" {
  description = "BigQuery table name"
  default     = "demo_table"
}

variable "gcs_bucket_name" {
  description = "My Storage bucket name"
  default     = "calobeto-portafolio-datasets"
}


