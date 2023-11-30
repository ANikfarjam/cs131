#!/bin/zsh

# Input file
input_file=$1

#check if the directory that data should be on already exist or not
directory=./year_data
if [ -d "$directory" ]; then
    echo "The directory exists."
else
    mkdir "$directory"
    echo "The directory created."
fi
#now since since we now that data is from 2009 to 2020
years_str=("09" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20") 
for year in "${years_str[@]}"; do
    temp_file=$(mktemp)
    echo "region,Influenza_Category,Count" > "$temp_file"
    sed -n "/^$year,/p" "$input_file" | sed -n "s/^$year,//p" >> "$temp_file"
    mv "$temp_file" ./year_data/"$year.csv"
    echo "data for the year $year is created"
done

