import csv
import calendar

x = []
y = {}

try:
    a = input("Enter a File Name (To Read) With Extension: ")
    b = open(a, "rt")

    for row in b:
        if row[0:6] not in x:
            x.append(row[0:6])

    i = 0
    value = 0

    for s in x:
        d = open(a, "rt")
        e = csv.reader(d)
        for row in e:
            try:
                if(row[0][0:6] == s):
                    value += float(row[1])
                    continue

            except ValueError:
                pass

            except IndexError:
                pass

        y.update({s:value})
        value = 0
        
    c = input("Enter a File Name (To Write) With Extension: ")
    e = open(c, "wt", newline = '')
    f = csv.writer(e)

    for key,value in sorted(y.items()):
        f.writerow([key,value])
    e.close()

except IOError:
    print ("File Not Found....")

try:
    g = open(c, "rt")
    h = csv.reader(g)
    l = []

    for row in h:
        row[0] = row[0][4:6]
        if row[0] not in l:
            l.append(row[0])
        else:
            continue

    count = 0
    m = {}

    for j in l:
        n = open(c, "rt")
        o = csv.reader(n)
        for r in o:
            try:
                if (r[0][4:6] == j):
                    count += float(r[1])
                    continue

            except ValueError:
                pass

            except IndexError:
                pass
            
        m.update({calendar.month_name[int(j)]:(count/10)})
        count = 0

    print ("")
    print ("Average Monthly Rainfall(in mm) Over a Period of 10 Years")
    print ("=========================================================")
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for k,v in (sorted(m.items(),key =lambda x:months.index(x[0]))):
        print ("%-10s\t%8.4f" % (k,v))

except :
    print("File Not Found....");
