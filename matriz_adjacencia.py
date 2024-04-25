#Matriz de adjacencia

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        # Grafo direcionado simples
        self.grafo[u-1][v-1] = 1  # Trocar o = por >= se for multigrafo

        # self.grafo[v-1][u-1] = 1 Caso o grafo não seja direcionado
    
    def mostra_matriz(self):
        print('Matriz de adjacencia do grafo: ')
        for i in range(self.vertices):
            print(self.grafo[i]) # Mostra as linhas inteiras da matriz 

    
g = Grafo(4)

g.add_aresta(1, 2)
g.add_aresta(3, 4)
g.add_aresta(2, 3)

g.mostra_matriz()

