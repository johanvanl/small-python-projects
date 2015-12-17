from bs4 import BeautifulSoup

import sys
import urllib2

def readFile(fn):
    with open(fn, 'r') as f:
        data = f.read()
    return data

def writeFile(fn, content):
    with open(fn, 'w') as f:
        f.write(content)

def urlToString(url):
    f = urllib2.urlopen(url)
    return f.read()

def printHelp():
    print 'Use JMeterFromSitemap in one of the following two ways:'
    print '    $ python JMeterFromSitemap.py -file <filename>'
    print '    $ python JMeterFromSitemap.py -url <url>'

element = """
<HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="%s" enabled="true">
<elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
<collectionProp name="Arguments.arguments"/>
</elementProp>
<stringProp name="HTTPSampler.domain"></stringProp>
<stringProp name="HTTPSampler.port"></stringProp>
<stringProp name="HTTPSampler.connect_timeout"></stringProp>
<stringProp name="HTTPSampler.response_timeout"></stringProp>
<stringProp name="HTTPSampler.protocol"></stringProp>
<stringProp name="HTTPSampler.contentEncoding"></stringProp>
<stringProp name="HTTPSampler.path">%s</stringProp>
<stringProp name="HTTPSampler.method">GET</stringProp>
<boolProp name="HTTPSampler.follow_redirects">true</boolProp>
<boolProp name="HTTPSampler.auto_redirects">false</boolProp>
<boolProp name="HTTPSampler.use_keepalive">true</boolProp>
<boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
<boolProp name="HTTPSampler.image_parser">true</boolProp>
<boolProp name="HTTPSampler.monitor">false</boolProp>
<stringProp name="HTTPSampler.embedded_url_re"></stringProp>
</HTTPSamplerProxy>
<hashTree/>
"""

if len(sys.argv) < 3:
    printHelp()
    exit(0)

data = readFile('full_site_test_head.txt')

xml = ''
if sys.argv[1] == '-file':
    xml = readFile(sys.argv[2])
elif sys.argv[1] == '-url':
    xml = urlToString(sys.argv[2])
else:
    printHelp()
    exit(0)

soup = BeautifulSoup(xml, 'html.parser')
for link in soup.find_all('loc'):
    data += element % (link.string, link.string)

data += readFile('full_site_test_tail.txt')

writeFile('full_site_test.jmx', data)
