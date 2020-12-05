""" 12 THIS IS A TEST """

from pprint import pp
import csv
import sys


csv_path = None
if len(sys.argv) > 1: csv_path = sys.argv[1]
else: sys.exit(">>> You must specify one argument : the CSV complete file path. If the file is in the same folder as you are now, you can put just the filename (relative path).")
# csv_path = "/Users/c/Downloads/All videos in channel 0a4ac35aa7894489b85af84ffacfefe9.csv"


urls_to_write = []
with open(csv_path) as csv_file:
	csv_content = csv.reader(csv_file)
	for line_csv in csv_content:
		# print(line_csv)
		uri = [f for f in line_csv if "/watch?" in f]
		if (len(uri)) > 0:
			uri = uri[0]
			# print('uri:', uri)
			url = "https://youtube.com" + uri
			# print('url:', url)
			urls_to_write.append(url)
# pp(urls_to_write)


cleaned_csv_path = csv_path.replace(".csv", ".cleaned") + ".csv"
with open(cleaned_csv_path, "w+", newline="") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerows(urls_to_write)
	print("writing cleaned urls done!")
