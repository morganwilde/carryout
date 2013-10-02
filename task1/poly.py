def powSafe(base, total, module):
	return (base * total) % module

def poly(x, m, coefs):
	value = 0
	for coef in coefs:
		if value == 0: valueTemp = 1
		else: valueTemp = powSafe(x, valueTemp, m)
		value += (valueTemp * coef) % m

	return str(value % m) # This will be concatenated with a str

fileI = open("poly.in", "r")
fileO = open("poly.out", "w+")

# First line contains n and k ints
line1 = fileI.readline().split()
n, k = int(line1[0]), int(line1[1])

# Second line has all the polynomial coefficients
line2 = fileI.readline().split()
# Create a list of by converting each item on line2 to int
coefficients = [int(c) for c in line2]

# Calculate polynomial for each X
for line in fileI:
	linel = line.split()
	x, m = int(linel[0]), int(linel[1])

	fileO.write(poly(x, m, coefficients) + "\n")

# Free up memory
fileI.close()
fileO.close()
