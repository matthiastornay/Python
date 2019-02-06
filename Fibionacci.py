n = 0
a = 1
b = 1

times = input("n ? ")

while (n < times):
	n += 1
	c = b
	b += a
	a = c
	print(b)

