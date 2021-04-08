#!/bin/bash
# Script that show the number of bytes returned by an URL.
curl -sI "$1" | grep -i "Content-Length:" | cut -d " " -f2
