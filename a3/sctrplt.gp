# Set the output format to SVG
set terminal svg enhanced size 800,600
set output 'a3t4.svg'

# Set the title and labels for the plot
set title "Correlation Between Travel Distance and Amount Paid (August 2019)"
set xlabel "Distance"
set ylabel "Amount Paid"

# Use space as the column separator in the CSV file
set datafile separator ' '

# Plot the data as a scatter plot
plot 'gnu2.csv' using 1:2 with points pointtype 7 pointsize 1.0 title "Amount Paid"

