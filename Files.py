# import csv
# with open('Team.csv','r') as csvfile:
#  data = csv.reader(csvfile, delimiter=' ')
#  for row in data:
#    print(' '.join(row))


import csv
with open('movies.csv', 'w') as file:
    writer1 = csv.writer(file)
    writer1.writerow(["SN", "Movie", "Protagonist"])
    writer1.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer1.writerow([2, "Harry Potter", "Harry Potter"])

