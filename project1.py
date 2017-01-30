""" 
project 1 
contains the make_complete_graph, compute_in_degrees and in_degree_distribution method 
implementations 

"""

EX_GRAPH0 = dict()
EX_GRAPH0[0] = set([1,2])
EX_GRAPH0[1] = set()
EX_GRAPH0[2] = set()
EX_GRAPH1 = {0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2 = {0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}



def make_complete_graph(num_nodes):
    """
    creates a complete graph with num_nodes number of vertices
    input = number of nodes 
    output = a complete graph with input number of nodes
    """
    graph = dict()
    edge_set = set()
    for node in range(num_nodes):
        edge_set.clear()
        for edge_node in range(num_nodes):
            if(node != edge_node):
                edge_set.add(edge_node)
        graph[node] = edge_set.copy()
    return graph

print make_complete_graph(5)
print make_complete_graph(1)
print make_complete_graph(0)
print make_complete_graph(-1)



def compute_in_degrees(digraph):
    """
    computes the indegrees of a given graph
    """
    in_degree_count = dict()
    for node,edge_list in digraph.items():
        for edge_node in edge_list:
            if edge_node in in_degree_count:
                in_degree_count[edge_node] += 1
            else:
                in_degree_count[edge_node] = 1
        if(node not in in_degree_count):
            in_degree_count[node] = 0
    return in_degree_count

print "compute in degree"
print compute_in_degrees(EX_GRAPH0)
print compute_in_degrees(EX_GRAPH1)
print compute_in_degrees(EX_GRAPH2)



def in_degree_distribution(digraph):
    """
    compute the degree distribution of the input digraph
    """
    distribution_in_degree = dict()
    degree_count = compute_in_degrees(digraph)
    for count in degree_count.values():
        if count in distribution_in_degree:
            distribution_in_degree[count] += 1
        else: 
            distribution_in_degree[count] = 1
    return distribution_in_degree

print "indegree distribution"
a_dist = in_degree_distribution(EX_GRAPH0)
print a_dist
b = sum(a_dist.values())
norm_a_dist = {x: (y/float(b)) for x, y in a_dist.items()}
norm_graph_dist = {x:(y/float(b)) for x,y in a_dist.items()}
norm_graph_dist2 = dict((k, v/float(b)) for k, v in a_dist.items())
print norm_graph_dist2
print in_degree_distribution(EX_GRAPH1)
print in_degree_distribution(EX_GRAPH2)