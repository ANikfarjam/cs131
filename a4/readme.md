In the given data set movies there is column that is complitly empty "gross"
This bash script will scan through the given data set and identify the empty column and will delete them
im going to use the movies data set as an example to drop the gross column
to achive this im using these step:
------------------------------------------------------------------------------------------------------------
1- I created a function that chack wether an column is empty:
is_empty_column() {
    column="$1"
     awk -v col="$column" '{if ($col != "") {exit 1}} END {exit 0}' "$input_file"
}
2- loop through each column and when assign the column that is empty to that variable
for ((i = 1; i <= num_columns; i++)); do
    if is_empty_column "$i"; then
        columns_to_delete+=" $i"
    fi
done

3- use sed to delete that column
else
    # Use sed to delete the empty columns
    sed -i -e "s/,$columns_to_delete,/,/g" "$input_file"
    echo "Empty columns removed from the dataset."
fi
------------------------------------------------------------------------------------------------------------
result:
[ashkan23fa@sjsu a4]$ ./delete_emplty_columns.sh ../ws8/movies.csv
Empty columns removed from the dataset.
