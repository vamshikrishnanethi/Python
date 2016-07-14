x = [1,2,3,4,5,6,7,8,9,10]
y = x[4:9]

def multiply():
    for a in y:
        for b in x:
            c = a * b
            print ("%d x %2d = %2d" % (a,b,c))
        print ("")
        
multiply()
