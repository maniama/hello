import pyTempNet as tn
import numpy as np
import sys
import random
time_table_val = []
time_table_nr = []
tab_time = []
number=0
bet_edge=[]
to_copy_list_nowe=[]
to_copy_list_nowe_time=[]
rr_num = 0
r_num = 0
active_nodes_list = []
active_nodes_list_time = []
new_active_nodes = []
new_active_nodes_time = []
new_to_dodac_list=[]
new_to_dodac_list_time=[]
new_to_copy_list_nowe=[]
new_to_copy_list_nowe_time=[]
new_to_copy_list=[]
new_to_copy_list_time=[]
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
to_dodac_list=[]
to_dodac_list_time=[]
to_copy_list_time = []
to_copy_list_nowe = []
to_copy_list_nowe_time = []
to_see_list=[]
to_see_list_time=[]
num_ac=[]
copy = []
copy_list = []
copy_time = []
copy_list_time = []
contacts_timestep = []
already=[]
global_eff = 0
all_nodes_number = 0
nr_con = 0
contacts_for_node = []
num_con = 0
new_nr_ac=[]
nr_ac=[]
efficiency = []
bet_nodes2 = []
bet_nodes3 = []
average_num = []
bet_nodes = []
t = tn.readFile( "example_network.tedges", sep=" ", fformat="TEDGE",
                        timestampformat="%s",
                        maxlines=sys.maxsize)
t.setMaxTimeDiff(20)
nazwa="example_network"
def time_table(time_tabel_val, time_table_nr, node_contacts):
    delete_nodes_list(time_table_nr)
    delete_nodes_list(time_table_val)
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


