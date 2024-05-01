import csv

filename = 'student.csv'
with open(filename,"r") as csfile:
    csvreader = csv.reader(csfile,delimiter=',')
    for row in csvreader:
       # print(row) #['Dias', '+7777777777']
        name,phone_number = row
        print(name,phone_number) #Dias +7777777777
        

