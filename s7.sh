clear
echo -n "Enter a file name:"
read fname
echo "There are" cat $fname |wc -l "lines in a file "$fname
