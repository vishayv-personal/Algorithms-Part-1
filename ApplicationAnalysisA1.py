"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import simpleplot
import math

# Set timeout for CodeSkulptor if necessary
import codeskulptor
codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

def avg_out_degree(digraph):
    """
    computes avg out-degree of a given graph
    """
    summ = 0
    for node,edge_list in digraph.items():
        summ += len(edge_list)
    #print summ
    return float(summ)/len(digraph)

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

graph_dist = in_degree_distribution(citation_graph)
print graph_dist
sum_deg =  sum(graph_dist.values())
norm_graph_dist = dict()
for k,v in graph_dist.items():
    norm_graph_dist[k] = v/float(sum_deg)
print norm_graph_dist
print avg_out_degree(citation_graph) 

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
                      "log (base e) of indegree", "log (base e) of frequency", [plot1], false)



