def gcdEuclid2(a, b):
	if a == 0 or b==0:
		return a + b
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return b
a = input("a = ")
b = input("b = ")
print "Greatest common divisor is : ",gcdEuclid2(a, b)
