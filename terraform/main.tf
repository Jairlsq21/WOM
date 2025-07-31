terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project     = "wom-prueba"
  region      = "us-central1"
}

resource "google_cloudfunctions_function" "function" {
  name        = "cloud-function-test"
  runtime     = "python310"
  available_memory_mb   = 256
  source_archive_bucket = "files_repos"
  source_archive_object = "helloworld.zip"
  trigger_http = true
  entry_point = "hello_world"
  # Para funciones basadas en eventos, como Pub/Sub:
  # trigger_http = false
  # event_trigger {
  #   event_type = "google.cloud.pubsub.topic.v1.messagePublished"
  #   resource   = "your-pubsub-topic"
  #   service    = "pubsub.googleapis.com"
  # }
}

resource "google_storage_bucket" "source_bucket" {
  name = "files_repos2"
  location = "US"
  uniform_bucket_level_access = true
}