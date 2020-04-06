/* this is a multi
comment */

provider "aws" {
  region = "${var.region}"
}

/*
  NAT Instance
*/


resource "aws_instance" "ship" {

  ami           = "${var.ami}"

  instance_type = "${var.master_instance_type}"
  key_name                    = "${var.key_name}"
  subnet_id                   = "${var.subnet_id}"
  tags = {
    Name = "${var.ship_name[count.index]}"
    Owner = "butzer@contractor.usgs.gov"
    Project = "LPIP"
  }
  iam_instance_profile                    ="${var.iam_role}"
  # security_groups = ["${var.security_group_ssh}", "${var.security_group_ping}", "${aws_security_group.xrdp.id}"]
  security_groups = ["${var.security_group_ssh}", "${var.security_group_ping}", "${var.security_group_web}"]
  root_block_device {volume_size = 40}
  user_data                   = "${file("files/os_boot.sh")}"

  count = 2
}
