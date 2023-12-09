#!/bin/bash
terraform apply \
    -auto-approve \
    -no-color \
    2>> repeater-err.log \
    1>> repeater.log
exit