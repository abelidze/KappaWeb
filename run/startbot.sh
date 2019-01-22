#!/bin/bash
echo "Starting KappaWeb Services..."
sleep 1

screen -S KappaWeb -c startbot.conf

sleep 2
echo "KappaWeb Started! <-> Type 'screen -r' to attach session"
