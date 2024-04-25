#Matriz de distancia

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v, peso):
        # Grafo direcionado simples
        self.grafo[u-1][v-1] = peso  # Pesos positivos

        # self.grafo[v-1][u-1] = 1 Caso o grafo não seja direcionado
    
    def mostra_matriz(self):
        print('Matriz de adjacencia do grafo: ')
        for i in range(self.vertices):
            print(self.grafo[i]) # Mostra as linhas inteiras da matriz 


v = int(input('Digite o numero de vertices: '))
g = Grafo(v)

a = int(input('Digite o numero de arestas: '))
for i in range(a):
    u =  int (input('Digite o vertice de origem: '))
    v = int (input('Digite o vertice de destino: '))
    peso = int(input('Digite o peso da aresta: '))
    g.add_aresta(u, v, peso)
    
g.mostra_matriz()
    
# Adicionar arestas manualmente:

# g = Grafo(4)

# g.add_aresta(1, 2, 5)
# g.add_aresta(3, 4, 9)
# g.add_aresta(2, 3, 3)

# g.mostra_matriz()

