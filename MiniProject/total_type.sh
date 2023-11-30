#!/bin/bash
input_file=$1
#echo "year,region,Influenza_Category,Count" > type_data.csv
# Use awk to group by Influenza_Category and sum the Count
awk -F',' 'BEGIN {OFS=","} NR>1 {arr[$3]+=$4} END {for (i in arr) print i, arr[i]}' "$input_file" | sort > "type_data.csv"


