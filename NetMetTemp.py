import pyTempNet as tn
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import matplotlib.pyplot as pl
plt.switch_backend('agg')
time_table_val = []
time_table_nr = []
tab_time = []
number=0
bet_edge=[]
rr_num = 0
r_num = 0
active_nodes_list = []
active_nodes_list_time = []
new_active_nodes = []
new_active_nodes_time = []
nowe_active = []
new_time_con = []
time_cc = []
con_t = []
con = []
contacts = 0
nr_r = 0
time_con = 0
distance_list = []
found_a = 0
found_b = 0
koniec = 0
global_eff=0
ideal_gl_eff=0
all_nodes_number=0
nodes_number = []
inst_con = []
distance = []
time_alive = []
efficiency = []
average_num = []
bet_nodes = []

ideal_gl_eff = 0
to_copy_list = []
to_copy_list_time = []
copy = []
copy_list = []
copy_time = []
copy_list_time = []
contacts_timestep = []

global_eff = 0
all_nodes_number = 0
nr_con = 0
contacts_for_node = []
num_con = 0
def distance_count():

    global_eff=0
    ideal_gl_eff=0
    all_nodes_number=0
    found_b=0
    nr_con=0
    found_a=0
    num_con=0
    for x in range(0, len(time_table_nr)):

        for i in range(0, len(t.nodes)):
            distance[i] = 0
        dist_all = 0
        to = time_table_val[x]
        nr = time_table_nr[x]
        print(to)

        for tt in range(nr, len(node_contacts)):
            if node_contacts[tt][2] == to:
                inst_con[int(node_contacts[tt][0]) - 1][1] += 1
                found_dwa = 1
                done = 1
                nr_con += 1
                if int(time_alive[int(node_contacts[tt][0]) - 1][3]) == 0:
                    time_alive[int(node_contacts[tt][0]) - 1][1] = node_contacts[tt][2]
                    time_alive[int(node_contacts[tt][0]) - 1][3] = 1
                else:
                    time_alive[int(node_contacts[tt][0]) - 1][2] = node_contacts[tt][2]

                for r in range(0, len(active_nodes_list)):
                    copy = []
                    copy_time = []
                    copy_list = []
                    copy_list_time = []
                    for rr in range(0, len(active_nodes_list[r])):
                        rr_time = rr - 1
                        if active_nodes_list[r][rr] == node_contacts[tt][0]:
                            found_a += 1
                            if rr != len(active_nodes_list[r]) - 1:
                                if active_nodes_list[r][rr + 1] == node_contacts[tt][1]:
                                    found_dwa -= 1
                        if active_nodes_list[r][rr] == node_contacts[tt][1]:
                            found_b += 1
                        koniec = active_nodes_list[r][len(active_nodes_list[r]) - 1]

                        copy.extend([active_nodes_list[r][rr]])
                        if rr > 0:
                            copy_time.extend([active_nodes_list_time[r][rr_time]])
                        if rr >= 1 and len(copy) > 1:

                            if active_nodes_list[r][rr] == node_contacts[tt][0] and found_b == 0:
                                copy_list.extend(copy)
                                copy_list.extend([node_contacts[tt][1]])

                                copy_list_time.extend(copy_time)
                                copy_list_time.extend([node_contacts[tt][2]])
                                # print(copy_list)
                                # print(copy_list_time)
                                to_copy_list.append(copy_list)
                                to_copy_list_time.append(copy_list_time)

                    del (copy_time)
                    del (copy)

                    del (copy_list_time)
                    del (copy_list)
                    found_a = 0
                    found_b = 0
                active_nodes_list.extend(to_copy_list)
                active_nodes_list_time.extend(to_copy_list_time)
                delete_nodes_list(to_copy_list)
                delete_nodes_list(to_copy_list_time)
                active_nodes_list.append([node_contacts[tt][0], node_contacts[tt][1]])
                active_nodes_list_time.append([node_contacts[tt][2]])
        # print(active_nodes_list)
        # print(active_nodes_list)
        contacts_timestep.append(nr_con)
        nr_con = 0

        for y in range(0, len(active_nodes_list)):
            # print(active_nodes_list[y])
            # print(active_nodes_list_time[y])
            for xx in range(0, len(active_nodes_list[y])):
                for xxx in range(xx + 1, len(active_nodes_list[y])):

                    time_zero = xx
                    time = xxx - 1
                    if active_nodes_list_time[y][time] == active_nodes_list_time[y][time_zero]:
                        time_diff = 1
                    else:
                        time_diff = abs(active_nodes_list_time[y][time] - active_nodes_list_time[y][time_zero]) / 15

                    if time_diff < D[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1]:
                        Di[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1] += 1
                        nodes_number[int(active_nodes_list[y][xx]) - 1][1] += 1
                        nodes_number[int(active_nodes_list[y][xxx]) - 1][1] += 1
                        D[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1] = time_diff

        for ii in range(0, len(t.nodes)):
            for jj in range(0, len(t.nodes)):
                if D[ii][jj] == 300 or D[ii][jj] == 0:
                    distance[ii] += 0
                else:
                    distance[ii] += 1 / D[ii][jj]
            dist_all += distance[ii]
        global_eff += float(1.0 / (len(t.nodes) * (len(t.nodes) - 1)) * dist_all)
        #print(inst_con)
        # print(nodes_number)
        #print(D)
    #print(t.nodes)
    #print(efficiency)
    for ii in range(0, len(t.nodes)):
        print(ii)
        all_nodes_number += nodes_number[ii][1]
        time_alive[ii][3] = abs(time_alive[ii][1] - time_alive[ii][2])
        efficiency[ii][1]='% .4f' % float(1.0 / len(time_table_val) * int(distance[ii]))
        average_num[ii][1]='% .4f' % float(1.0 / len(time_table_val) * int(inst_con[ii][1]))
        bet_nodes[ii][1]='% .4f' % float(1.0 / len(time_table_val) * float(int(nodes_number[ii][1])) / float(all_nodes_number))
    for ii in range(0, len(t.nodes)):
        for jj in range(0, len(t.nodes)):
            if ii != jj:
                D_id[ii][jj] = 1
            num_con += Di[ii][jj]
            Di[ii][jj] = '% .4f' % float(1.0 / len(time_table_val) * float(Di[ii][jj] / all_nodes_number))
            ideal_gl_eff += D_id[ii][jj]

        contacts_for_node.append(num_con)
        num_con = 0

    plik = open(nazwa + "_data", 'a')
    plik.write("nazwa" + '\t' + "nodes" + '\t' + "cont" + '\t' + "tsteps" + '\t' + "time" + '\t' + "glob eff" + '\t')
    plik.write('\n')
    plik.write(nazwa + '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' + str(
        len(time_table_val)) + '\t' + str(t.getObservationLength()) + '\t' + str(
        '% .4f' % float((1.0 / len(time_table_val) * global_eff) / ideal_gl_eff)) + '\t')
    plik.write('\n')
    plik.write("nodes" + '\t' + "eff" + '\t' + "av_n" + '\t' + "b_n" + '\t' + "talive" + '\t')
    plik.write('\n')
    for ii in range(0, len(t.nodes)):
        plik.write('\n')
        plik.write(
            str(t.nodes[ii]) + '\t' + str(efficiency[ii][1]) + '\t' + str(average_num[ii][1]) + '\t' + str(bet_nodes[ii][1]) + '\t' + str(
                '% .4f' % float(time_alive[ii][3])) + '\t')
    plik.write('\n')
    plik.write("bett_edge")
    for ii in range(0, len(t.nodes)):
        plik.write('\n')
        for jj in range(0, len(t.nodes)):
            plik.write(str(Di[ii][jj]) + " \t")
            bet_edge.append([ii,jj,Di[ii][jj]])
    plik.write('\n')

    print(D)

    #delete_nodes_list (active_nodes_list)
    #print(active_nodes_list)
    print('% .4f' % float((1.0 / len(time_table_val) * global_eff) / ideal_gl_eff))
    return '% .4f' % float((1.0 / len(time_table_val) * global_eff) / ideal_gl_eff)



