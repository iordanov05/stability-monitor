#!/bin/bash
for i in $(seq 1 30); do
  docker run -d --rm -p $((8080 + $i)):8080 --name mock_server_$i stability-monitor-mock
done
