# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# The net two lines to scraperwiki library 
import scraperwiki
import lxml.html
#
print("Hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print[html]
#i am coding
print(html)
record = {}
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print(root.cssselect("div#footer"))
listofmatches=root.cssselect("a")
for match in listofmatches:
  print(match)
  record["link"]=lxml.html.tostring(match)
  print(record)
  scraperwiki.sqlite.save(unique_keys=['link'], data=record)
  print(lxml.html.tostring(match))
# c
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
