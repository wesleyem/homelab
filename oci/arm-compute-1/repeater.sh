#!/bin/bash
terraform apply -auto-approve 2>> repeater-err.log 1>> repeater.log
exit