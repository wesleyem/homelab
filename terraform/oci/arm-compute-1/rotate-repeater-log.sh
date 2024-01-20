#!/bin/sh
# use with cron to move log files
error_log_filename="repeater-errlog"
log_filename="repeaterlog"
working_dir="/root/projects/homelab/oci/arm-compute-1/logs"
timestamp=$(date +%s)
cd $working_dir
mv $error_log_filename repeater-errlog-$timestamp
mv $log_filename repeaterlog-$timestamp
exit
