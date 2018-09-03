

import pyTempNet as tn
import numpy as np
import matplotlib.pyplot as plt
import sys

import matplotlib.pyplot as pl
plt.switch_backend('agg')
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
def distance_count():
    to_see_list=[]
    to_see_list_time=[]
    to_copy_list_nowe=[]
    to_copy_list_nowe_time=[]
    global_eff=0
    ideal_gl_eff=0
    all_nodes_number=0
    to_copy_list=[]
    to_dodac_list=[]
    to_copy_list_time=[]
    to_dodac_list_time=[]
    nr_con=0
    num_con=0
    time_table_val_num=[]
    for i in range(0, len(t.nodes)):
        distance[i] = 0.0
    dist_all = 0.0
    for ii in range(len(time_table_val)):
        if ii==len(time_table_val)-1:
            time_table_val_num.append([time_table_val[ii], len(node_contacts)-time_table_nr[ii]])
        else:
            time_table_val_num.append([time_table_val[ii],time_table_nr[ii+1]-time_table_nr[ii]])
    print(time_table_val_num)

    for tt in range(0, len(time_table_val_num)):

        num_nodes_contacts = time_table_nr[tt]
        print(time_table_val[tt])

        for ttt in range(0,time_table_val_num[tt][1]):


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
                num_ac=[]
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
                    new_nr_ac=[]

                    linia_active = list(active_nodes_list[r])
                    linia_active_t = list(active_nodes_list_time[r])


                    if node_contacts[num_nodes_contacts][0] in linia_active:
                        if node_contacts[num_nodes_contacts][1] in linia_active:
                            id_0=linia_active.index(node_contacts[num_nodes_contacts][0])
                            id_1=linia_active.index(node_contacts[num_nodes_contacts][1])
                            if id_0+1!=id_1:
                                if id_0<id_1:
                                    copy = list(linia_active[:linia_active.index(node_contacts[num_nodes_contacts][0]) + 1])

                                    copy_time = list(linia_active_t[:linia_active.index(node_contacts[num_nodes_contacts][0])])
                                    copy.extend([node_contacts[num_nodes_contacts][1]])
                                    copy_time.extend([node_contacts[num_nodes_contacts][2]])
                                    to_copy_list.append(copy)
                                    to_copy_list_time.append(copy_time)
                                    copy_i=1
                                    del copy
                                    del copy_time
                                    continue
                                else:
                                    nowe = [node_contacts[num_nodes_contacts][0], node_contacts[num_nodes_contacts][1]]
                                    nowe_time = [node_contacts[num_nodes_contacts][2]]
                                    to_copy_list_nowe.append(nowe)
                                    to_copy_list_nowe_time.append(nowe_time)
                                    nowe_i=1

                                    del nowe
                                    del nowe_time
                                    continue

                        else:
                            id_0=linia_active.index(node_contacts[num_nodes_contacts][0])

                            copy = list(linia_active[:linia_active.index(node_contacts[num_nodes_contacts][0]) + 1])

                            copy_time = list(linia_active_t[:linia_active.index(node_contacts[num_nodes_contacts][0])])
                            copy.extend([node_contacts[num_nodes_contacts][1]])
                            copy_time.extend([node_contacts[num_nodes_contacts][2]])
                            to_copy_list.append(copy)
                            to_copy_list_time.append(copy_time)
                            copy_i=1
                            del copy
                            del copy_time
                            continue

                    else:
                        nowe = [node_contacts[num_nodes_contacts][0], node_contacts[num_nodes_contacts][1]]
                        nowe_time = [node_contacts[num_nodes_contacts][2]]
                        to_copy_list_nowe.append(nowe)
                        to_copy_list_nowe_time.append(nowe_time)
                        nowe_i=1

                        del nowe
                        del nowe_time
                        continue
                #print(to_see_list)
                to_see_list=list(active_nodes_list)
                to_see_list_time=list(active_nodes_list_time)

                identico_i=1
                if identico_i!=0:

                    if copy_i!=0:

                        for ii in range(len(to_copy_list)):
                            line_copy = list(to_copy_list[ii])
                            line_copy_t = list(to_copy_list_time[ii])

                            identic=0

                            for jj in range(len(to_see_list)):
                                line_identic = list(to_see_list[jj])
                                count_id=0
                                #print(str(ii)+"lllll"+str(jj))
                                for kk in range(len(line_copy)):

                                    if line_copy[kk] in line_identic:
                                        if line_copy.index(line_copy[kk])==line_identic.index(line_copy[kk]):
                                            count_id+=1
                                        else:
                                            break
                                    else:
                                        break
                                if count_id ==len(line_copy):
                                    identic+=1


                            if identic==0:
                                #print(line_copy)
                                new_to_copy_list.append(line_copy)
                                new_to_copy_list_time.append(line_copy_t)
                        delete_nodes_list( to_copy_list)
                        delete_nodes_list( to_copy_list_time)
                        to_copy_list=list(new_to_copy_list)
                        to_copy_list_time = list(new_to_copy_list_time)
                        delete_nodes_list(new_to_copy_list)
                        delete_nodes_list(new_to_copy_list_time)

                    if nowe_i!=0:

                        for ii in range(0,len(to_copy_list_nowe)):

                            line_nowe = list(to_copy_list_nowe[ii])
                            line_nowe_t = list(to_copy_list_nowe_time[ii])
                            identic=0
                            for jj in range(0,len(to_see_list)):
                                line_identic = list(to_see_list[jj])
                                count_idn=0

                                for kk in range(len(line_nowe)):

                                    if line_nowe[kk] in line_identic:
                                        if line_nowe.index(line_nowe[kk])==line_identic.index(line_nowe[kk]):
                                            count_idn+=1
                                        else:
                                            break
                                    else:
                                        break
                                #print(str(count_idn)+" "+str(len(line_identic))+"lll")
                                #print(str(line_nowe)+" "+str(len(line_nowe)))
                                if count_idn==len(line_nowe):
                                    identic+=1
                            if identic==0:

                                new_to_copy_list_nowe.append(line_nowe)
                                new_to_copy_list_nowe_time.append(line_nowe_t)

                        delete_nodes_list( to_copy_list_nowe)
                        delete_nodes_list( to_copy_list_nowe_time)
                        to_copy_list_nowe=list(new_to_copy_list_nowe)
                        to_copy_list_nowe_time = list(new_to_copy_list_nowe_time)
                        delete_nodes_list(new_to_copy_list_nowe)
                        delete_nodes_list(new_to_copy_list_nowe_time)

                if copy_i!=0:
                    if len(to_copy_list)>1:
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
                    if len(to_copy_list_nowe)>1:
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
        print(str(active_nodes_list)+" lll")
        for y in range(0, len(active_nodes_list)):

            for xx in range(0, len(active_nodes_list[y])):
                for xxx in range(xx+1, len(active_nodes_list[y])):

                    time_zero = xx
                    time = xxx-1
                    #print(y)

                    #print (active_nodes_list_time)
                    #print(str(active_nodes_list[y][xx])+" "+str(active_nodes_list[y][xxx]))
                    #print(str(active_nodes_list_time[y][time]) + " " + str(active_nodes_list_time[y][time_zero]))
                    if active_nodes_list_time[y][time] == active_nodes_list_time[y][time_zero]:
                        time_diff = 1
                    else:
                        time_diff = abs(active_nodes_list_time[y][time] - active_nodes_list_time[y][time_zero]) / 15

                    if time_diff < D[int(active_nodes_list[y][xx])][int(active_nodes_list[y][xxx])]:
                        Di[int(active_nodes_list[y][xx])][int(active_nodes_list[y][xxx])] += 1
                        nodes_number[int(active_nodes_list[y][xx])][1] += 1
                        nodes_number[int(active_nodes_list[y][xxx])][1] += 1
                        D[int(active_nodes_list[y][xx])][int(active_nodes_list[y][xxx])] = time_diff
                    #print("helo")
        for i in range(0, len(t.nodes)):
            distance[i] = 0
        dist_all = 0
        for ii in range(0, len(t.nodes)):
            for jj in range(0, len(t.nodes)):
                if D[ii][jj] == 300 or D[ii][jj] == 0:
                    distance[ii] += 0.0
                else:
                    distance[ii] += 1.0 / D[ii][jj]
            print(distance[ii])
            dist_all += distance[ii]
        global_eff += float(1.0 / (len(t.nodes) * (len(t.nodes) - 1)) * dist_all)


    for ii in range(0, len(t.nodes)):
        print(ii)
        print(distance[ii])
        all_nodes_number += nodes_number[ii][1]
        time_alive[ii][3] = abs(time_alive[ii][1] - time_alive[ii][2])
        efficiency[ii][1]='% .4f' % float(1.0 / len(time_table_val) * float(distance[ii]))
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

t = tn.readFile( 'example_network.tedges', sep=" ", fformat="TEDGE",
                        timestampformat="%s",
                        maxlines=sys.maxsize)
t.setMaxTimeDiff(20)
nazwa="example2"
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


