#!/bin/bash
# Script that do a request and display the status code of the response.
curl -sI "$1" | grep "HTTP/1.0" | cut -d " " -f2
