#!/bin/bash

input_file="$1"

# Define a function to check if a column is empty
is_empty_column() {
    column="$1"
    awk -v col="$column" '{if ($col != "") {exit 1}} END {exit 0}' "$input_file"
}

# Get the number of columns in the input file
num_columns=$(awk -F ',' '{print NF; exit}' "$input_file")

# Create a list of columns to delete
columns_to_delete=""
for ((i = 1; i <= num_columns; i++)); do
    if is_empty_column "$i"; then
        columns_to_delete+=" $i"
    fi
done

if [ -z "$columns_to_delete" ]; then
    echo "No empty columns found in the dataset."
else
    # Use sed to delete the empty columns
    sed -i -e "s/,$columns_to_delete,/,/g" "$input_file"
    echo "Empty columns removed from the dataset."
fi
