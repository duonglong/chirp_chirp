def gcdEuclid(a, b):
	if a == 0:
		return b
	return gcdEuclid(a - b, b) if a > b else gcdEuclid(b - a, a)
a = input("A = ")
b = input("B = ")
print gcdEuclid(a ,b)
