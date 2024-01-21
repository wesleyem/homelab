#!/bin/bash
base_dir="$HOME/projects/homelab/terraform/oci"
directories=("arm-compute-1" "arm-compute-2" "arm-compute-3")
error_log_filename="repeater-errlog"
log_filename="repeaterlog"

for dir in "${directories[@]}"; do
    log_dir="$base_dir/$dir/logs"
    timestamp="Timestamp: $(date)"
    echo "$timestamp" >> "$log_dir/$error_log_filename"
    echo "$timestamp" >> "$log_dir/$log_filename"
    (cd "$log_dir/.." && terraform apply -auto-approve -no-color 2>> "$log_dir/$error_log_filename" 1>> "$log_dir/$log_filename")
done
exit
