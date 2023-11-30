grep -v "Influenza_Tested" ./flu-publichealthlab-byregion-fluseason.csv | 
grep -v "Influenza_Total" |
cut -d',' -f2,5,6 | 
awk -F',' '{ week = substr($1, 5); print week","$2","$3 }' | 
sort | 
awk -F',' '{ count[$1","$2]+=$3 } END { for (c in count) print c","count[c] }' | 
sort -t',' -k3nr > type_week_ranking.csv