def distance_count2(number,node_contacts,active_nodes_list,active_nodes_list_time):

    global_eff=0
    ideal_gl_eff=0
    all_nodes_number=0
    found_b=0
    nr_con=0
    found_a=0
    num_con=0
    #print(node_contacts)
    for x in range(0, len(time_table_nr)):
        print(active_nodes_list)
        for i in range(0, len(t.nodes)):
            distance[i] = 0
        dist_all = 0
        to = time_table_val[x]
        nr = time_table_nr[x]
        print(to)

        for tt in range(0, len(node_contacts)):
            #print(str(node_contacts[tt][2])+" "+str(to))
            if node_contacts[tt][2] == to:
                inst_con[int(node_contacts[tt][0]) - 1][1] += 1
                found_dwa = 1
                done = 1
                nr_con += 1
                if int(time_alive[int(node_contacts[tt][0]) - 1][3]) == 0:
                    time_alive[int(node_contacts[tt][0]) - 1][1] = node_contacts[tt][2]
                    time_alive[int(node_contacts[tt][0]) - 1][3] = 1
                else:
                    time_alive[int(node_contacts[tt][0]) - 1][2] = node_contacts[tt][2]

                for r in range(0, len(active_nodes_list)):
                    copy = []
                    copy_time = []
                    copy_list = []
                    copy_list_time = []
                    for rr in range(0, len(active_nodes_list[r])):
                        rr_time = rr - 1
                        if active_nodes_list[r][rr] == node_contacts[tt][0]:
                            found_a += 1
                            if rr != len(active_nodes_list[r]) - 1:
                                if active_nodes_list[r][rr + 1] == node_contacts[tt][1]:
                                    found_dwa -= 1
                        if active_nodes_list[r][rr] == node_contacts[tt][1]:
                            found_b += 1
                        koniec = active_nodes_list[r][len(active_nodes_list[r]) - 1]

                        copy.extend([active_nodes_list[r][rr]])
                        if rr > 0:
                            copy_time.extend([active_nodes_list_time[r][rr_time]])
                        if rr >= 1 and len(copy) > 1:

                            if active_nodes_list[r][rr] == node_contacts[tt][0] and found_b == 0:
                                copy_list.extend(copy)
                                copy_list.extend([node_contacts[tt][1]])

                                copy_list_time.extend(copy_time)
                                copy_list_time.extend([node_contacts[tt][2]])
                                # print(copy_list)
                                # print(copy_list_time)
                                to_copy_list.append(copy_list)
                                to_copy_list_time.append(copy_list_time)

                    del (copy_time)
                    del (copy)

                    del (copy_list_time)
                    del (copy_list)
                    found_a = 0
                    found_b = 0
                active_nodes_list.extend(to_copy_list)
                active_nodes_list_time.extend(to_copy_list_time)
                delete_nodes_list(to_copy_list)
                delete_nodes_list(to_copy_list_time)
                active_nodes_list.append([node_contacts[tt][0], node_contacts[tt][1]])
                active_nodes_list_time.append([node_contacts[tt][2]])

                # print(active_nodes_list)
                # print(active_nodes_list)
            contacts_timestep.append(nr_con)

            nr_con = 0

        for y in range(0, len(active_nodes_list)):
            # print(active_nodes_list[y])
            # print(active_nodes_list_time[y])
            for xx in range(0, len(active_nodes_list[y])):
                for xxx in range(xx + 1, len(active_nodes_list[y])):

                    time_zero = xx
                    time = xxx - 1
                    if active_nodes_list_time[y][time] == active_nodes_list_time[y][time_zero]:
                        time_diff = 1
                    else:
                        time_diff = abs(active_nodes_list_time[y][time] - active_nodes_list_time[y][time_zero]) / 15

                    if time_diff < D[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1]:
                        Di[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1] += 1
                        nodes_number[int(active_nodes_list[y][xx]) - 1][1] += 1
                        nodes_number[int(active_nodes_list[y][xxx]) - 1][1] += 1
                        D[int(active_nodes_list[y][xx]) - 1][int(active_nodes_list[y][xxx]) - 1] = time_diff
        print(D)

        for ii in range(0, len(t.nodes)):
            for jj in range(0, len(t.nodes)):
                if D[ii][jj] == 300 or D[ii][jj] == 0:
                    distance[ii] += 0
                else:
                    distance[ii] += float(1.0 / D[ii][jj])

            dist_all += distance[ii]

        global_eff += float(1.0 / (len(t.nodes) * (len(t.nodes) - 1)) * dist_all)
        #print(inst_con)
        # print(nodes_number)
        #print(D)
    for ii in range(0, len(t.nodes)):

        all_nodes_number += nodes_number[ii][1]
    for ii in range(0, len(t.nodes)):
        for jj in range(0, len(t.nodes)):
            if ii != jj:
                D_id[ii][jj] = 1
            num_con += Di[ii][jj]
            Di[ii][jj] = '% .4f' % float(1.0 / len(time_table_val) * float(Di[ii][jj] / all_nodes_number))
            ideal_gl_eff += D_id[ii][jj]

        contacts_for_node.append(num_con)
        num_con = 0
    print (ideal_gl_eff)
    print(global_eff)
    print('% .4f' % float((1.0 / len(time_table_val) * global_eff) / ideal_gl_eff))
    delete_nodes_list(active_nodes_list)
    print(D)
    return '% .4f' % float((1.0 / len(time_table_val) * global_eff) / ideal_gl_eff)


