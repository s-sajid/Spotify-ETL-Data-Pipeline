variable "Spotify_Client_ID" {
    type = "string"
    sensitive = true
}

variable "Spotify_Client_Secret" {
    type = "string"
    sensitive = true
}

variable "AWS_Access_Key" {
    type = "string"
    sensitive = true
}

variable "AWS_Secret_Key" {
    type = "string"
    sensitive = true
}

variable "region" {
    type = string
    default = "us-west-2"
}