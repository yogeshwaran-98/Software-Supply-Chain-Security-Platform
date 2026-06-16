resource "aws_s3_bucket" "demo_bucket" {
  bucket = "public-bucket"
}

resource "aws_s3_bucket_public_access_block" "demo bucket access" {
  bucket = aws_s3_bucket.demo_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}