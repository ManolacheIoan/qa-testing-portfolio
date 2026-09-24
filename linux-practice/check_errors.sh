#!/bin/bash
echo "Checking server.log for errors..."
ERROR_COUNT=$(grep -c "ERROR" server.log)
echo "Found $ERROR_COUNT errors."
