#!/usr/bin/python2.7

# Standard Library Imports.
from urllib2 import urlopen

# Third-party Imports.
from bs4 import BeautifulSoup
from pandas import DataFrame, option_context

if __name__ == "__main__":
    # Hard-coded URL for the web-page containing touchdown statistics.
    url = ("https://www.wunderground.com/history/airport/KNYC/2015/1/11/"
           "MonthlyHistory.html")
    
    # Parse the web-page and extract the table using Beautiful Soup.
    table = BeautifulSoup(urlopen(url).read(), "html.parser").find(
        "table", id="obsTable")
    
    # Extract the header names, which are enclosed in the first tbody tag.
    cols = [col.text for col in table.find("tbody").find_all("td")]
    
    # Extract the table and translate it into a data frame.
    data = DataFrame([[col.text.strip() for col in row.find_all("td")]
                      for row in list(table.find_all("tbody"))[1:]],
                     columns=cols)
                     
    # Output the result to standard out.
    with option_context('display.max_rows', None):
        print data.iloc[:, 0:4]