variable "AWS_Access_Key" {
    type = string
    sensitive = true
}

variable "AWS_Secret_Key" {
    type = string
    sensitive = true
}

variable "region" {
    default = "us-west-2"
}