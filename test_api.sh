#!/bin/bash
response=$(curl -s http://127.0.0.1:5000/weather?city=London)

if [[ $response == *"temperature"* ]]; then
  echo "Test Passed: API is working"
  exit 0
else
  echo "Test Failed: API is not responding"
  exit 1
fi
