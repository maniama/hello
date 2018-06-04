import pyTempNet as tn
import igraph
import numpy as np
import matplotlib.pyplot as plt
import sys
from IPython.display import *
from IPython.display import HTML
import base64
import plotly.graph_objs as go
from wand.image import Image
import plotly.plotly as py
import time as ti
import datetime
from subprocess import call
from plotly import tools
from decimal import Decimal
import plotly.graph_objs as go
import random
import matplotlib

plt.switch_backend('agg')
# matplotlib.use('Agg')
# import plotly.figure_factory as ff
# tools.set_credentials_file(username='maniama', api_key='qiLX2oVUhZgnWOTX6nOV')
import matplotlib.pyplot as pl

# usuwanie elementow macierzy kontaktow
def delete_nodes_list(nodes):
    for n in range(0, len(nodes)):
        nodes.remove(nodes[0])


def list_of_contacts():
    node_contacts=[]


    for i in range(0,len(t.tedges)):
        nodes = []
        for ii in range(0, 3):
            nodes.append(0)
        for j in range(0,3):
            nodes[j]=t.tedges[i][j]
        node_contacts.append(nodes)

    return node_contacts

# utworzenie macierzy polaczen miedzy kontaktami; A i C
# aktywnosc ukladu w czasie, w jednostce czasowej A_sum
def adj2(time_table_val, time_table_nr, a, C, A, A_sum, Nodes_edges, list, node_contacts):
    n = 0
    found = 0
    A_test = np.zeros((len(t.nodes), len(t.nodes)))
    time_table(time_table_val, time_table_nr,node_contacts)

    for i in range(0, len(time_table_val)):
        A.append(A_test)
        A_sum.append(np.zeros(len(t.nodes)))
    for x in range(0, len(time_table_val)):
        #print(n)
        to = time_table_val[x]
        nr = time_table_nr[x]

        for k in range(nr, len(node_contacts)):  # dla danego czasu podawany indeks do tedges

            if node_contacts[k][2] == to:

                for counter in range(0, len(t.nodes)):

                    if node_contacts[k][0] == t.nodes[counter]:
                        v = counter
                        found = found + 1
                    if node_contacts[k][1] == t.nodes[counter]:
                        w = counter
                        found = found + 1

                    if found == 2:
                        a[v][w] += 1.0
                        a[w][v] += 1.0
                        list.append([v, w, x])
                        found = 0

        C += a
        A[x] = a
        a = np.zeros((len(t.nodes), len(t.nodes)))

        n = n + 1
        name = 'A' + str(x)

    print("adj2 done")

# plik = open('example', 'w')
# tworzy tabelke wszystkich czasow podczas eksperymentu
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
    print("table_table done")


