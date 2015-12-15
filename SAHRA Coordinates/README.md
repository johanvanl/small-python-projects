# SAHRA Coordinates

I found that the [List of Heritage Sites in South Africa](https://en.wikipedia.org/wiki/Category:Lists_of_heritage_sites_in_South_Africa) pages were very incomplete and wanted to help complete them by filling in all the missing coordinates.

On each of these pages the Heritage Sites are stored in tables, below is an example of a table row found in the page source.

```
{{SAHRA heritage site row
| guid = 856
| SiteReference = 9/2/258/0047
| Site_name = Old Agriculture Publication Building, Vermeulen Street, Pretoria
| Magisterial_district = Pretoria
| Municipal_name =
| Town = Pretoria
| Erf number =
| Farm number =
| Portion =
| Latitude = -25.744816
| Longitude = 28.192572
| NHRA status = Provincial Heritage Site
| NMC status = National monument
| Description =
| image =  Old Agriculture Publication Building Vermeulen Street Pretoria 002.jpg
|commonscat=Old Agriculture Publication Building, Pretoria
}}
```

What I would then do on each page is I would go through all the table rows and if the 'Latitude' is empty I would fill it in by using the Site Reference.

For the example above the Site Reference is '9/2/258/0047', the SAHRA website entry would then be http://www.sahra.org.za/sahris/sites/922580047 which has the reference, with the slashes removed, in the url.

In the page source I would find the following structure:

```
<span class="geo">
<abbr class="latitude" title="-25.755820">25° 45' 20.952" S</abbr>,
<abbr class="longitude" title="28.230870">28° 13' 51.132" E</abbr>
</span>
```

From the above structure I would then save the values in the 'title' attribute, namely '-25.755820' and '28.230870' into their respective places.

---

I used [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) to parse the HTML pages to get the latitude and longitude, which I downloaded and included in my project.
