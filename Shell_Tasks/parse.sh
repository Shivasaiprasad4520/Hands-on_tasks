#!/bin/bash

# Path of nginx access log
LOG_FILE="/var/log/nginx/access.log"

# Check file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found!"
    exit 1
fi

echo "Top 10 IP Addresses accessing Nginx:"
echo "-----------------------------------"

awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -10