def wykresy():
    print("aktywnosc nodow w ukladzie")
    fig = pl.bar(range(0, len(time_table_nr)), contacts_timestep)
    pl.axis([0, len(time_table_nr) , 0, max(contacts_timestep) ])
    pl.title('aktywnosc nodow w ukladzie')
    pl.xlabel("nodes")
    pl.ylabel("liczba polaczen")

    pl.savefig("aktywnosc_n_" + nazwa + ".png")
    pl.cla()


    print("rozklad stopni wierzcholkow")
    fig = pl.hist(contacts_for_node, len(contacts_for_node), density=1, facecolor='blue', alpha=0.5)
    pl.title('rozklad stopni wierzcholkow')
    pl.xlabel("k")
    pl.ylabel("P")
    pl.savefig("rozklad_s_w_" + nazwa + ".png")
    pl.cla()

    print("histogram czasu wystepowania wezla w ukladzie")
    fig = pl.hist(time_alive , density=1, facecolor='blue', alpha=0.5)
    pl.title('histogram czasu wystepowania wezla w ukladzie')
    pl.xlabel("t")
    pl.ylabel("P")
    pl.savefig("hist_czas_" + nazwa + ".png")
    pl.cla()

    print("histogram l. kontaktow")
    fig = pl.hist(contacts_timestep , density=1, facecolor='blue', alpha=0.5)
    pl.title('histogram l. kontaktow')
    pl.xlabel("con")
    pl.ylabel("P")
    pl.savefig("hist_l_k_" + nazwa + ".png")
    pl.cla()

