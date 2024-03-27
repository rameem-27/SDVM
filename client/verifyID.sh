#!/bin/bash

while true; do
    python3 qr_read.py
    python3 tojson.py
    if [ $? -eq 0 ]; then
        break  # Exit the loop upon successful processing
    else
        echo "Not XML"
    fi
done

# Continue execution
python3 client.py
python3 clr_json.py

