output "security_group_id" {
  value = aws_security_group.app_sg.id
}

output "artifact_bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}