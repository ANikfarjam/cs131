#!/bin/zsh

# Input file
input_file=$1

# Output file
output_file="yearly_dataset.csv"

# Create a temporary file to store intermediate results
temp_file=$(mktemp)

# Add a header to the temporary file
echo "year,region,Influenza_Category,Count" > "$temp_file"

# get yearly count of death
awk -F',' 'NR>1 {split($3, date, "/"); year=date[3]; print year","$4","$5","$6}' "$input_file" | \
awk -F',' '{arr[$1","$2","$3]+=$4} END {for (i in arr) print i","arr[i]}' | \
#goup everything by year
sort -n -k1 >> "$temp_file"
# Move the temporary file to the final output file
mv "$temp_file" "$output_file"

echo "Processing complete. Results saved to $output_file"