def distance_count2(number,node_contacts,active_nodes_list,active_nodes_list_time):
    to_see_list = []
    to_see_list_time = []
    to_copy_list_nowe = []
    to_copy_list_nowe_time = []
    global_eff = 0
    ideal_gl_eff = 0
    all_nodes_number = 0
    to_copy_list = []
    to_dodac_list = []
    to_copy_list_time = []
    to_dodac_list_time = []
    nr_con = 0
    num_con = 0
    time_table_val_num = []
    for i in range(0, len(t.nodes)):
        distance[i] = 0.0
    dist_all = 0.0
    for ii in range(len(time_table_val)):
        if ii == len(time_table_val) - 1:
            time_table_val_num.append([time_table_val[ii], len(node_contacts) - time_table_nr[ii]])
        else:
            time_table_val_num.append([time_table_val[ii], time_table_nr[ii + 1] - time_table_nr[ii]])
    # print(time_table_val_num)

    for tt in range(0, len(time_table_val_num)):

        num_nodes_contacts = time_table_nr[tt]
        print(time_table_val[tt])

        for ttt in range(0, time_table_val_num[tt][1]):

            inst_con[int(node_contacts[num_nodes_contacts][0])][1] += 1
            nr_con += 1
            if int(time_alive[int(node_contacts[num_nodes_contacts][0])][3]) == 0:
                time_alive[int(node_contacts[num_nodes_contacts][0])][1] = node_contacts[num_nodes_contacts][2]
                time_alive[int(node_contacts[num_nodes_contacts][0])][3] = 1
            else:
                time_alive[int(node_contacts[num_nodes_contacts][0])][2] = node_contacts[num_nodes_contacts][2]
            if len(active_nodes_list) == 0:
                active_nodes_list.append(
                    [node_contacts[num_nodes_contacts][0], node_contacts[num_nodes_contacts][1]])
                active_nodes_list_time.append([node_contacts[num_nodes_contacts][2]])
            else:
                num_ac = []
                identico_i = 0
                delete_nodes_list(to_see_list)
                delete_nodes_list(to_see_list_time)
                delete_nodes_list(to_copy_list)
                delete_nodes_list(to_copy_list_time)
                delete_nodes_list(to_copy_list_nowe)
                delete_nodes_list(to_copy_list_nowe_time)
                copy_i = 0
                dodac_i = 0
                nowe_i = 0
                for r in range(0, len(active_nodes_list)):
                    new_nr_ac = []

                    linia_active = list(active_nodes_list[r])
                    linia_active_t = list(active_nodes_list_time[r])

                    if node_contacts[num_nodes_contacts][0] in linia_active:
                        if node_contacts[num_nodes_contacts][1] in linia_active:
                            id_0 = linia_active.index(node_contacts[num_nodes_contacts][0])
                            id_1 = linia_active.index(node_contacts[num_nodes_contacts][1])
                            if id_0 + 1 != id_1:
                                if id_0 < id_1:
                                    copy = list(
                                        linia_active[:linia_active.index(node_contacts[num_nodes_contacts][0]) + 1])

                                    copy_time = list(
                                        linia_active_t[:linia_active.index(node_contacts[num_nodes_contacts][0])])
                                    copy.extend([node_contacts[num_nodes_contacts][1]])
                                    copy_time.extend([node_contacts[num_nodes_contacts][2]])
                                    to_copy_list.append(copy)
                                    to_copy_list_time.append(copy_time)
                                    copy_i = 1
                                    del copy
                                    del copy_time
                                    continue
                                else:
                                    nowe = [node_contacts[num_nodes_contacts][0], node_contacts[num_nodes_contacts][1]]
                                    nowe_time = [node_contacts[num_nodes_contacts][2]]
                                    to_copy_list_nowe.append(nowe)
                                    to_copy_list_nowe_time.append(nowe_time)
                                    nowe_i = 1

                                    del nowe
                                    del nowe_time
                                    continue

                        else:
                            id_0 = linia_active.index(node_contacts[num_nodes_contacts][0])

                            copy = list(linia_active[:linia_active.index(node_contacts[num_nodes_contacts][0]) + 1])

                            copy_time = list(linia_active_t[:linia_active.index(node_contacts[num_nodes_contacts][0])])
                            copy.extend([node_contacts[num_nodes_contacts][1]])
                            copy_time.extend([node_contacts[num_nodes_contacts][2]])
                            to_copy_list.append(copy)
                            to_copy_list_time.append(copy_time)
                            copy_i = 1
                            del copy
                            del copy_time
                            continue

                    else:
                        nowe = [node_contacts[num_nodes_contacts][0], node_contacts[num_nodes_contacts][1]]
                        nowe_time = [node_contacts[num_nodes_contacts][2]]
                        to_copy_list_nowe.append(nowe)
                        to_copy_list_nowe_time.append(nowe_time)
                        nowe_i = 1

                        del nowe
                        del nowe_time
                        continue
                # print(to_see_list)
                to_see_list = list(active_nodes_list)
                to_see_list_time = list(active_nodes_list_time)

                identico_i = 1
                if identico_i != 0:

                    if copy_i != 0:

                        for ii in range(len(to_copy_list)):
                            line_copy = list(to_copy_list[ii])
                            line_copy_t = list(to_copy_list_time[ii])

                            identic = 0

                            for jj in range(len(to_see_list)):
                                line_identic = list(to_see_list[jj])
                                count_id = 0
                                # print(str(ii)+"lllll"+str(jj))
                                for kk in range(len(line_copy)):

                                    if line_copy[kk] in line_identic:
                                        if line_copy.index(line_copy[kk]) == line_identic.index(line_copy[kk]):
                                            count_id += 1
                                        else:
                                            break
                                    else:
                                        break
                                if count_id == len(line_copy):
                                    identic += 1

                            if identic == 0:
                                # print(line_copy)
                                new_to_copy_list.append(line_copy)
                                new_to_copy_list_time.append(line_copy_t)
                        delete_nodes_list(to_copy_list)
                        delete_nodes_list(to_copy_list_time)
                        to_copy_list = list(new_to_copy_list)
                        to_copy_list_time = list(new_to_copy_list_time)
                        delete_nodes_list(new_to_copy_list)
                        delete_nodes_list(new_to_copy_list_time)

                    if nowe_i != 0:

                        for ii in range(0, len(to_copy_list_nowe)):

                            line_nowe = list(to_copy_list_nowe[ii])
                            line_nowe_t = list(to_copy_list_nowe_time[ii])
                            identic = 0
                            for jj in range(0, len(to_see_list)):
                                line_identic = list(to_see_list[jj])
                                count_idn = 0

                                for kk in range(len(line_nowe)):

                                    if line_nowe[kk] in line_identic:
                                        if line_nowe.index(line_nowe[kk]) == line_identic.index(line_nowe[kk]):
                                            count_idn += 1
                                        else:
                                            break
                                    else:
                                        break
                                # print(str(count_idn)+" "+str(len(line_identic))+"lll")
                                # print(str(line_nowe)+" "+str(len(line_nowe)))
                                if count_idn == len(line_nowe):
                                    identic += 1
                            if identic == 0:
                                new_to_copy_list_nowe.append(line_nowe)
                                new_to_copy_list_nowe_time.append(line_nowe_t)

                        delete_nodes_list(to_copy_list_nowe)
                        delete_nodes_list(to_copy_list_nowe_time)
                        to_copy_list_nowe = list(new_to_copy_list_nowe)
                        to_copy_list_nowe_time = list(new_to_copy_list_nowe_time)
                        delete_nodes_list(new_to_copy_list_nowe)
                        delete_nodes_list(new_to_copy_list_nowe_time)

                if copy_i != 0:
                    if len(to_copy_list) > 1:
                        for ii in range(len(to_copy_list)):
                            line_copy = list(to_copy_list[ii])
                            line_copy_t = list(to_copy_list_time[ii])
                            identic = 0
                            if len(to_copy_list) != 1:
                                for jj in range(ii + 1, len(to_copy_list)):
                                    count_id = 0
                                    line_copy2 = list(to_copy_list[jj])
                                    for kk in range(len(line_copy)):
                                        if line_copy[kk] in line_copy2:
                                            if line_copy.index(line_copy[kk]) == line_copy2.index(line_copy[kk]):
                                                count_id += 1
                                            else:
                                                break
                                        else:
                                            break
                                    if count_id == len(line_copy):
                                        identic += 1
                                if identic == 0:
                                    new_to_copy_list.append(line_copy)
                                    new_to_copy_list_time.append(line_copy_t)

                        delete_nodes_list(to_copy_list)
                        delete_nodes_list(to_copy_list_time)
                        to_copy_list = list(new_to_copy_list)
                        to_copy_list_time = list(new_to_copy_list_time)
                        delete_nodes_list(new_to_copy_list)
                        delete_nodes_list(new_to_copy_list_time)


                else:
                    if len(to_copy_list_nowe) > 1:
                        # print(str(to_copy_list_nowe)+"oooooo")
                        for ii in range(len(to_copy_list_nowe)):
                            line_nowe = list(to_copy_list_nowe[ii])
                            line_nowe_t = list(to_copy_list_nowe_time[ii])
                            identic = 0
                            for jj in range(ii + 1, len(to_copy_list_nowe)):
                                line_nowe2 = list(to_copy_list_nowe[jj])

                                count_id = 0
                                for kk in range(len(line_nowe)):

                                    if line_nowe[kk] in line_nowe2:
                                        if line_nowe.index(line_nowe[kk]) == line_nowe2.index(line_nowe[kk]):
                                            count_id += 1
                                        else:

                                            break
                                    else:
                                        break

                                if count_id == len(line_nowe):
                                    identic += 1
                            if identic == 0:
                                new_to_copy_list_nowe.append(line_nowe)
                                new_to_copy_list_nowe_time.append(line_nowe_t)

                        delete_nodes_list(to_copy_list_nowe)
                        delete_nodes_list(to_copy_list_nowe_time)

                        to_copy_list_nowe = list(new_to_copy_list_nowe)
                        to_copy_list_nowe_time = list(new_to_copy_list_nowe_time)
                        delete_nodes_list(new_to_copy_list_nowe)
                        delete_nodes_list(new_to_copy_list_nowe_time)

            if len(to_copy_list) != 0:
                active_nodes_list.extend(to_copy_list)
                active_nodes_list_time.extend(to_copy_list_time)

                delete_nodes_list(to_copy_list)
                delete_nodes_list(to_copy_list_time)

            else:

                # print(str(to_copy_list_nowe) + "   ppp")
                active_nodes_list.extend(to_copy_list_nowe)
                active_nodes_list_time.extend(to_copy_list_nowe_time)

                delete_nodes_list(to_copy_list_nowe)
                delete_nodes_list(to_copy_list_nowe_time)
            # print(active_nodes_list)
            # print(active_nodes_list_time)
            num_nodes_contacts += 1

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

                    if time_diff < D[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ]:
                        Di[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ] += 1
                        nodes_number[int(active_nodes_list[y][xx]) ][1] += 1
                        nodes_number[int(active_nodes_list[y][xxx]) ][1] += 1
                        D[int(active_nodes_list[y][xx]) ][int(active_nodes_list[y][xxx]) ] = time_diff

        for i in range(0, len(t.nodes)):
            distance[i] = 0
        dist_all = 0
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
plik=open(nazwa+ "_data", "r")

