"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    
def make_complete_graph(num_nodes):
    """
    creates a complete graph with num_nodes number of vertices
    input = number of nodes 
    output = a complete graph with input number of nodes
    """
    graph = dict()
    edge_set = set()
    for node in range(num_nodes):
        edge_set = set()
        for edge_node in range(num_nodes):
            if(node != edge_node):
                edge_set.add(edge_node)
        graph[node] = edge_set.copy()
    return graph

def upa(n,m):
    
    graph = make_complete_graph(m)
    up_inst = UPATrial(m)
    #print m,graph.values
    for dummy_var in range(m,n):
        new_node_neighbors = up_inst.run_trial(m)
        for new_node in new_node_neighbors:
            if( new_node not in graph):
                graph[new_node] = set()
            graph[new_node].add(dummy_var)
        graph[dummy_var] = new_node_neighbors

    return graph

upa_graph = upa(27770,13)

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

graph_dist = in_degree_distribution(dpa_graph)
print graph_dist
sum_deg =  sum(graph_dist.values())
norm_graph_dist = dict()
for k,v in graph_dist.items():
    norm_graph_dist[k] = v/float(sum_deg)
print norm_graph_dist
#print avg_out_degree(citation_graph) 

def build_plot(plot_type = True):
    """
    Build plot of the in degree distribution
    """
    plot = []
    for input_val in norm_graph_dist.keys():
        
        if(input_val != 0):
        
            if plot_type:
                plot.append([input_val, norm_graph_dist[input_val]])
            else:
                plot.append([math.log(input_val), math.log(norm_graph_dist[input_val])])
    return plot

plot1 = build_plot(False)
simpleplot.plot_lines("In-Degree Distribution", 600, 600, 
                      "log (base e) of indegree", "log (base e) of frequency", [plot1], True)


    

