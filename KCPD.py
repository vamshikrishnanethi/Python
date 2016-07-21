import csv

print ("KCPD Crime Statistics\n")
def choice():
    c = int(input("1. Summary By Zip Code\n2. Victim Count By Offense Type\n3. Quit\nPlease Enter a Value: "))
    print ("")
    if c == 1:
        zipcode()
    elif c == 2:
        victim_count()
    elif c == 3:
        exit()
    else:
        print ("Please Choose from the Options Displayed")
        choice()
        
def zipcode():
    a = open("incidents.csv","rt")
    b = csv.reader(a)
    l = {}
    
    for row in b:
        try:
            if(l.get(row[4])):
                
                l.update({row[4]:l.get(row[4])+1})
            else:
                l.update({row[4]:1})        
        except Exception:
            pass

    l['99999'] = l['99999'] + l['0'] + l['']
    del l['0'],l[''],l['Zip Code']    

    print ("Summary By Zip Code")
    print ("==================")
    for k,v in sorted(l.items()):
        print(k,v)
    a.close()

def victim_count():
    x = open("incidents.csv","rt")
    y = csv.reader(x)
    z = {}
    d = open("offenses.csv","rt")
    e = csv.reader(d)
    f = {}
    g = {}

    for row in y:
        try:
            if(z.get(int(row[3]))):
                z.update({int(row[3]):z.get(int(row[3]))+1})
            else:
                z.update({int(row[3]):1})        
        except Exception:
            pass   

    for row in e:
        try:
            f.update({int(row[0]):row[1]})

        except ValueError:
            pass; 

    i = 0
    while i<30:
        g.update({f.get(i):z.get(i)})
        i += 1

    del g[None]

    print ("   Victim Count By Offense")
    print ("=============================")
    for key, value in sorted(g.items(), key = lambda t: t[1], reverse = True):
        print ("%-21s\t%5d" % (key,value))

choice()
