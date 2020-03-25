#!/bin/sh

curl -X GET "https://api.inovujemesdaty.cz/locations" -H "accept: text/csv"  > locations.csv # sloupec s geometrii smazan rucne

./download.py # pro jinou datovou sadu staci upravit par promennych hned nahore

rm -f ./tmp/*.csv

