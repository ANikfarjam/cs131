#!/bin/bash

# Your input file
input_file=$1

# Extract and sum the counts for each region
awk -F',' 'NR>1 {region_count[$4]+=$6} END {for (region in region_count) print region "," region_count[region]}' $input_file | sort -t',' -k1,1 > total_death.csv
echo "file created. total_death.csv"