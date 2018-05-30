
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
matplotlib.use('Agg')
#import plotly.figure_factory as ff
#tools.set_credentials_file(username='maniama', api_key='qiLX2oVUhZgnWOTX6nOV')
import matplotlib.pyplot as pl

#t = tn.readFile('example_network.tedges', sep=" ",fformat = "TEDGE", timestampformat="%s", maxlines=sys.maxsize)
t = tn.readFile('aaa.tedges', sep=" ",fformat = "TEDGE", timestampformat="%s", maxlines=sys.maxsize)
t.setMaxTimeDiff(20)
t.nodes.sort()
nazwa="aaa"


#utworzenie macierzy polaczen miedzy kontaktami; A i C
#aktywnosc ukladu w czasie, w jednostce czasowej A_sum
def adj2(time_table_val, time_table_nr,a,C,A,A_sum, Nodes_edges,list):
    n = 0
    found=0
    A_test=np.zeros((len(t.nodes), len(t.nodes)))
    time_table(time_table_val, time_table_nr)

    for i in range(0, len(time_table_val)):

        A.append(A_test)
        A_sum.append(np.zeros(len(t.nodes)))
    for x in range(0,len(time_table_val)):
        print(n)
        to = time_table_val[x]
        nr = time_table_nr[x]

        for k in range(nr,len(t.tedges)): # dla danego czasu podawany indeks do tedges

            if t.tedges[k][2] == to:

                for counter in range(0,len(t.nodes)):


                        if t.tedges[k][0]==t.nodes[counter]:
                            v=counter
                            found=found+1
                        if t.tedges[k][1]==t.nodes[counter]:
                            w=counter
                            found = found + 1

                        if found==2 :
                            a[v][w] += 1.0
                            a[w][v] += 1.0
                            list.append([v,w,x])
                            found = 0





        C+=a
        A[x]=a
        a = np.zeros((len(t.nodes), len(t.nodes)))

        n = n + 1
        name='A'+str(x)
        #np.savetxt(name,A[x], fmt='%.2e')
    #np.savetxt('A_sum', A_sum, fmt='%.2e')
    #np.savetxt('C', C, fmt='%.2e')
    #plik.close()
    #plik2.close()
    #plik3.close()



        #name="ad_"+str(x)+".out"
        #np.savetxt(name,a,delimiter=",")

    print("adj2 done")



plik = open(nazwa+"_wyniki", 'w')
#plik = open('example', 'w')
#tworzy tabelke wszystkich czasow podczas eksperymentu
def time_table(time_tabel_val, time_table_nr):
    to=t.tedges[0][2]
    n = 0
    time_table_val.append(to)
    time_table_nr.append(0)
    for k in range(0,len(t.tedges)): # dla danego czasu podawany indeks do tedges
        if t.tedges[k][2] != to:
            to = t.tedges[k][2]
            time_table_val.append(to)
            time_table_nr.append(k)

        n = n+1
    print("table_table done")



def wykresy(tab_time,Av_node,Nr_con_no):
    print("logxlog")
   # hist_data3 = Av_node
    # Create distplot with curve_type set to 'normal'
    # fig3 = ff.create_distplot(hist_data3, show_hist=False)
   # data = [go.Histogram(x=hist_data3,
    #                     histnorm='probability')]
    # Add title
    # fig3['layout'].update(title='roz_stopni')
    # Plot!
   # py.iplot(data, filename='roz_stopni')




    print("rozklad stopni wierzcholkow")

    # Create distplot with curve_type set to 'normal'
    #fig3 = ff.create_distplot(hist_data3, show_hist=False)

    # Add title
    #fig3['layout'].update(title='roz_stopni')
    # Plot!

    fig = pl.hist(Av_node, len(Av_node) / 2, density=1, facecolor='blue', alpha=0.5)
    pl.title('rozklad stopni wierzcholkow')
    pl.xlabel("k")
    pl.ylabel("P")
    pl.savefig("rozklad_s_w.png")


    print("aktywnosc nodow w ukladzie")
   # for x in range(0,len(time_table_val)):
    #    trace = go.Scatter(
     #       x=t.nodes,
      #      y=A_sum[x]
       # )


