#!/bin/sh
error_log_filename="repeater-errlog"
log_filename="repeaterlog"
base_dir="$HOME/projects/homelab/terraform/oci"
directories=("arm-compute-1" "arm-compute-2" "arm-compute-3")

for dir in "${directories[@]}"; do
    working_dir="$base_dir/$dir/logs"
    timestamp=$(date +%s)
    cd "$working_dir" && mv "$error_log_filename" "$error_log_filename-$timestamp" && mv "$log_filename" "$log_filename-$timestamp"
done
