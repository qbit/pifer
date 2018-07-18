#!/bin/sh

# Install dependencies and tools
sudo apt-get install python3-pigpio pigpio python3-websockets tmux

# Enable the GPIO daemon
sudo systemctl enable pigpiod && systemctl start pigpiod
