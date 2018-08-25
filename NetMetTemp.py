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
        #print active_nodes_list
        for i in range(0, len(t.nodes)):
            distance[i] = 0
        dist_all = 0
        to = time_table_val[x]
        nr = time_table_nr[x]
        print(to)

        for tt in range(nr, len(node_contacts)):
            #print(node_contacts)
            if node_contacts[tt][2] == to:
                inst_con[int(node_contacts[tt][0]) ][1] += 1
                found_dwa = 1
                done = 1
                nr_con += 1
                if int(time_alive[int(node_contacts[tt][0]) ][3]) == 0:
                    time_alive[int(node_contacts[tt][0]) ][1] = node_contacts[tt][2]
                    time_alive[int(node_contacts[tt][0]) ][3] = 1
                else:
                    time_alive[int(node_contacts[tt][0])][2] = node_contacts[tt][2]

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
        #print(active_nodes_list)
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

                    if time_diff < D[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ]:
                        Di[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ] += 1
                        nodes_number[int(active_nodes_list[y][xx]) ][1] += 1
                        nodes_number[int(active_nodes_list[y][xxx]) ][1] += 1
                        D[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ] = time_diff

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
        nodes[0] = int(t.tedges[i][0])
        nodes[1] = int(t.tedges[i][1])
        nodes[2] = int(t.tedges[i][2])

        nodes2[0] = int(t.tedges[i][1])
        nodes2[1] = int(t.tedges[i][0])
        nodes2[2] = int(t.tedges[i][2])
        node_contacts.append(nodes)
        node_contacts.append(nodes2)

    return node_contacts

def node_id_rm(node_contacts):
    for k in range(len(node_contacts)):
        for ii in range(len(t.nodes)):
            for jj in range(0,2):
                if node_contacts[k][jj]==int(t.nodes[ii]):
                    node_contacts[k][jj]=ii
#print("Temporal network robustness")
#with open("/home/marta/mode", "r") as f:
 #   for line in f:
  #      data = line.split("\t")
        #zmienic
   #     nazwa = data[0]

    #    delta = (int(data[1]))
        #r = (data[2])
        #r_p = float((data[3]))


t = tn.readFile( '05_01.tedges', sep=" ", fformat="TEDGE",
                        timestampformat="%s",
                        maxlines=sys.maxsize)
t.setMaxTimeDiff(20)
nazwa="05_01"
#print(t.Summary())
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
node_tab=[]

node_contacts = list_of_contacts()
time_table(time_table_val, time_table_nr, node_contacts)

node_id_rm(node_contacts)

e_przed=distance_count()


wykresy()


