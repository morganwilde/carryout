fileI = open("grain.in", "r")
fileO = open("grain.out", "w+")

# n - the number of lines left to read in the file, range [1, 10000]
n = (fileI.readline())
# db - dict with grain totals for each brand
db = {}
# k1, k2, k3 - dicts to store info if the King received more grain of type
k1 = {}
k2 = {}
k3 = {}

def updateKings(brand, count):
	"""
	Saves the info of extra grain each King received
	brand - type of grain, range [A, Z]
	count - the total number of grains for the brand
	"""
	remainder = count % 3
	index = int(str(count)[-2:])
	kings = []

	# Specific ordering of kings for each index range
	if   index >= 1 and index <= 33: kings = [k1, k2, k3]
	elif index >= 34 and index <= 66:kings = [k2, k3, k1]
	elif index >= 67 and index <= 99:kings = [k3, k1, k2]
	
	# Distribute grain while there're any left
	for king in kings:
		if remainder > 0: king[brand] += 1
		remainder -= 1
			
# Find the total number of grains of each brand
for line in fileI:
	grain  = line.split()
	brand  = grain[0]
	number = grain[1]
	# Insert each brand into k1, k2, k3
	k1[brand] = 0;
	k2[brand] = 0;
	k3[brand] = 0;

	if db.get(brand, None) == None:
		db[brand]  = int(number)
	else:
		db[brand] += int(number)

# Once the totals are ready, distribute the grain
for key in sorted(db.iterkeys()):
	# This will store the distribution summary for each of the 3 Kings
	out = ['', '', '']
	updateKings(key, db[key])

	if db[key] % 100 == 0:
		# Assign each list item to '-'
		out[0:2] = '-' * 3
	else:	
		# Check for Kings with extra grains
		if k1[key] == 1:out[0] = '+'
		else:			out[0] = '='
		if k2[key] == 1:out[1] = '+'
		else:			out[1] = '='
		if k3[key] == 1:out[2] = '+'
		else:			out[2] = '='

	# Output the result
	fileO.write(key + " " + ''.join(out) + "\n")
