x = [int(x) for x in input("Enter The Elements in First Matrix: ").split()]
y = [int(y) for y in input("Enter The Elements in Second Matrix: ").split()]

a = (x[0] * y[0]) + (x[1] * y[2])
b = (x[0] * y[1]) + (x[1] * y[3])
c = (x[2] * y[0]) + (x[3] * y[2])
d = (x[2] * y[1]) + (x[3] * y[3])

print ("The Product of The Given 2x2 Matrix is")
print ("%d\t%d\n%d\t%d" % (a,b,c,d))
