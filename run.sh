#!/bin/sh
cd -- "$(dirname "$BASH_SOURCE")"

echo "what would you like to do?"
echo "1) Generate a list of leads"
echo "2) Generate a list of lead URL's"
echo "3) Both"
select abc in "1" "2" "3"; do
    case $abc in
     #   a ) python leadleech.py; break;;
     #   b ) python leadleech2.py; break;;
	 #	c ) python leadleech.py; python leadleech2.py; exit;;
    esac
done