#        fig = tools.make_subplots(rows=1, cols=2)

 #       fig.append_trace(trace, 1, x)


  #  fig['layout'].update(height=600, width=600, title='i <3 subplots')
   # py.iplot(fig, filename='simple-subplot')
    print("histogram czasu wystepowania wezla w ukladzie")
    #hist_data =tab_time
    #print(tab_time)
    # Create distplot with curve_type set to 'normal'
    #fig = ff.create_distplot(hist_data, show_hist=False)
    #data2 = [go.Histogram(x=hist_data,
                      #   histnorm='probability')]
    # Add title
    #fig['layout'].update(title='czas_w_ukladzie')
    # Plot!

    fig = pl.hist(data2)
    fig = pl.hist(tab_time, len(tab_time) / 2, density=1, facecolor='blue', alpha=0.5)
    pl.title('histogram czasu wystepowania wezla w ukladzie')
    pl.xlabel("t")
    pl.ylabel("P")
    pl.savefig("hist_czas.png")
 

    print("histogram l. kontaktow")

    # Create distplot with curve_type set to 'normal'
    #fig2 = ff.create_distplot(hist_data2, show_hist=False)
    #data3 = [go.Histogram(x=hist_data2)]
    # Add title
    #fig2['layout'].update(title='l_kontaktow')
    # Plot!
    #py.iplot(data3, filename='l_kontaktow')

    fig = pl.hist(Nr_con_no,len(Nr_con_no)/2,density=1,facecolor='blue', alpha=0.5)
    pl.title('histogram l. kontaktow')
    pl.xlabel("con")
    pl.ylabel("P")
    pl.savefig("hist_l_k.png")
 

#najkrotsza droga
def shortest_distance_2(a,time_table_val,C,A,D,B,list,list_list,Di):

    active_nodes_list = []
    nowe_active=[]
    new_time_con=[]
    nodes = []
    is_or_not=0
    is_or_not_2 = 0
    time_cc=[]
    contacts=[]
    time_con=[]
    none_is=0
    for v in range(0,len(t.nodes)):
        start=v

        print(start)
        delete_nodes_list(nodes)
        search_start_con(start, nodes, list)

        delete_nodes_list(active_nodes_list)
        delete_nodes_list(time_con)
        delete_nodes_list(time_cc)

        for jj in range(0, len(nodes)):
            create_list(active_nodes_list,nodes,start,jj,time_con)

        for w in range(0,10):
            print("thanos")
            liczymy_polaczenia(active_nodes_list, contacts, time_con, time_cc, start, nowe_active, new_time_con,
                               list)
        check_stop(active_nodes_list,time_con,v,Di)
    print("short distance done")


def make_list(list_list,D):
    for v in range(0,len(t.nodes)):
        for w in range(0,len(t.nodes)):
            if v!=w:

                list_list.append([v,w])
            else:
                D[v][w]=0

    print("make_list done")
def liczymy_polaczenia(active_nodes_list,contacts,time_con,time_cc,start,nowe_active,new_time_con,list):
    yes=0
    for jj in range(0, len(active_nodes_list)):

        delete_nodes_list(contacts)
        delete_nodes_list(time_cc)

        find_con(contacts, active_nodes_list[jj][len(active_nodes_list[jj])-1], time_con[jj][len(time_con[jj])-2], time_cc, list)

        for jjj in range(0, len(contacts)):
            num=0

            if contacts[jjj] in active_nodes_list[jj]:
                num+=1
            if num==0:

                nowe_active_nodes(jjj,active_nodes_list, contacts[jjj], time_con,jj,nowe_active,new_time_con,time_cc,start)
                yes=1
    if yes==1:
        delete_nodes_list(active_nodes_list)
        delete_nodes_list(time_con)
        for i in range(len(nowe_active)):
            active_nodes_list.append(nowe_active[i])
        for i in range(len(new_time_con)):
            time_con.append(new_time_con[i])

        delete_nodes_list(nowe_active)
        delete_nodes_list(new_time_con)

def check_stop(active_nodes_list,time_con,v,Di):
    #print(active_nodes_list)
    for x in range(0,len(active_nodes_list)):
        for xx in range(1,len(active_nodes_list[x])):
            time_diff = (time_table_val[time_con[x][xx-1]] - time_table_val[time_con[x][0]])/15 +1
            #print(active_nodes_list[x])
            #print(time_con[x])
            #print(time_diff)
            if time_diff < D[active_nodes_list[x][0]][active_nodes_list[x][xx]]:
                Di[active_nodes_list[x][0]][active_nodes_list[x][xx]] +=1
                D[active_nodes_list[x][0]][active_nodes_list[x][xx]] = time_diff


