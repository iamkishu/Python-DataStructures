
from tabnanny import check


adj_graph_list = {
    "A" : ["B"],
    "B" : ["C"],
    "C" : ["D"],
    "D" : ["E"],
    "E" : ["F",],
    "F" : ["G"],
    "G" : ["H"],
    "H" : ["A"]
}
'''
adj_graph_list = {
    "A" : ["B", "D"],
    "B" : ["A", "C"],
    "C" : ["B"],
    "D" : ["A", "E", "F"],
    "E" : ["D", "F", "G"],
    "F" : ["D", "E", "H"],
    "G" : ["E", "H"],
    "H" : ["G", "F"]
}
'''

#DFS

visited = {}
parent = {}
dfs_output = []

for i in adj_graph_list.keys():
    visited[i] = False
    parent[i] = None

dfs_stack = []
origin = 'A'
dfs_stack.append(origin)
visited[origin] = True

''' #dfs core
while len(dfs_stack) > 0:
    el = dfs_stack.pop()
    dfs_output.append(el)
    for i in adj_graph_list[el]:
        if visited[i] is not True:
            visited[i] = True
            parent[i] = el
            dfs_stack.append(i)

print(dfs_output)
'''

check_loop = False
while len(dfs_stack) > 0:
    el = dfs_stack.pop()
    dfs_output.append(el)
    print(adj_graph_list[el])
    for i in adj_graph_list[el]:
        if visited[i] is not True:
            visited[i] = True
            parent[i] = el
            dfs_stack.append(i)
        else:
            if i == adj_graph_list[parent[el]]:
                check_loop = False
            else:
                check_loop = True
if check_loop:
    print('Looped')
else:
    print("No loop")
                
#print(dfs_output)