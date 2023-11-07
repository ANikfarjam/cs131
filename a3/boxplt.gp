# Set the terminal to SVG and specify the output file
set terminal svg enhanced size 800,600 font "Helvetica,12"
set output "a3t3.svg"

# Set the title and labels for the axes
set title "Correlation between Number of Passengers and Average Tip Amount (August 2019)"
set xlabel "Number of Passengers"
set ylabel "Average Tip Amount"

# Define the data file and separator
datafile = "gnu1.csv"
separator = ","

# Set the style of the bars
set style data boxes
set style fill solid



# Set the border (line) color and width for the boxes (e.g., black and 1)
set style line 1 lc rgb "black" lw 1
set boxwidth 0.5  # Adjust the box width as needed

# PLot
plot datafile using 1:2 with boxes title "Tip Amount"
