# Name:Jeb Barker
# Date:Sep. 20, 2020

# Each Vertex object will have attributes to store its own name and its list of its neighboring vertices.
class Vertex:
    def __init__(self, value, edge_list):
        self.value = value
        self.edge_list = edge_list
    def getEdge_list(self):
        return self.edge_list
    # def __str__(self):
    # return self.value + " " + str(self.edge_list)


# If the file exists, read all edges and build a graph. It returns a list of Vertexes.
def build_graph_deprecated(filename):
    try:
        file = open(filename)
        graph = {}
        for v in file:
            vertex = Vertex(v.strip().split()[0], [])
            if vertex.value in list(graph):
                # print(graph[vertex.value])
                graph[vertex.value].append(v.split()[1][0:1])
                # print(v.strip().split()[1])
            else:
                graph[vertex.value] = list(v.strip().split()[1])

        return [Vertex(k, graph[k]) for k in list(graph)]

    except FileNotFoundError:
        return []


def build_graph(filename):
    try:
        graph = []
        file_ = open(filename)
        for x, line in enumerate(file_.readlines()):
            vert = [line.split()[0] == v.value for v in graph]
            if not any(vert):
                graph.append(Vertex(line.split()[0], []))

        file = open(filename)
        for line in file.readlines():
            vert = [line.split()[0] == v.value for v in graph]
            newVert = [line.split()[1] == v.value for v in graph]
            print(vert.index(True))
            print(newVert.index(True))
            vertex = graph[vert.index(True)]
            edgeL = vertex.edge_list
            newVertex = graph[newVert.index(True)]
            edgeL.append(newVertex)
            display_graph(graph)
        return graph



    except FileNotFoundError:
        return []


# prints all vertices and adjacent lists of the given graph.
def display_graph(graph):
    for v in graph:
        print(str(v.value) + " " + str([ver.value for ver in v.edge_list]))


# checks if two Vertexes are reachable or not.
def is_reachable(fromV, toV, graph):
    if fromV == toV:
        return True
    else:
        if any([is_reachable(v, toV, graph) for v in fromV.edge_list]):
            return True
        return False


# returns the length of the path from a Vertex to the other Vertex.
# If the other Vertex is not reachable, return -1.  (Ex) Path cost of A to B to C is 2.
def path_cost(fromV, toV, graph):
    if fromV == toV:
        return 1
    else:
        for v in fromV.edge_list:
            return path_cost(v, toV, graph) + 1
    return -1

"""
# Test cases
g = build_graph(input("filename: "))  # build a graph

# To check if you build the graph with object correctly
for v in g:
    print(v, v.edge_list)

display_graph(g)  # display the graph (edge list)
fromV, toV = None, None
print("If you want to stop checking, type -1 for vertex values")
fromV_val, toV_val = input("From vertex value: "), input("To vertex value: ")  # Get vertex values from user

while fromV_val != '-1':
    # Find from and to Vertexes at graph
    for v in g:
        if v.value == fromV_val: fromV = v
        if v.value == toV_val: toV = v

    if fromV is None or toV is None:
        print("One or more vertex value does not exist.")
    else:
        print("From {} to {} is reachable?".format(fromV_val, toV_val), is_reachable(fromV, toV, g))
        print("Path cost from {} to {} is".format(fromV_val, toV_val), path_cost(fromV, toV, g))

    # Reset to test another case
    fromV_val, toV_val = input("\nFrom vertex value: "), input("To vertex value: ")
    fromV, toV = None, None
"""
''' Sample output:
Content of abcd.txt:
A C
B A
C C
C D
D C
D A

 ----jGRASP exec: python Lab_0_build_graph_kim.py
filename: abcd.txt
<__main__.Vertex object at 0x000001E96F03D6A0> [<__main__.Vertex object at 0x000001E96F03DEE0>]
<__main__.Vertex object at 0x000001E96F062640> [<__main__.Vertex object at 0x000001E96F03D6A0>]
<__main__.Vertex object at 0x000001E96F03DEE0> [<__main__.Vertex object at 0x000001E96F03DEE0>, <__main__.Vertex object at 0x000001E96F0627C0>]
<__main__.Vertex object at 0x000001E96F0627C0> [<__main__.Vertex object at 0x000001E96F03DEE0>, <__main__.Vertex object at 0x000001E96F03D6A0>]
A ['C']
B ['A']
C ['C', 'D']
D ['C', 'A']
If you want to stop checking, type -1 for vertex values
From vertex value: A
To vertex value: B
From A to B is reachable? False
Path cost from A to B is 9999

From vertex value: B
To vertex value: A
From B to A is reachable? True
Path cost from B to A is 1

From vertex value: A
To vertex value: D
From A to D is reachable? True
Path cost from A to D is 2

From vertex value: B
To vertex value: D
From B to D is reachable? True
Path cost from B to D is 3

From vertex value: C
To vertex value: C
From C to C is reachable? True
Path cost from C to C is 0

From vertex value: C
To vertex value: E
One or more vertex value does not exist.

From vertex value: C
To vertex value: A
From C to A is reachable? True
Path cost from C to A is 2

From vertex value: D
To vertex value: C
From D to C is reachable? True
Path cost from D to C is 1

From vertex value: -1
To vertex value: -1

 ----jGRASP: operation complete.
'''
