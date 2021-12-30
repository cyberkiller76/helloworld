echo -n "Enter year of your birth:"
read byear
cyear=date | tr -s " " | cut -d "" -f 6
age= 'expr' $cyear - $byear
echo You are $age years old as of today.
