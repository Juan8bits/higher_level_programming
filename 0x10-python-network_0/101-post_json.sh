#!/bin/bash
# Do a POST request with the content of a file (JSON object).
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