def nowe_active_nodes(jjj,active_nodes_list, jum, time_con, j,nowe_active,new_time_con,time_cc,start):
    col=active_nodes_list[j]
    col.extend([jum])
    nowe_active.append(col)
    colt = time_con[j]
    colt.extend([time_cc[jjj]])
    new_time_con.append(colt)
def list_inst(list,D):
    for xx in range(0, len(list)):
        D[list[xx][0]][list[xx][1]] = 1
        D[list[xx][1]][list[xx][0]] =1
    print("list_inst done")
# (funkcja do wyszukiwania wszystkich sasiadow od wyznaczonego miejsca)
def find_con(contacts,next,j,time_cc,list):
    y=0
    for xx in range(0,len(list)):
        if list[xx][2]==j:
            y=xx

    for x in range(y, len(list)):

        if list[x][1]==next:
                contacts.extend([list[x][0]])
                time_cc.extend([list[x][2]])
        if list[x][0]==next:
                contacts.extend([list[x][1]])
                time_cc.extend([list[x][2]])


# wyszukuje wszystkie polaczenia start - jezeli nie ma to koniec
def search_start_con(start,nodes,list):


    for x in range(0,len(list)):

        if list[x][1]==start:

            nodes.append([list[x][2],list[x][0]])

        elif list[x][0]==start:
            nodes.append([list[x][2], list[x][1]])

#usuwanie elementow macierzy kontaktow
def delete_nodes_list(nodes):

    for n in range(0,len(nodes)):
        nodes.remove(nodes[0])

#utworzenie listy
def create_list(active_nodes_list,  nodes,start,jj,time_con ):
    active_nodes_list.append([start,nodes[jj][1]])
    time_con.append([nodes[jj][0]])


#odczytuje najkrotszy dystans miedzy kontaktami i liczy efficiency
def distance_read(D,dist,rel_eff):
    np.savetxt("distance.out", D, delimiter=",")

    for v in range(0,len(t.nodes)):
        for w in range(0,len(t.nodes)):
            if(v!=w):
                if D[v][w]==300:
                    dist+=0
                else:
                    dist+=(1.0/D[v][w])
    print("dist"+" "+str(dist)+" "+"/"+" "+str(len(t.nodes))+" "+"*"+" "+str(len(t.nodes)-1))
    rel_eff=dist/(len(t.nodes)*(len(t.nodes)-1))

    print("distance_read done")

    print("relative efficiency")
    print('% .4f' % rel_eff)
    plik.write("relative efficiency")
    plik.write(" ")
    plik.write(str('% .4f' % rel_eff))
    plik.write('\n')

#sredni stopien wezla - rozklad
def nr_con_node(C,nr_con_n,nr_con_t,Nr_con_no):
    lol = 0
    for v in range(0,len(t.nodes)):
        nr = 0

        suma = 0

        for w in range(v,len(t.nodes)):
            nr+=C[v][w]
            if C[v][w]!=0:
                lol+=1
        suma+=nr
        nr_con_n+=(suma/len(t.nodes))
        nr_con_t+=(suma/20)
        Nr_con_no.append(nr_con_n)
        print(lol)
    nr_con_n=(nr_con_n/len(t.nodes))
    nr_con_t = (nr_con_t / len(t.nodes))
    #print(nr_con_n)
    #print(nr_con_t)
    print("nr_con_node done")
    #print(lol/len(t.nodes))

# liczba kontaktow na wezel i na jednostke czasu, sredni wezel
def av_nr_node(C,av_n,Av_node):

    for v in range(0,len(t.nodes)):
        nr=0
        for w in range(v,len(t.nodes)):

            if C[v][w]!=0:
                av_n+=1
                nr+=1
        Av_node.append(nr)
    av_n=av_n/len(t.nodes)

    print("sredni stopien")
    print(av_n)
    plik.write("sredni stopien")
    plik.write(" ")
    plik.write(str(av_n))
    plik.write('\n')


 #histogram czasu wystepowania wezla w ukladzie
