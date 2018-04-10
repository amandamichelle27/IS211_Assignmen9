#!/usr/bin/python2.7

# Standard Library Imports.
from urllib2 import urlopen

# Third-party Imports.
from bs4 import BeautifulSoup
from pandas import DataFrame

if __name__ == "__main__":
    # Hard-coded URL for the web-page containing touchdown statistics.
    url = ("https://www.cbssports.com/nfl/stats/playersort/nfl/"
           "year-2017-season-regular-category-touchdowns")

    # Parse the web-page and extract the table using Beautiful Soup.
    table = BeautifulSoup(urlopen(url).read(), "html.parser").find("table")

    # Extract the header names, which are enclosed in a SortableHeader class.
    cols = [col.text for col in table.find_all(
        "th", class_=["sortableColumn", "sortableColumnAsc"])]

    # Extract the table and translate it into a data frame.
    data = DataFrame([[col.text for col in row]
                      for row in list(table.find_all("tr"))[3:-1]],
                     columns=cols)

    # Output the result to standard out.
    print data[["Player", "Team", "TD"]][0:20]