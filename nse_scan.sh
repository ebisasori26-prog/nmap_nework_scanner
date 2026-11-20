#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP> <NSE_SCRIPT>"
    exit 1
fi

IP=$1
SCRIPT=$2

echo "Starting Nmap NSE Scan..."
echo "Target IP: $IP"
echo "NSE Script: $SCRIPT"

nmap -sV --script "$SCRIPT" "$IP"

echo "Scan Completed!"