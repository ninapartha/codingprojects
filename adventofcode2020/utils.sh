awk '{print before $0 after}' before="\"" after="\"," input.txt > output.txt

# puzzle4
perl -000 -pe 's/(?<!\n)\n (?!\n|$)//g' input.txt | awk ' /^$/ { print; } /./ { printf("%s ", $0); } ' > output.txt