def time_table(time_tabel_val, time_table_nr, node_contacts):
    to = node_contacts[0][2]
    n = 0
    time_table_val.append(to)
    time_table_nr.append(0)
    for k in range(0, len(node_contacts)):  # dla danego czasu podawany indeks do tedges
        if node_contacts[k][2] != to:
            to = node_contacts[k][2]
            time_table_val.append(to)
            time_table_nr.append(k)

        n = n + 1

def delete_nodes_list(nodes):
    for n in range(0, len(nodes)):
        nodes.remove(nodes[0])

def list_of_contacts():
    node_contacts=[]

    for i in range(0,len(t.tedges)):
        nodes = []
        nodes2=[]
        for ii in range(0, 3):
            nodes.append(0)
            nodes2.append(0)
        for j in range(0,3):
            nodes[j]=int(t.tedges[i][j])

        nodes2[0] = int(t.tedges[i][1])
        nodes2[1] = int(t.tedges[i][0])
        nodes2[2] = int(t.tedges[i][2])
        node_contacts.append(nodes)
        node_contacts.append(nodes2)

    return node_contacts

print("Temporal network robustness")
with open("/home/marta/mode", "r") as f:
    for line in f:
        data = line.split("\t")
        #zmienic
        nazwa = data[0]
        numero = (int(data[1]))
        delta = (int(data[2]))
        r = (data[3])
        r_p = (float(data[4]))


