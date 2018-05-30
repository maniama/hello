import sys
import pickle
import os
ff = "sg_infectious_contact_list/listcontacts_2009_"
fff = "sg_infectious_contact_list/"

print("There are 69 files")
number = input('How many files you want to join')
#number=2

def file_sort(file_name,file):
    with open(file_name) as f:
        for line in f:

            data = line.split("\t")

            t = (int(data[0]))
            node_one = (int(data[1]))
            node_two =(int(data[2]))

            dane = str(node_one)+" "+ str(node_two)+" "+ str(t)+" " + "\n"

            # print("Linia zrobiona")

            file.write(dane)
    print("DONE"+"    "+file_name)
    f.close()
#file_new = input('Enter new file name: ')
file_new="b.tedges"

# new_file_tedge="sg_infectious_contact_list/plik1.tedges"
uno='_'
dos='.txt'
m=5
d=5

new_file_tedge = fff + file_new
file = open(new_file_tedge, "a+")
tekst = "node1" + " " + "node2" + " " + "time" + "\n"
print(tekst)
file.write(tekst)
for x in range(0,number):
    dd = '0' + str(d)
    mm = '0' + str(m)

    if d<10:
        file_name=ff + mm + uno + dd + dos
        print(file_name)
        if os.path.isfile(file_name):
            file_sort(file_name, file)

        if m == 4 and d == 30:
            m = 5
            d = 1
        elif m == 5 and d == 31:
            m = 6
            d = 1
        elif m == 6 and d == 30:
            m = 7
            d = 1
        d+=1
    else:
        file_name=ff + mm + uno + str(d) + dos
        print(file_name)
        if os.path.isfile(file_name):
            file_sort(file_name, file)

        if m==4 and d==30:
            m=5
            d=1
        elif m==5 and d==31:
            m=6
            d=1
        elif m==6 and d==30:
            m=7
            d=1
        d+=1


    x+=1



file.close()
