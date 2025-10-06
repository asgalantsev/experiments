def DFS(graph, node, visited):
    if graph != {}:
        visited.add(node)
        for neighbour in graph[node]:
            if(neighbour not in visited):
                DFS(graph, neighbour, visited)


def test_dfs():
    # Test case 1: Simple connected graph
    graph1 = {0: [1, 2], 1: [2], 2: []}
    visited = set()
    DFS(graph1, 0, visited)
    assert visited == {0, 1, 2}, f"Test 1 failed: expected {set([0, 1, 2])}, got {visited}"

    # Test case 2: Graph with cycles
    graph2 = {0: [1], 1: [2, 0], 2: [3], 3: [2]}
    visited = set()
    DFS(graph2, 0, visited)
    assert visited == {0, 1, 2, 3}, f"Test 2 failed: expected {set([0, 1, 2, 3])}, got {visited}"

    # Test case 3: Graph with disconnected components
    graph3 = {0: [1], 1: [], 2: [3], 3: []}
    visited = set()
    DFS(graph3, 0, visited)
    assert visited == {0, 1}, f"Test 3 failed: expected {set([0, 1])}, got {visited}"

    # Test case 4: Graph with self-loop
    graph4 = {0: [1, 0], 1: []}
    visited = set()
    DFS(graph4, 0, visited)
    assert visited == {0, 1}, f"Test 4 failed: expected {set([0, 1])}, got {visited}"

    # Test case 5: Empty graph
    graph5 = {}
    visited = set()
    DFS(graph5, 0, visited)
    assert visited == set(), f"Test 5 failed: expected empty set, got {visited}"

    # Test case 6: Single node graph
    graph6 = {0: []}
    visited = set()
    DFS(graph6, 0, visited)
    assert visited == {0}, f"Test 6 failed: expected {set([0])}, got {visited}"

    print("All tests passed!")

if __name__ == "__main__":
    test_dfs()