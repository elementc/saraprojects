import csv, sys

# If we do not have as many arguments as we're supposed to, we should print a friendly hint and bail out.
if len(sys.argv[1]) != 2:
	print("Usage: python zipcoder.py <your zipcode sequence of interest>")
	quit()

# Grab the thing to look for from the program's arguments.
target = sys.argv[1]

# Open the zip code data to look through.
with open('uszips.csv') as csvfile:
	# Treat the data as a table of "dictionaries" which let us ask for specific columns by name.
	reader = csv.DictReader(csvfile)
	# Loop over the rows in the table...
	for row in reader:
		# ...looking for rows that have the thing we're looking for inside the zip code column...
		if target in row['zip']:
			# ...and print the matches!
			print(row['zip'] + " - " +row['city'] + ", " + row['state_name'])
