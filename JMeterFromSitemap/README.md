# JMeter from Sitemap

This Python script outputs a [JMeter](http://jmeter.apache.org/) test script that would for every thread visit every webpage on the website in a random order and collect some data.

All that needs to be passed to the script is the sitemap, this can be done by saving the sitemap to a file and running the script as follows:

```
$ python JMeterFromSitemap.py -file <filename>
```

Or to pass the url of the sitemap as a parameter, as folows:

```
$ python JMeterFromSitemap.py -url <url>
```

The JMeter script is saved in *full_site_test.jmx*.
