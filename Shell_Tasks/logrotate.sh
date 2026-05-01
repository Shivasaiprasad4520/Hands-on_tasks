#!/bin/bash

###########################
# Metadata
#author : Shivasaiprasad
## this shell script to automate the process of rotating log files and compressing old files to save disk space

###########################

# Log directory and file pattern
log_directory="/var/log/myapp"
file_pattern="*.log"

# Function to rotate log files
rotate_log_files() {
    find "$log_directory" -name "$file_pattern" -exec mv {} {}.1 \;
    echo "Log files rotated."
}

# Function to compress old log files
compress_old_log_files() {
    find "$log_directory" -name "$file_pattern.1" -mtime +"$compress_after_days" -exec gzip {} \;
    echo "Old log files compressed."
}

# Main script

# Call the rotate_log_files Function
rotate_log_files

# Call the compress_old_log_files Function
compress_old_log_files