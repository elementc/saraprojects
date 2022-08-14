import csv, sys

checked = 0
military = 0
nonmilitary = 0

# Open the zip code data to look through.
with open('uszips.csv') as csvfile:
	# Treat the data as a table of "dictionaries" which let us ask for specific
        # columns by name.
	reader = csv.DictReader(csvfile)
	# Loop over the rows in the table...
	for row in reader:
		checked = checked + 1
		# ...looking for rows that have the thing we're looking for inside the
                # military...
		if "FALSE" in row['military']:
			nonmilitary = nonmilitary + 1
		else:
			military = military + 1

print(f"checked: {checked}, military: {military}, nonmilitary: {nonmilitary}")
