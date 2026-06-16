resource "aws_db_instance" "rds_demo" {

  identifier         = "demo-db"

  engine             = "mysql"

  instance_class     = "db.t3.micro"

  allocated_storage  = 20

  storage_encrypted  = false

  username           = "admin"

  password           = "Password123!"

}