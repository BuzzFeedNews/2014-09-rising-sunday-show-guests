#!/usr/bin/env python
import pandas as pd
import sys

def get_guests_by_year(guests):
    years = guests["date"].apply(lambda d: d.year)
    year_counts = years.value_counts()
    guests_by_year = guests.groupby([ years, "name" ]).size().unstack(level=0)
    return guests_by_year

round_3 = lambda x: round(x, 3)

def condense_counts(counts):
    totals = counts.sum(axis=1)
    return pd.DataFrame({
        "total": totals,
        "n2014": counts[2014],
        "p2014": (counts[2014] * 1.0 / totals).apply(round_3),
        "is_max_in_2014": counts[2014] > counts[counts.columns[:-1]].max(axis=1)
    })

def filter_condensed(condensed):
    c = condensed
    return c[
        (c["is_max_in_2014"]) &
        (c["n2014"] >= 5) &
        (c["p2014"] >= round_3(1.0 / 3))
    ].sort("p2014", ascending=False)

def find_trending(f):
    guests = pd.read_csv(f, parse_dates=["date"])
    counts = get_guests_by_year(guests)
    condensed = condense_counts(counts)
    filtered = filter_condensed(condensed)
    return filtered

if __name__ == "__main__":
    trending = find_trending(sys.stdin)
    trending.reset_index().to_csv(sys.stdout, index=False, sep="\t")
