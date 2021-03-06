import re

# Read the file into lines
def fileToList(fn):
  file_list = []
  with open(fn, 'r') as f:
    for line in f:
      line = line.strip()
      file_list.append(line)
  return file_list

# If a column contains more than one row merge
# the rows together

# This is done in place
def mergeColumns(cols):
  colIndex = 0
  while colIndex < len(cols):
    if not cols[colIndex].startswith('|'):
      cols[colIndex-1:colIndex+1] = ['\n'.join(cols[colIndex-1:colIndex+1])]
    else:
      colIndex += 1

def fileListToRows(fn):
  file_list = fileToList(fn)
  rows = []
  index = 0
  while index < len(file_list):
    if file_list[index] == '{{SAHRA heritage site row':
      cols = []
      index += 1
      # Add all the columns to the cols list
      while file_list[index] != '}}':
        cols.append(file_list[index])
        index += 1
      mergeColumns(cols)
      rows.append(cols)
    index += 1
  return rows

# If the column is empty do not add to Dictionary
def rowToDict(row, ignoreEmptyColumn=False):
  # The row pattern for example:
  # | Site_name = 24 The Avenue, Stellenbosch
  pattern = '\|\s([\w\s]+?)\s=(.*)'

  dict = {}
  for col in row:
    # Make the '.' special character match any character at all,
    # including a newline
    # Otherwise you get the text until the first newline
    # and these columns can contain multiple lines
    m = re.match(pattern, col, re.DOTALL)
    if m and not (ignoreEmptyColumn and m.group(2).strip() == ''):
      dict[m.group(1)] = m.group(2).strip()
  return dict

def wikiTableToDict(fn):
  rows = fileListToRows(fn)
  dictRows = []
  for row in rows:
    dictRows.append(rowToDict(row, True))
  return dictRows

if __name__ == "__main__":
  print wikiTableToDict('input.txt')

