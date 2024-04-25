class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafos = [[] for i in range(self.vertices)]

    def add_aresta(self, u, v):
        # Grafo direcionado simples sem peso
        self.grafos[u-1].append(v)

        # self.grafos[v-1].append(u) Caso o grafo não seja direcionado
    
    def mostra_lista(self):
        print('Lista de adjacencia do grafo: ')
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ') # Mostra as linhas inteiras da matriz
            for j in self.grafos[i]:
                print(f'{j}  ->', end='  ')
            print('')

g = Grafo(4)

g.add_aresta(1, 2)
g.add_aresta(1, 3)
g.add_aresta(1, 4)
g.add_aresta(2, 3)

g.mostra_lista()
