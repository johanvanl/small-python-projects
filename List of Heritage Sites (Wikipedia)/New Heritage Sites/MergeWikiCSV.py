import WikiTablesToDictRows
import CsvToDictRows

wiki =  WikiTablesToDictRows.wikiTableToDict('input.txt')
csv = CsvToDictRows.csvToDictRows('csv_files/general.csv')

wiki_list = []
for w in wiki:
    wiki_list.append(w['SiteReference'])

csv_list = []
for c in csv:
    csv_list.append(c['SiteReference'])

# For Length
'''
print len(wiki_list)
print len(csv_list)
exit(0)
'''


# Test for Duplicates
'''
print 'Any Duplicates in the Wiki list:'
wiki_set = set(wiki_list)
print len(wiki_list)
print len(wiki_set)

print '\nAny Duplicates in the CSV list:'
csv_set = set(csv_list)
print len(csv_list)
print len(csv_set)

print '\nIntersection (supposed to be zero)'
print len(wiki_set & csv_set)
print wiki_set & csv_set
exit(0)
'''


# Merge the two lists of Dictionary Rows
merge = wiki + csv

# Sort the list alphabetically
merge.sort(key = lambda x: x['SiteReference'])

# Output the new Wikipedia Table
cols = ['guid', 'SiteReference', 'Site_name', 'Magisterial_district', 'Municipal_name', 'Town', 'Erf number', 'Farm number', 'Portion', 'Latitude', 'Longitude', 'NHRA status', 'NMC status', 'Description', 'image', 'commonscat']

f = open('output.txt','w')
for dictRow in merge:
  f.write('{{SAHRA heritage site row' + '\n')
  for col in cols:
    row = '| ' + col + ' ='
    if col in dictRow:
       row += ' ' + dictRow[col]
    # All the columns are always present except for
    # commonscat, so if commonscat is empty don't add
    # and empty line for it
    elif col == 'commonscat':
      continue
    f.write(row + '\n')
  f.write('}}' + '\n')  
f.close()
