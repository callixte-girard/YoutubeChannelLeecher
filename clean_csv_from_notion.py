""" 12 THIS IS A TEST """

from static.methods import my_pp as pp
import csv
import sys
import os


csv_path = None
if len(sys.argv) > 1: csv_path = sys.argv[1]
else: sys.exit(">>> You must specify one argument : the CSV complete file path. If the file is in the same folder as you are now, you can put just the filename (relative path).")
# csv_path = "/Users/c/Downloads/All videos in channel 0a4ac35aa7894489b85af84ffacfefe9.csv"


rows_to_write = []
with open(csv_path, "r") as csv_file:
	csv_content = csv.reader(csv_file)
	for line_csv in csv_content:
		# print(line_csv)
		title = line_csv[0]
		uri = [f for f in line_csv if "/watch?" in f]
		if (len(uri)) > 0:
			# extract value from the array
			uri = uri[0]
			# print('uri:', uri)
			url = "https://youtube.com" + uri
			# print('url:', url)
			rows_to_write.append([url, title])
# pp(rows_to_write)

# now create the path for the clean csv...
cleaned_csv_path = csv_path.replace(".csv", ".cleaned") + ".csv"
# ...and "pre-overwrite" it if it already exists
if os.path.isfile(cleaned_csv_path): os.remove(cleaned_csv_path)

with open(cleaned_csv_path, "w", newline="") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerows(rows_to_write)
	print(">>> Writing cleaned urls done!")
