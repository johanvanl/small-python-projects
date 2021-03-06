import csv

def getCsvRows(fn):
  rows = []
  with open(fn, 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      rows.append(row)
  return rows

# If the column is empty do not add to Dictionary
def rowToDict(header, row, ignoreEmptyColumn=False):
  dict = {}
  for index in range(len(header)):
    if ignoreEmptyColumn and row[index].strip() == '':
      continue
    dict[header[index]] = row[index].strip()
  return dict

def csvToDictRows(fn):
  rows = getCsvRows(fn)
  header = rows[0]
  rows = rows[1:]
  dictRows = []
  index = 1
  for row in rows:
    dictRows.append(rowToDict(header, row, True))
  return dictRows
  
if __name__ == "__main__":
  print csvToDictRows('csv_files/table_mountain.csv')
