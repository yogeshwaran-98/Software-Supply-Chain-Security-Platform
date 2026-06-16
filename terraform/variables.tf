variable "aws_region" {
  description = "AWS Region"

  type = string

  default = "ap-south-1"
}

variable "artifact_bucket_name" {
  description = "Bucket for storing artifacts"

  type = string
}