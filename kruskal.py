from collections import defaultdict 
import networkx as nx
import matplotlib.pyplot as plt
import pylab
from tkinter import *

options = {
    'node_size': 500,
    'width': 1,
}


class Graph: 
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
                               

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    def Kruskal_MST(self): 
  
        result =[]
        result2 = []
  
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        while e < self.V -1 : 
  
        
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
       
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

  
       
        for u,v,weight  in result: 
            result2.append(f"\n{u+1} ==> {v+1}  Peso : {weight}\n")
        return result2
  
g = Graph(9) 

g.addEdge(0, 1, 4) 
g.addEdge(0, 7, 8) 
g.addEdge(1, 7, 11) 
g.addEdge(1, 2, 8) 
g.addEdge(7, 6, 1)
g.addEdge(7, 8, 7)
g.addEdge(8, 6, 6)
g.addEdge(8, 2, 2)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(6, 5, 2)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 6, 10)

G = nx.Graph()

G.add_edge(1, 2, weight=4) 
G.add_edge(1, 8, weight=8) 
G.add_edge(2, 8, weight=11) 
G.add_edge(2, 3, weight=8) 
G.add_edge(8, 7, weight=1)
G.add_edge(8, 9, weight=7)
G.add_edge(9, 7, weight=6)
G.add_edge(9, 3, weight=2)
G.add_edge(3, 4, weight=7)
G.add_edge(3, 6, weight=4)
G.add_edge(7, 6, weight=2)
G.add_edge(4, 6, weight=14)
G.add_edge(4, 5, weight=9)
G.add_edge(5, 6, weight=10)


print("Implementação")
print("Fim")

window = Tk()
window.geometry("400x250")
label1 = Label(window,text=g.Kruskal_MST())



#Implementação com biblioteca
#Podendo modificar o algoritmo para PRIM
a = nx.minimum_spanning_tree(G,weight='weight',algorithm='kruskal')
b = sorted(a.edges(data=True),reverse=True)

label2 = Label(window,text="Implementação(NETWORKX)\n"+str(b).replace('{','').replace('}','').replace(',','\n').replace('(','').replace(')','').replace('[','').replace(']',''))

label1.pack()
label2.pack()
#Representação Gráfica
pos = nx.circular_layout(G)
plt.title("Interface amigável")
plt.axis('off')
nx.draw(G,pos=pos,with_labels=True, font_weight='bold',**options)

plt.show()
window.mainloop()
pylab.show()
