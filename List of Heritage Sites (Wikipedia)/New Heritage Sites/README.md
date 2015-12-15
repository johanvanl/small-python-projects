# New Heritage Sites

I was provided with an Excel Spreadsheet from which I exported each sheet as a seperate CSV file, found in the folder 'csv_files':
* beaufort-west.csv
* bellville.csv
* caledon.csv
* cape-town-cape-town-cbd.csv
* cape-town-near-cape-town.csv
* clanwilliam.csv
* general.csv
* george-and-mossel-bay.csv
* knysna.csv
* paarl.csv
* roberston-and-montagu.csv
* Simonstown.csv
* stellenbosch-somerset-west-and-strand-in-town.csv
* stellenbosch-somerset-west-and-strand-near-town.csv
* swellendam-and-riversdale.csv
* table _mountain.csv
* tulbagh.csv
* worcester.csv
* wynberg.csv

Only works between the first ```{{SAHRA heritage site row``` and the last ```}}```.

## CSV File to List of Dictionaries
Found in the file ```CsvToDictRows.py```.

## Wikipedia Table to List of Dictionaries
Found in the file ```WikiTablesToDictRows.py```.

## Merge the CSV File with the Wikipedia Table
Found in the file ```MergeWikiCSV.py```.

## Before Merging the CSV File with the Wikipedia Table
Test for duplicate Site References, first in the current Wikipedia Table and then between the current Wikipedia Table and the new Heritage Sites in the CSV.

Run wiki alone the first time to just make sure the spacing is correct, so that the big edit doesn't contain all the formatting edits as well.

Sort the original table first to make sure it's already alphabetical to start with, so that the big edit doesn't contain the sorting of the original table as well.

