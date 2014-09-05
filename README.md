# "Rising" Sunday Show Guests 

This repository contains the data and code behind the September 5, 2014 BuzzFeed News post, "[Five Sunday Morning Show Guests Whose Stars Are Rising](http://buzzfeed.com/jsvine/five-sunday-morning-show-guests-whose-stars-are-rising)." 

## Data

The data — [`data/guests.csv`](data/guests.csv) — [comes from *The New York Times*'s The Upshot](http://www.nytimes.com/2014/09/06/upshot/looking-for-john-mccain-try-a-sunday-morning-show.html), via researchers at [American University](http://www.american.edu/spa/wpi/sunday-morning-monitor.cfm). The Upshot kindly [cleaned the data and published it to a GitHub repository](https://github.com/TheUpshot/Sunday-Shows), which is the basis for this analysis. 

## Analysis

A Python script, [`scripts/find-trending-guests.py`](scripts/find-trending-guests.py), counts the total number of appearances per guest, per year. Next it filters the guests, looking for the following three criteria:

- Guest has appeared at least five times this year (through August 3, the most recent Sunday in the dataset).

- Guest has appeared more times this year than any other year since January 2009.

- Guest's appearances this year account for at least one-third of all of appearances since 2009.

The script has one requirement, [`pandas`](https://github.com/pydata/pandas).

To execute the script on a Unix operating system, run `./scripts/find-trending-guests.py < data/guests.csv > output/trending-guests.tsv`, or simply `make findings`.
