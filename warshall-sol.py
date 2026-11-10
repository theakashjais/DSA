import copy
import pydot

#graph = [[0, 1, 1, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0],
#         [0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0]]

names = ['A', 'B', 'C', 'D', 'E', 'F']
graph = [[0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0]]

def warshall(A):
    T = copy.deepcopy(A)
    for i in range(len(T)):
        T[i][i] = 1

    for k in range(len(T)):
        for j in range(len(T)):
            for i in range(len(T)):
                if T[i][j] == 0:                    # no direct connection
                    if T[i][k] > 0 and T[k][j] > 0: # path via k exists
                        T[i][j] = 1                 # add direct edge
    return T

def write_transitive_closure(graph, closure, names):
    digraph = pydot.Dot(graph_type='digraph')
    for i in range(len(graph)):
        digraph.add_node(pydot.Node(names[i]))
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] > 0:
                digraph.add_edge(pydot.Edge(names[i], names[j]))
    digraph.write_pdf('graph.pdf')
    for i in range(len(closure)):
        for j in range(len(closure)):
            if closure[i][j] > 0 and graph[i][j] == 0 and i != j:
                digraph.add_edge(pydot.Edge(names[i], names[j], color='red'))
    digraph.write_pdf('graph-transitive-closure.pdf')


closure = warshall(graph)
write_transitive_closure(graph, closure, names)

def Warshall(A):
   T = copy.deepcopy(A)
   for k in range(len(T)):
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == 0:
                if T[i][k]>0 and T[k][j]>0:
                    T[i][j] = 1
   return T

            