def time_show(tab_time):
    start=0
    stop=0
    for n in range(0,len(t.nodes)):
        for x in range(0,len(t.tedges)):
            if t.tedges[x][0]==t.nodes[n] or t.tedges[x][1]==t.nodes[n]:
                if start==0:
                    start=t.tedges[x][2]
                else:
                    stop = t.tedges[x][2]
        if (stop-start)<0:

            tab_time.append(float(-(stop-start)))
        else:
            tab_time.append(float(stop - start))
def miary(bet_n,bet_e,bb_e,bb_n):
	bet_n=(2/((len(t.nodes)-1)*(len(t.nodes)-2)))*bb_n
	bet_e=(2/(len(t.nodes)*(len(t.nodes)-1))*bb_e
def info_dane(av_n,rel_eff,bet_n,bet_e,dist,time_table_val):
	plik2=open(nazwa,'a')
	plik2.write(nazwa+"/t"+str(len(t.nodes))+"/t"+str(len(t.tedges))+"/t"+
	str(getObseravtionLenght())+"/t"+str(20)+"/t"+str(len(time_table_val)))+
	"/t"+str(av_n)+"/t"+str(dist)+"/t"+"betweenes_n"+"/t"+"betweenes_e"+
	"/t"+str(rel_eff))
	plik2.close()


def informacje():
    print("ilosc wezlow")
    print(len(t.nodes))
    plik.write("ilosc wezlow")
    plik.write(" ")
    plik.write(str(len(t.nodes)))
    plik.write('\n')

    print("ilosc kontaktow")
    print(len(t.tedges))
    plik.write("ilosc kontaktow")
    plik.write(" ")
    plik.write(str(len(t.tedges)))
    plik.write('\n')

    print("czas obserwacji")
    print(t.getObservationLength())
    plik.write("czas obserwacji")
    plik.write(" ")
    plik.write(str(t.getObservationLength()))
    plik.write('\n')

    print("delta czas")
    print(20)
    plik.write("delta czas")
    plik.write(" ")
    plik.write(str(20))
    plik.write('\n')

    print("liczb time stepow")
    print(len(time_table_val))
    plik.write("liczb time stepow")
    plik.write(" ")
    plik.write(str(len(time_table_val)))
    plik.write('\n')

def random_attack():
    for i in range(0,len(t.tedges)):
        if(random.uniform(0, 1)==1):
            t.tedges.remove(t.tedges[i])

def most_contact_attack_e(Di):
    di_all=0
    for j in range(0,len(t.nodes)):
        for jj in range (0, len(t.nodes)):
            di_all+=Di[j][jj]
    #t.tedges.remove(max())

def most_contact_attack_i(Di):
    di_all=0
    di_i=[]
    d=0
    for j in range(0,len(t.nodes)):
        for jj in range (0, len(t.nodes)):
            di_all+=Di[j][jj]
            d+=Di[j][jj]
        di_i.append(d)

    #t.tedges.remove(max())
time_table_val=[]
time_table_nr = []
dist=0
tab_time=[]
Av_node=[]
Nr_con_no=[]
ak=[]
av_n=0
rel_eff=0
nr_con_t=0
nr_con_n=0
A=[]
list_list=[]
Node_edges=[]
A_sum=[]
Di=np.zeros((len(t.nodes), len(t.nodes)))
B=np.zeros((len(t.nodes), len(t.nodes)))
D=np.zeros((len(t.nodes), len(t.nodes)))
C=np.zeros((len(t.nodes), len(t.nodes)))
for v in range(0,len(t.nodes)):
    for w in range(0,len(t.nodes)):
        D[v][w]=300
a = np.zeros((len(t.nodes), len(t.nodes)))
list=[]
adj2(time_table_val, time_table_nr,a,C,A,A_sum, Node_edges,list)
make_list(list_list,D)
shortest_distance_2(a,time_table_val,C,A,D,B,list,list_list,Di)
list_inst(list,D)
print(D)
distance_read(D,dist,rel_eff)


nr_con_node(C,nr_con_n,nr_con_t,Nr_con_no)
av_nr_node(C,av_n,Av_node)
time_show(tab_time)

wykresy(tab_time,Av_node,Nr_con_no)
informacje()
plik.close()

   


        
        
