default:

findings: output/trending-guests.tsv

output/trending-guests.tsv: scripts/find-trending-guests.py data/guests.csv
	./scripts/find-trending-guests.py < data/guests.csv > output/trending-guests.tsv
