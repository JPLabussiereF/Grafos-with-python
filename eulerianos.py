# Se um grafo não tem nenhum vertice com grau impár, vai ser um grafo euleriano.
# Se um grafo tem exatamente 2 vertices com grau impar, vai ser um grafo semi-euleriano.
# Se um grafo tem mais de 2 vertices com grau impar, não vai ser um grafo euleriano, nem semi-euleriano.
# Semi-euleirano começa em um vertice com grau impar e termina em outro vertice com grau impar (ou seja, começa e termina em vertices diferentes).
# Euleriano começa e termina no mesmo vertice.
# Caso o grafo não seja nem eureliano, nem semi-euleriano, eles vao repetir arestas.

#Matriz de adjacencia

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        # Multigrafo 
        self.grafo[u-1][v-1] += 1  # Trocar o += por =, se for grafo simples
        if u != v: # Essa linha de código permite arestas multiplas e laços.
            self.grafo[v-1][u-1] = 1 
    
    def mostra_matriz(self):
        print('Matriz de adjacencia do grafo: ')
        for i in range(self.vertices):
            print(self.grafo[i]) # Mostra as linhas inteiras da matriz 

    def possui_aresta(self, u, v):
        if self.grafo[u-1][v-1] == 0:
            print(f'Não existe aresta entre {u} e {v}')
        else:
            print(f'Existe {self.grafo[u-1][v-1]} de arestas entre {u} e {v}')

    def euleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau = grau + 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]
            if grau % 2 != 0:
                contador += 1
        if contador == 0:
            print('O grafo é euleriano')
        elif contador == 2:
            print('O grafo é semi-euleriano')
        else:
            print('O grafo não é euleriano nem semi-euleriano')


g = Grafo(4)

g.add_aresta(1, 2)
g.add_aresta(3, 4)
g.add_aresta(2, 3)
g.add_aresta(1, 4)


g.possui_aresta(2, 1)
g.possui_aresta(2, 4)

g.euleriano()

g.mostra_matriz()



    