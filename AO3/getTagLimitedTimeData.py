import sys

from toastyTools import (
    getAO3TagTimeframeURL,
    getArguments,
    getListFromTextFile,
    getNumWorksFromURL,
    prepCSVOutfile,
    writeEndlineToCSV,
    writeFieldToCSV,
)

DEBUG = 1

infile, startDate, endDate, outfile = getArguments(
    sys.argv,
    4,
    "Usage: getTagLimitedTimeData.py tagfile startDate endDate outfile (e.g., getTagLimitedData.py tags.txt 2020-01-01 2020-10-20 out.csv",
)

tags = getListFromTextFile(infile)
outfp = prepCSVOutfile(outfile, "tag,works " + startDate + " to " + endDate)

for tag in tags:
    if DEBUG:
        print(tag)

    writeFieldToCSV(outfp, tag)

    limitedURL = getAO3TagTimeframeURL(tag, [], [], startDate, endDate)
    if DEBUG:
        print(limitedURL)

    limitedWorks = getNumWorksFromURL(limitedURL, True)
    if DEBUG:
        print(limitedWorks)

    writeFieldToCSV(outfp, str(limitedWorks))

    writeEndlineToCSV(outfp)
