import sys
import pickle
ff = "sg_infectious_contact_list/listcontacts_2009_"
fff = "sg_infectious_contact_list/"


#file_file = input('Enter name of the file: ')
file_file="05_03.txt"
file_name = ff + file_file
# file_name="sg_infectious_contact_list/listcontacts_2009_05_01.txt"

#file_new = input('Enter new file name: ')
file_new="aaaa.tedges"

# new_file_tedge="sg_infectious_contact_list/plik1.tedges"

new_file_tedge = fff + file_new
file = open(new_file_tedge, "a+")

tekst = "node1" + " " + "node2" + " " + "time" + "\n"
print(tekst)
file.write(tekst)
zero=0
with open(file_name) as f:
    for line in f:

        data = line.split("\t")

        t = (int(data[0]))
        node_one = (int(data[1]))
        node_two = (int(data[2]))
        if zero==0:
            t_zero=t
            zero=1


        dane = str(node_one)+" "+ str(node_two)+" "+ str(t-t_zero)+" " + "\n"

        # print("Linia zrobiona")
        print(dane)
        file.write(dane)

f.close()
file.close()