t = tn.readFile('/home/marta/Downloads/' + nazwa + '_network.tedges', sep=" ", fformat="TEDGE",
                        timestampformat="%s",
                        maxlines=sys.maxsize)
t.setMaxTimeDiff(15)
t.nodes.sort()
D = np.zeros((len(t.nodes), len(t.nodes)))
Di = np.zeros((len(t.nodes), len(t.nodes)))
D_id = np.zeros((len(t.nodes), len(t.nodes)))
for i in range(0, len(t.nodes)):
    nodes_number.append([i, 0])
    efficiency.append([i, 0])
    average_num.append([i, 0])
    bet_nodes.append([i, 0])
    inst_con.append([i, 0])
    distance.append(0)
    time_alive.append([i, 0, 0, 0])

for v in range(0, len(t.nodes)):
    for w in range(0, len(t.nodes)):
        D[v][w] = 300
nodes = []
nodes2 = []
node_contacts = list_of_contacts()
time_table(time_table_val, time_table_nr, node_contacts)

e_przed=distance_count()


wykresy()

if r == 'r':
    print("attack random")
    # print(node_contacts)
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))

    a = np.zeros((len(t.nodes), len(t.nodes)))
    new_node_contacts = []
    active_nodes_list1=[]
    active_nodes_list_time1=[]
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300

    for ii in range(0, int(len(t.nodes) * r_p)):
        ran_num = (random.randint(1, len(t.nodes)))

        print(str((ran_num )) + " usuniety node")

        for c in range(0, len(node_contacts)):

            if (int(node_contacts[c][0]) == int(ran_num) or int(node_contacts[c][1]) == int(ran_num)):
                print("lol")
            else:
                new_node_contacts.append(node_contacts[c])

    e_po=distance_count2(len(t.nodes)-ii, new_node_contacts, active_nodes_list1, active_nodes_list_time1)

if r == 'f':
    print("attack efficiency")
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))

    a = np.zeros((len(t.nodes), len(t.nodes)))
    new2_node_contacts = []
    active_nodes_list2=[]
    active_nodes_list_time2=[]
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300

    print (efficiency)
    stop = 0
    while (stop != len(efficiency) - 1):
        stop = 0
        for ii in range(0, len(efficiency) - 1):

            if (efficiency[ii][1] > efficiency[ii + 1][1]):
                temp = efficiency[ii]
                efficiency[ii] = efficiency[ii + 1]
                efficiency[ii + 1] = temp
            else:
                stop += 1
    print(efficiency)

    for ii in range(0, int(len(t.nodes) * r_p)):

        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == int(efficiency[len(efficiency)-1][0]+1) or int(node_contacts[c][1]) == int(efficiency[len(efficiency)-1][0])+1):
                print("lol")
            else:
                new2_node_contacts.append(node_contacts[c])
        del efficiency[len(efficiency)-1]

    e_po = distance_count2(len(efficiency),new2_node_contacts,active_nodes_list2,active_nodes_list_time2)
