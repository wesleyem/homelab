#!/bin/bash
# run with cron to grab available instance
log_dir="/root/projects/homelab/oci/arm-compute-1/logs"
error_log_filename="repeater-errlog"
log_filename="repeaterlog"
timestamp="Timestamp: $(date)"
echo $timestamp >> $log_dir/$error_log_filename
echo $timestamp >> $log_dir/$log_filename
terraform apply \
    -auto-approve \
    -no-color \
    2>> $log_dir/$error_log_filename \
    1>> $log_dir/$log_filename
exit