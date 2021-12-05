provider "aws" {
    region = "${var.region}"
    access_key = var.AWS_Access_Key
    secret_key = var.AWS_Secret_Key
}

resource "aws_instance" "ec2_deployment_test" {
  ami = "ami-00f7e5c52c0f43726"
  instance_type = "t2.micro"
}