if r == 'a':
    print("attack average node number")
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))

    a = np.zeros((len(t.nodes), len(t.nodes)))
    new3_node_contacts = []
    active_nodes_list3=[]
    active_nodes_list_time3=[]
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300

    print(average_num)
    stop = 0
    while (stop != len(average_num) - 1):
        stop = 0
        for ii in range(0, len(average_num) - 1):

            if (average_num[ii][1] > average_num[ii + 1][1]):
                temp = average_num[ii]
                average_num[ii] = average_num[ii + 1]
                average_num[ii + 1] = temp
            else:
                stop += 1
    print(average_num)
    for ii in range(0, int(len(t.nodes) * r_p)):
        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == int(average_num[len(efficiency) - 1][0]+1) or int(node_contacts[c][1]) == int(average_num[len(efficiency) - 1][0])+1):
                print("lol")
            else:
                new3_node_contacts.append(node_contacts[c])
        del average_num[len(average_num) - 1]


    e_po = distance_count2(len(average_num), new3_node_contacts, active_nodes_list3, active_nodes_list_time3)
if r == 'n':
    print("atack betweenness node")
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))

    a = np.zeros((len(t.nodes), len(t.nodes)))
    new4_node_contacts = []
    active_nodes_list4=[]
    active_nodes_list_time4=[]
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300
    print(bet_nodes)
    stop = 0
    while (stop != len(bet_nodes) - 1):
        stop = 0
        for ii in range(0, len(bet_nodes) - 1):

            if (bet_nodes[ii][1] > bet_nodes[ii + 1][1]):
                temp = bet_nodes[ii]
                bet_nodes[ii] = bet_nodes[ii + 1]
                bet_nodes[ii + 1] = temp
            else:
                stop += 1
    print(bet_nodes)
    for ii in range(0, int(len(t.nodes) * r_p)):
        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == int(bet_nodes[len(bet_nodes) - 1][0]+1) or int(node_contacts[c][1]) == int(bet_nodes[len(bet_nodes) - 1][0])+1):
                print("lol")
            else:
                new4_node_contacts.append(node_contacts[c])
        del bet_nodes[len(bet_nodes) - 1]

    e_po = distance_count2(len(bet_nodes), new4_node_contacts, active_nodes_list4, active_nodes_list_time4)

if r == 'e':
    print("attack betweeness edge")
    e_list = []
    new5_node_contacts = []
    active_nodes_list5=[]
    active_nodes_list_time5=[]
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))

    a = np.zeros((len(t.nodes), len(t.nodes)))

    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300
    print(bet_edge)
    stop = 0
    while (stop != len(bet_edge) - 1):
        stop = 0
        for ii in range(0, len(bet_edge) - 1):

            if (bet_edge[ii][2] > bet_edge[ii + 1][2]):
                temp = bet_edge[ii]
                bet_edge[ii] = bet_edge[ii + 1]
                bet_edge[ii + 1] = temp
            else:
                stop += 1
    print(bet_edge)
    for ii in range(0, int(len(t.nodes) * r_p)):

        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == int(bet_edge[len(bet_edge)-1][0])+1 and int(node_contacts[c][1]) == int(bet_edge[len(bet_edge)-1][1])+1):
                print("lol")
            else:
                new5_node_contacts.append(node_contacts[c])
        del bet_edge[len(bet_edge)-1]


    e_po = distance_count2(len(t.nodes)-ii, new5_node_contacts, active_nodes_list5, active_nodes_list_time5)


plik2 = open(nazwa + "_attack", 'a')
plik2.write(
    "nazwa" + '\t' + "rozd" + '\t' + "P" + '\t' + "nodes" + '\t' + "cont" + '\t' + "tsteps" + '\t' + "time" + '\t' + "Eprzed" + '\t' + "E po" + '\t' + "R")
plik2.write('\n')
plik2.write(nazwa + '\t' + r + '\t' + str(r_p) + '\t' + str(len(t.nodes)) + '\t' + str(
    len(node_contacts)) + '\t' + str(len(time_table_val)) +
            '\t' + str(t.getObservationLength()) + '\t' + str(e_przed) + '\t' + str(e_po) + '\t' + str(float(e_po)/float(e_przed)))
plik2.write('\n')
