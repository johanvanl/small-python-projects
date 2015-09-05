from bs4 import BeautifulSoup
import urllib2

def getLatLongTuple(ref):
  ref = ref.strip().replace('/', '')

  url= 'http://www.sahra.org.za/sahris/sites/' + ref
  page = urllib2.urlopen(url)

  soup = BeautifulSoup(page.read(), "html.parser")

  '''
  <abbr class="latitude" title="-26.291846">26 17' 30.6456" S</abbr>
  <abbr class="longitude" title="28.097212">28 5' 49.9632" E</abbr>
  '''

  lat = soup.find("abbr", {"class": "latitude"})['title']
  lon = soup.find("abbr", {"class": "longitude"})['title']
  return (str(lat), str(lon))

def getLatLongTupleNoExp(ref):
  try:
    return getLatLongTuple(ref)
  except:
    return None

def textAfterEquals(s):
  return s[s.index('=')+2:]

file_list = []
with open("input.txt", "r") as f:
  for line in f:
    line = line.strip()
    file_list.append(line)

count = 1
index = 0
while index < len(file_list):
  if file_list[index] == '{{SAHRA heritage site row':
    ref = textAfterEquals(file_list[index+2])
    if textAfterEquals(file_list[index+10]) == '':
      print '\n' + str(count)
      count += 1
      print 'No Location for ' + ref
      tu = getLatLongTupleNoExp(ref)
      if tu is not None:
        file_list[index+10] = '| Latitude = ' + tu[0]
        file_list[index+11] = '| Longitude = ' + tu[1]
        print 'Added Location for ' + ref
      else:
        print "Couldn't find location for " + ref
  index += 1

f = open('output.txt','w')
for line in file_list:
  f.write(line + '\n')
f.close()
