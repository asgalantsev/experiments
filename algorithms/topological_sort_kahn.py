from collections import defaultdict


def topological_sort_kahn(graph):
    indegree = defaultdict(int)
    queue = []

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []

    while queue:

        node = queue.pop(0)
        topological_order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

        
    if(len(topological_order) != len(graph)):
        print("Cycle exists")
        return []

    return topological_order


def test_topological_sort():
    # Test case 1: A simple DAG
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    print("\nTest Case 1 - DAG:")
    result1 = topological_sort_kahn(graph1)
    print("Topological Order:", result1)
    
    # Test case 2: Graph with cycle
    graph2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    print("\nTest Case 2 - Graph with cycle:")
    result2 = topological_sort_kahn(graph2)
    print("Topological Order:", result2)

if __name__ == "__main__":
    test_topological_sort()
