#!/usr/bin/python2.7

# Standard Library Imports.
from urllib2 import urlopen

# Third-party Imports.
from bs4 import BeautifulSoup
from pandas import DataFrame, option_context

if __name__ == "__main__":
    # Hard-coded URL for the web-page containing touchdown statistics.
    url = "https://finance.yahoo.com/quote/AAPL/history?ltr=1"

    # Parse the web-page and extract the table using Beautiful Soup.
    table = BeautifulSoup(urlopen(url).read(), "html.parser").find(
        "table", {"data-test": "historical-prices"})

    # Extract the header names from the th tags in thead tag.
    cols = [col.text for col in table.find("thead").find_all("th")]

    # Extract the table and translate it into a data frame, skipping both
    # the header row and trailing row that contains footnotes.
    data = DataFrame([[col.text for col in row]
                      for row in list(table.find_all("tr"))[1:-1]],
                     columns=cols)

    # Output the result to standard out.
    with option_context('display.max_rows', None):
        print data[["Date", "Close*"]]