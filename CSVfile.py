import csv
f=open("emp.csv","r")
ro=csv.reader(f)
ld=list(ro)
print(ld)