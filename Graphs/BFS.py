import collections


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

#BFS

visited = {}
parent = {}
level = {}
bfs_out = []
bfs_queue = collections.deque()

for node in  adj_graph_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

source = "A"
visited[source] = True
level[source] = 0
bfs_queue.append(source)

while len(bfs_queue) > 0 :
    el = bfs_queue.popleft()
    bfs_out.append(el)
    for i in adj_graph_list[el]:
        if visited[i] is not True:
            visited[i] = True
            parent[i] = el
            level[i] = level[el]+1
            bfs_queue.append(i)

print(bfs_out)

#shortest distance to 'G' from source [A]
print(level)
print(level['G'])


#shortest path to 'G' from source 
destination = 'G'
path = []
while destination is not None:
    path.append(destination)
    destination = parent[destination]
path.reverse()
print(path)



