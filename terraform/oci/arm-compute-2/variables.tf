# OCI
# ---
# Variables needed for OCI

# OCI Config
variable "tenancy_ocid" {
    type = string
    description = "OCID of your tenancy."
}
variable "user_ocid" {
    type = string
    description = "OCID of the user calling the API."
}
variable "private_key_path" {
    type = string
    description = "The path (including filename) of the private key stored on your computer. This key pair is NOT the SSH key that you use to access compute instances."
}
variable "fingerprint" {
    type = string
    description = "Fingerprint for the key pair being used."
}
variable "region" {
    type = string
    description = "An OCI region."
}
variable "ssh_authorized_keys" {
    type = string
    description = "SSH public key used to access compute instance"
}
variable "ids" {
  type = object({
    source_id = string
    compartment_id = string
    subnet_id = string
  })
  description = "Object of all the string ids"
}

variable "availability_domain" {
  type = string
  description = "Availability Domain"
}