def wykresy(tab_time, Av_node, Nr_con_no):
    print("logxlog")
    counts, bins, bars = pl.hist(Av_node, len(Av_node) // 2, density=1, facecolor='blue', alpha=0.5)

    bins2 = []
    pl.cla()
    for i in range(0, len(bins) - 1):
        bins2.append((len(Av_node) // 2) * i)
    fig = pl.plot(bins2, counts, 'ro')
    pl.title('logxlog')
    pl.xlabel("log(k)")
    pl.ylabel("log(P)")
    pl.savefig("logxlog_" + nazwa + ".png")
    pl.cla()

    print("rozklad stopni wierzcholkow")
    fig = pl.hist(Av_node, len(Av_node) // 2, density=1, facecolor='blue', alpha=0.5)
    pl.title('rozklad stopni wierzcholkow')
    pl.xlabel("k")
    pl.ylabel("P")
    pl.savefig("rozklad_s_w_" + nazwa + ".png")
    pl.cla()

    print("aktywnosc nodow w ukladzie")
    fig = pl.bar(range(0, len(t.nodes)), Av_node)
    pl.axis([0, len(t.nodes) + 1, 0, max(Av_node) + 1])
    pl.title('aktywnosc nodow w ukladzie')
    pl.xlabel("nodes")
    pl.ylabel("liczba polaczen")

    pl.savefig("aktywnosc_n_" + nazwa + ".png")
    pl.cla()

    print("histogram czasu wystepowania wezla w ukladzie")
    fig = pl.hist(tab_time, len(tab_time) // 2, density=1, facecolor='blue', alpha=0.5)
    pl.title('histogram czasu wystepowania wezla w ukladzie')
    pl.xlabel("t")
    pl.ylabel("P")
    pl.savefig("hist_czas_" + nazwa + ".png")
    pl.cla()

    print("histogram l. kontaktow")
    fig = pl.hist(Nr_con_no, len(Nr_con_no) // 2, density=1, facecolor='blue', alpha=0.5)
    pl.title('histogram l. kontaktow')
    pl.xlabel("con")
    pl.ylabel("P")
    pl.savefig("hist_l_k_" + nazwa + ".png")
    pl.cla()


# najkrotsza droga
def shortest_distance_2(list,Di):
    active_nodes_list = []
    nowe_active = []
    new_time_con = []
    nodes = []
    time_cc = []
    contacts = []
    time_con = []
    for v in range(0, len(t.nodes)):
        start = v

        #print(start)
        delete_nodes_list(nodes)
        search_start_con(start, nodes, list)

        delete_nodes_list(active_nodes_list)
        delete_nodes_list(time_con)
        delete_nodes_list(time_cc)

        for jj in range(0, len(nodes)):
            create_list(active_nodes_list, nodes, start, jj, time_con)

        for w in range(0, numero):
            #print("thanos")
            liczymy_polaczenia(active_nodes_list, contacts, time_con, time_cc, start, nowe_active, new_time_con,
                               list)
        check_stop(active_nodes_list, time_con, v, Di)
    print("short distance done")


def make_list(list_list, D):
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            if v != w:

                list_list.append([v, w])
            else:
                D[v][w] = 0

    print("make_list done")


def liczymy_polaczenia(active_nodes_list, contacts, time_con, time_cc, start, nowe_active, new_time_con, list):
    yes = 0
    print("elo")
    for jj in range(0, len(active_nodes_list)):

        delete_nodes_list(contacts)
        delete_nodes_list(time_cc)

        find_con(contacts, active_nodes_list[jj][len(active_nodes_list[jj]) - 1], time_con[jj][len(time_con[jj]) - 1],
                 time_cc, list)
        print("trololol")
        for jjj in range(0, len(contacts)):
            num = 0

            if contacts[jjj] in active_nodes_list[jj]:
                num += 1
            if num == 0:
                nowe_active_nodes(jjj, active_nodes_list, contacts[jjj], time_con, jj, nowe_active, new_time_con,
                                  time_cc, start)
                yes = 1
    if yes == 1:
        delete_nodes_list(active_nodes_list)
        delete_nodes_list(time_con)
        for i in range(len(nowe_active)):
            active_nodes_list.append(nowe_active[i])
        for i in range(len(new_time_con)):
            time_con.append(new_time_con[i])

        delete_nodes_list(nowe_active)
        delete_nodes_list(new_time_con)


def check_stop(active_nodes_list, time_con, v, Di):
    #print(active_nodes_list)
    for x in range(0, len(active_nodes_list)):
        for xx in range(1, len(active_nodes_list[x])):
            time_diff = abs(time_table_val[time_con[x][xx - 1]] - time_table_val[time_con[x][0]]) / 15 + 1
            #print(active_nodes_list[x])
            # print(time_con[x])
            #print(time_diff)
            if time_diff < D[active_nodes_list[x][0]][active_nodes_list[x][xx]]:
                Di[active_nodes_list[x][0]][active_nodes_list[x][xx]] += 1
                D[active_nodes_list[x][0]][active_nodes_list[x][xx]] = time_diff



def nowe_active_nodes(jjj, active_nodes_list, jum, time_con, j, nowe_active, new_time_con, time_cc, start):
    col = active_nodes_list[j]
    col.extend([jum])
    nowe_active.append(col)
    colt = time_con[j]
    colt.extend([time_cc[jjj]])
    new_time_con.append(colt)


def list_inst(list, D):
    for xx in range(0, len(list)):
        D[list[xx][0]][list[xx][1]] = 1
        D[list[xx][1]][list[xx][0]] = 1
    print("list_inst done")


# (funkcja do wyszukiwania wszystkich sasiadow od wyznaczonego miejsca)
def find_con(contacts, next, j, time_cc, list):
    y = 0
    print(str(j)+"looloooooooo")
    for xx in range(0, len(list)):
        if list[xx][2] == j:
            y = xx

    for x in range(y, len(list)):

        if list[x][1] == next:
            contacts.extend([list[x][0]])
            time_cc.extend([list[x][2]])
        if list[x][0] == next:
            contacts.extend([list[x][1]])
            time_cc.extend([list[x][2]])


# wyszukuje wszystkie polaczenia start - jezeli nie ma to koniec
def search_start_con(start, nodes, list):
    for x in range(0, len(list)):

        if list[x][1] == start:

            nodes.append([list[x][2], list[x][0]])

        elif list[x][0] == start:
            nodes.append([list[x][2], list[x][1]])



# utworzenie listy
def create_list(active_nodes_list, nodes, start, jj, time_con):
    active_nodes_list.append([start, nodes[jj][1]])
    time_con.append([nodes[jj][0]])


# odczytuje najkrotszy dystans miedzy kontaktami i liczy efficiency
def distance_read(D,eff_list):
    dist=0
    dist_node=0
    #np.savetxt("distance_" + nazwa + str(numero) + "_" + str(attack), D, delimiter=",")
    for v in range(0, len(t.nodes)):
        for w in range(0, len(t.nodes)):
            if (v != w):
                dist_node=0
                if D[v][w] == 300:
                    dist += 0
                    dist_node+=0
                else:
                    dist += (1.0 / D[v][w])
                    dist_node += (1.0 / D[v][w])
        eff_list.append(dist_node)
    print("dist" + " " + str(dist) + " " + "/" + " " + str(len(t.nodes)) + " " + "*" + " " + str(len(t.nodes) - 1))
    rel_eff = dist / (len(t.nodes) * (len(t.nodes) - 1))

    print("distance_read done")

    print("relative efficiency")
    print('% .4f' % rel_eff)


    return rel_eff

# sredni stopien wezla - rozklad
def nr_con_node(C):
    lol = 0
    nr_con_n =0
    nr_con_t=0
    for v in range(0, len(t.nodes)):
        nr = 0

        suma = 0

        for w in range(v, len(t.nodes)):
            nr += C[v][w]
            if C[v][w] != 0:
                lol += 1
        suma += nr
        nr_con_n += (suma / len(t.nodes))
        nr_con_t += (suma / 20)
        Nr_con_no.append(nr_con_n)
        #print(lol)
    nr_con_n = (nr_con_n / len(t.nodes))
    nr_con_t = (nr_con_t / len(t.nodes))
    # print(nr_con_n)
    # print(nr_con_t)
    print("nr_con_node done")
    # print(lol/len(t.nodes))


# liczba kontaktow na wezel i na jednostke czasu, sredni wezel
def av_nr_node(C, Av_node,node_contacts):
    av_n=0
    for v in range(0, len(t.nodes)):
        nr = 0
        for w in range(v, len(t.nodes)):

            if C[v][w] != 0:
                av_n += 1
                nr += 1
        Av_node.append(nr)
    av_n = av_n / len(t.nodes)

    print("sredni stopien")
    print(av_n)
    return av_n



def time_show(tab_time,node_contacts):
    start = 0
    stop = 0
    for n in range(0, len(t.nodes)):
        for x in range(0, len(node_contacts)):
            if node_contacts[x][0] == t.nodes[n] or node_contacts[x][1] == t.nodes[n]:
                if start == 0:
                    start = node_contacts[x][2]
                    start = start - node_contacts[0][2]
                else:
                    stop = node_contacts[x][2]
                    stop = stop - node_contacts[0][2]
        if (stop - start) < 0:
            tab_time.append(float(-(stop - start)))
        else:
            tab_time.append(float(stop - start))


def miary_n(C):
    bb = 0
    bb_n = 0
    bb1 = 0
    b_n = []
    for v in range(0, len(t.nodes)):
        for w in range(v, len(t.nodes)):
            bb += C[v][w]

    for v in range(0, len(t.nodes)):

        for w in range(v, len(t.nodes)):
            bb1 += C[v][w]

        b_n.append(bb1)
        bb_n += (bb1 / bb)
        bb1 = 0

    bet_n = (2.0 / ((len(t.nodes) - 1.0) * (len(t.nodes) - 2.0))) * bb_n
    print('% .4f' % bet_n)
    return bet_n

def miary_e(C):
    bb = 0
    bb_e = 0
    b_e = np.zeros((len(t.nodes), len(t.nodes)))
    for v in range(0, len(t.nodes)):
        for w in range(v, len(t.nodes)):
            bb += C[v][w]

    for v in range(0, len(t.nodes)):

        for w in range(v, len(t.nodes)):
            bb2 = C[v][w]
            bb_e += (bb2 / bb)
            b_e[v][w] = bb2

    bet_e = (2.0 / (len(t.nodes) * (len(t.nodes) - 1.0))) * bb_e
    print('% .4f' % bet_e)

    return bet_e

def liczenie(node_contacts):
    adj2(time_table_val, time_table_nr, a, C, A, A_sum, Node_edges, list,node_contacts)
    make_list(list_list, D)
    shortest_distance_2(list, Di)
    list_inst(list, D)

    nr_con_node(C)
    av_nr_node(C,Av_node,node_contacts)
    time_show(tab_time,node_contacts)
    print(D)
    #wykresy(tab_time, Av_node, Nr_con_no)

def random_attack(node_contacts,r_num):
    new_node_contacts=[]
    for i in range(0, r_num):
        ran_num=(random.randint(0, len(t.nodes)))
        #print(str(ran_num)+"lololo")
        for c in range(0, len(node_contacts)):

            if (int(node_contacts[c][0]) ==ran_num or int(node_contacts[c][1]) == ran_num):
                print("lol")
            else:
                new_node_contacts.append(node_contacts[c])
        #print(new_node_contacts)
    return new_node_contacts

def most_eff(node_contacts,f_num,eff_list):

    for i in range(0, f_num):
        new_node_contacts = []
        for ii in range(0,len(eff_list)):
            max_eff=eff_list[0]
            if eff_list[ii]>max_eff:
                max_eff=eff_list[i]
        eff_list[eff_list.index(max_eff)]=0
        for c in range(0, len(node_contacts)):
                if (int(node_contacts[c][0]) == max_eff or int(node_contacts[c][1] )== max_eff):
                    print("lol")
                else:
                    new_node_contacts.append(node_contacts[c])
    return new_node_contacts


def most_contact_attack_e(Di,node_contacts,e_num):
    e_list=[]
    for v in range(0,len(t.nodes)):
        e_node=0
        for w in range(0,len(t.nodes)):
            e_node+=Di[v][w]
        e_list.append(e_node)
    for i in range(0, e_num):
        new_node_contacts = []
        for ii in range(0, len(e_list)):
            max_e = e_list[0]
            if e_list[ii] > max_e:
                max_e = e_list[i]
        e_list[e_list.index(max_e)] = 0
        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == max_e or int(node_contacts[c][1]) == max_e):
                print("lol")
            else:
                new_node_contacts.append(node_contacts[c])
    return new_node_contacts


def most_contact_attack_i(Di,node_contacts,n_num):
    new_node_contacts = []
    for i in range(0, n_num):
        for ii in range(0, len(t.nodes)):
            for jj in range(0,len(t.nodes)):
                max_n = Di[0][0]
                if Di[ii][jj] > max_n:
                    max_n = Di[ii][jj]
                    ii_n=ii
                    jj_n=jj
        D[ii_n][jj_n]=0
        for c in range(0, len(node_contacts)):
            if (int(node_contacts[c][0]) == max_n or int(node_contacts[c][1]) == max_n):
                print("lol")
            else:
                new_node_contacts.append(node_contacts[c])
    return new_node_contacts

def attack(r, r_num, f, f_num, e, e_num, n, n_num,node_contacts):
        if r==1:
            #print(node_contacts)
            #print(random_attack(node_contacts,r_num))
            liczenie(random_attack(node_contacts,r_num))
            plik2.write('\n' + nazwa +"r"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
        if f==1:
            liczenie(most_eff(node_contacts,f_num,eff_list))
            plik2.write('\n' + nazwa +"f"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
        if e==1:
            liczenie(most_contact_attack_e(Di,node_contacts,e_num))
            plik2.write('\n' + nazwa +"e"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
        if n==1:
            liczenie(most_contact_attack_i(Di,node_contacts,n_num))
            plik2.write('\n' + nazwa +"n"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))



time_table_val = []
time_table_nr = []
tab_time = []
Av_node = []
Nr_con_no = []
ak = []
A = []
list_list = []
Node_edges = []
A_sum = []
list = []
eff_list=[]
print("Temporal network robustness")
print("c -  choose your own ")
print("ff - file mode")
mode = raw_input("Choose mode or customise")
if mode == "ff":
    with open("/home/marta/mode","r") as f:
        for line in f:
            data = line.split("\t")

            nazwa = data[0]
            numero = (int(data[1]))
            delta = (int(data[2]))
            r = (int(data[3]))
            r_num = (int(data[4]))
            f = (int(data[5]))
            f_num = (int(data[6]))
            e = (int(data[7]))
            e_num = (int(data[8]))
            n = (int(data[9]))
            n_num = (int(data[10]))

            t = tn.readFile('/home/marta/Downloads/'+nazwa+'_network.tedges', sep=" ", fformat="TEDGE", timestampformat="%s",
                    maxlines=sys.maxsize)
            # t = tn.readFile('06_05.tedges', sep=" " ,fformat = "TEDGE", timestampformat="%s", maxlines=sys.maxsize)
            t.setMaxTimeDiff(int(delta))
            t.nodes.sort()
            Di = np.zeros((len(t.nodes), len(t.nodes)))
            B = np.zeros((len(t.nodes), len(t.nodes)))
            D = np.zeros((len(t.nodes), len(t.nodes)))
            C = np.zeros((len(t.nodes), len(t.nodes)))

            a = np.zeros((len(t.nodes), len(t.nodes)))

            for v in range(0, len(t.nodes)):
                for w in range(0, len(t.nodes)):
                    D[v][w] = 300

            plik2 = open(nazwa + "_wyniki" + str(numero), 'a')
            node_contacts = list_of_contacts()
            liczenie(node_contacts)
            plik2.write('\n' + nazwa +"0"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
            attack(r, r_num, f, f_num, e, e_num, n, n_num, node_contacts)

elif mode == "c":
    y_n = raw_input("Attacks (y) or not (n)?")
    if y_n == 'y':

        r = raw_input("Random attack y/n? ")
        r_num = raw_input("Number of nodes to delete? ")
        f = raw_input("Effectivness attack y/n?")
        f_num = raw_input("Number of nodes to delete? ")
        e = raw_input("Betweeness edge y/n? ")
        e_num = raw_input("Number of edges to delete? ")
        n = raw_input("Betweeness node y/n? ")
        n_num = raw_input("Number of nodes to delete? ")

        nazwa = input("Choose  file")
        numero = input("Choose thanos ")
        delta = input("Choose delta t ")
        t = tn.readFile(nazwa, sep=" ", fformat="TEDGE", timestampformat="%s",
                        maxlines=sys.maxsize)
        # t = tn.readFile('06_05.tedges', sep=" " ,fformat = "TEDGE", timestampformat="%s", maxlines=sys.maxsize)
        t.setMaxTimeDiff(int(delta))
        t.nodes.sort()
        Di = np.zeros((len(t.nodes), len(t.nodes)))
        B = np.zeros((len(t.nodes), len(t.nodes)))
        D = np.zeros((len(t.nodes), len(t.nodes)))
        C = np.zeros((len(t.nodes), len(t.nodes)))

        a = np.zeros((len(t.nodes), len(t.nodes)))

        for v in range(0, len(t.nodes)):
            for w in range(0, len(t.nodes)):
                D[v][w] = 300

        plik2 = open(nazwa + "_wyniki" + str(numero), 'a')
        node_contacts=list_of_contacts()
        liczenie(node_contacts)

        plik2.write('\n' + nazwa + "0" + '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                    str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
            av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
            '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
        attack(r, r_num, f, f_num, e, e_num, n, n_num,node_contacts)

    elif y_n == 'n':
        #nazwa = input("Choose  file")
        #numero = input("Choose thanos ")
        #delta = input("Choose delta t ")
        nazwa2 = '/home/marta/Downloads/example_network.tedges'
        nazwa="example"
        numero=2
        delta=15
        r=0
        f=0
        e=0
        n=0
        t = tn.readFile(nazwa2, sep=" ", fformat="TEDGE", timestampformat="%s",
                        maxlines=sys.maxsize)
        # t = tn.readFile('06_05.tedges', sep=" " ,fformat = "TEDGE", timestampformat="%s", maxlines=sys.maxsize)
        t.setMaxTimeDiff(int(delta))
        t.nodes.sort()
        Di = np.zeros((len(t.nodes), len(t.nodes)))
        B = np.zeros((len(t.nodes), len(t.nodes)))
        D = np.zeros((len(t.nodes), len(t.nodes)))
        C = np.zeros((len(t.nodes), len(t.nodes)))

        a = np.zeros((len(t.nodes), len(t.nodes)))

        for v in range(0, len(t.nodes)):
            for w in range(0, len(t.nodes)):
                D[v][w] = 300

        plik2 = open(nazwa + "_wyniki" +  str(numero), 'a')
        node_contacts=list_of_contacts()
        liczenie(node_contacts)

        plik2.write('\n' + nazwa +"0"+ '\t' + str(len(t.nodes)) + '\t' + str(len(node_contacts)) + '\t' +
                        str(t.getObservationLength()) + '\t' + str(15) + '\t' + str(len(time_table_val)) + '\t' + str(
                av_nr_node(C, Av_node, node_contacts)) + '\t' + str('% .4f' % distance_read(D,eff_list)) + '\t' + str(
                '% .4f' % miary_n(C)) + '\t' + str('% .4f' % miary_e(C)))
        print(D)

plik2.close()
