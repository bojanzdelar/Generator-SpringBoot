#!/bin/bash

rm -rf output
mkdir -p output
cd output
mkdir controller dto mapper model service repository
cd ..
python3 script.py