line=plik.readlines()
line[1] = line[1].split('\t')
line[4]= line[4].split('\t')
line[5]= line[5].split('\t')
line[6]= line[6].split('\t')
line[7]= line[7].split('\t')
line[8]= line[8].split('\t')

#print(line[1][5])
e_przed=line[1][5]
for i in range(0, len(t.nodes)):
    nodes_number.append([i, 0])
    efficiency.append([i, 0])
    bet_nodes2.append([i, 0])
    bet_nodes3.append([i,0])
    average_num.append([i, 0])
    bet_nodes.append([i, 0])
    inst_con.append([i, 0])
    distance.append(0)
    time_alive.append([i, 0, 0, 0])
numerek = 0
for ii in range(4, 9):
    bet_nodes[numerek][1] = float(line[ii][3])
    numerek += 1
eff=[]
for ii in range(len(bet_nodes)):
    eff.append(bet_nodes[ii][1])
eff.sort()
print (bet_nodes)
print(eff)

for jj in range(len(eff)):
    for iii in range(len(bet_nodes)):
        if bet_nodes[iii][1]==eff[jj]:
            bet_nodes2[jj][0]=bet_nodes[iii][0]
            bet_nodes2[jj][1]=eff[jj]
            del bet_nodes[iii]
            break
for jj in range(len(bet_nodes2)):
    if len(bet_nodes2)!=len(bet_nodes3):
        bet_nodes3.append([0,0])
    else:
        bet_nodes3[jj][0]=bet_nodes2[jj][0]
        bet_nodes3[jj][1] = bet_nodes2[jj][1]

