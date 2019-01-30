"""
Node List Example:
start-end-weight,start-end-weight
[a-b-3,a-c-2,b-c-5]
"""
def main():
    print("¯\_(ツ)_/¯")
    nodes = make_nodes(input().split(','))
    n = None
    while n is None:
        search = input("What vertex do we start with?: ")
        print(search)
        n = get_node(nodes, search)
    count = find_dijkstra_graph(nodes, n)
    for i in count:
        print(i,":", count[i])

# Turn our list of strings into something useful
# WORKING
def make_nodes(node_list):
    list = []
    for i in node_list:
        i = i.split('-')
        name = i[0]
        n = get_node(list, name)
        if n is None:
            node = {"name":i[0]}
            node['vertices'] = []
            node['vertices'].append({"node":i[1], "weight":int(i[2])})
            list.append(node)
        else:
            n['vertices'].append({"node":i[1], "weight":int(i[2])})

        #now make it reflexive (non-directed graph)
        # could make another helper function, but it'd save 10 lines ¯\_(ツ)_/¯
        name = i[1]
        n = get_node(list, name)
        if n is None:
            node = {"name":i[1]}
            node['vertices'] = []
            node['vertices'].append({"node":i[0], "weight":int(i[2])})
            list.append(node)
        else:
            n['vertices'].append({"node":i[0], "weight":int(i[2])})
    return list

# Helper checks to see if dictionary result already exists
# WORKING
def get_node(list, attr):
    for i in list:
        if i['name']==attr:
            return i
    return None

#Given a node to start from, find dijkstra's shortest
#   path to all other connected nodes in the graph
# WORKING
def find_dijkstra_graph(vertices, starting_vertex):
    distances = set_up_distances(vertices, starting_vertex)
    visited = []
    visit_surrounding_nodes(starting_vertex, distances, vertices, visited)
    return distances

# Recursive method to check surrounding nodes and change distances accordingly
# WORKING
def visit_surrounding_nodes(node, distances, vertices, visited):
    visited.append(node)
    node_name = node['name']
    for i in node['vertices']:
        i_name = i['node']
        # current_weight =
        if distances[node_name] + i['weight'] < distances[i_name]:
            distances[i_name] = distances[node_name] + i['weight']
    # Now recurse through other nodes
    for i in node['vertices']:
        if i['node'] == node_name:
            node['vertices'].pop(i)
        n = get_node(vertices, i['node'])
        if n in visited:
            continue
        else:
            visit_surrounding_nodes(n, distances, vertices, visited)


# Set all distances to max
# WORKING
def set_up_distances(vertices, starter):
    max = float("inf")
    distances = {}
    for i in vertices:
        if i == starter:
            distances[i['name']] = 0
        else:
            distances[i['name']] = max
    return distances

main()
