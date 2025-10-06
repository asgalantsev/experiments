def BFS(adj):
    """
    Perform Breadth-First Search on a graph represented by adjacency list.
    
    Args:
        adj (list of list): Adjacency list representation of the graph
        
    Returns:
        list: BFS traversal order of the nodes
    """
    if not adj:
        return []

    visited = len(adj) * [False]
    res = []
    from collections import deque
    q = deque()

    # Start BFS from node 0
    visited[0] = True
    q.append(0)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res

def test_bfs():
    # Test case 1: Simple connected graph
    adj1 = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    assert BFS(adj1) == [0, 1, 2, 3, 4], "Test case 1 failed"

    # Test case 2: Graph with multiple components
    adj2 = [[1], [0], [3], [2]]  # Two disconnected components: [0-1] and [2-3]
    assert BFS(adj2) == [0, 1], "Test case 2 failed"

    # Test case 3: Graph with cycles
    adj3 = [[1,2], [0,2], [0,1]]  # Triangle graph
    assert BFS(adj3) == [0, 1, 2], "Test case 3 failed"

    # Test case 4: Graph with self-loops
    adj4 = [[1,0], [0]]
    assert BFS(adj4) == [0, 1], "Test case 4 failed"

    # Test case 5: Empty graph
    adj5 = []
    assert BFS(adj5) == [], "Test case 5 failed"

    # Test case 6: Graph with single node
    adj6 = [[]]
    assert BFS(adj6) == [0], "Test case 6 failed"

    # Test case 7: Graph with many nodes
    adj7 = [[1,2,3], [0,2], [0,1], [0,4], [3]]
    assert BFS(adj7) == [0, 1, 2, 3, 4], "Test case 7 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_bfs()