for r_p in range(2,11):
    print("atack betweenness node" + " " + str(float(r_p / 10.0)))
    node_contacts=[]
    #print (node_contacts)
    node_contacts = list_of_contacts()
    time_table(time_table_val, time_table_nr, node_contacts)
    node_id_rm(node_contacts)
    Di = np.zeros((len(t.nodes), len(t.nodes)))
    B = np.zeros((len(t.nodes), len(t.nodes)))
    D = np.zeros((len(t.nodes), len(t.nodes)))
    C = np.zeros((len(t.nodes), len(t.nodes)))
    D_id = np.zeros((len(t.nodes), len(t.nodes)))
    a = np.zeros((len(t.nodes), len(t.nodes)))
    new_node_contacts = []
    active_nodes_list1 = []
    active_nodes_list_time1 = []

    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            D[v][w] = 300
    if len(bet_nodes3)!=0:
        for c in range(0, len(node_contacts)):

            if (int(node_contacts[c][0]) == int(bet_nodes3[len(bet_nodes3) - 1][0]) or int(
                    node_contacts[c][1]) == int(bet_nodes3[len(bet_nodes3) - 1][0])):
                print("lol")

            else:
                new_node_contacts.append(node_contacts[c])
        del bet_nodes3[len(bet_nodes3) - 1]

        time_table(time_table_val, time_table_nr, new_node_contacts)
        e_po = distance_count2(len(bet_nodes3), new_node_contacts, active_nodes_list1, active_nodes_list_time1)

        delete_nodes_list(node_contacts)
        delete_nodes_list(new_node_contacts)
    else:
        e_po = 0
        print("E_po" + str(e_po))
        print(D)
    plik2 = open(nazwa + "_attack", 'a')
    plik2.write(
        "rozd" + '\t' + "P" + '\t' + "nodes" + '\t' + "time" + '\t' + "Eprzed" + '\t' + "E po" + '\t' + "R")
    plik2.write('\n')
    plik2.write("n" + '\t' + str(r_p) + '\t' + str(len(t.nodes)) + '\t'
                + str(t.getObservationLength()) + '\t' + str(e_przed) + '\t' + str(e_po) + '\t' + str(
        float(e_po) / float(e_przed)))
    plik2.write('\n')