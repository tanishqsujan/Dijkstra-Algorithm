from typing import List, Optional

def is_safe(vertex: int, color: int, colors: List[int], graph: List[List[int]]) -> bool:
    """
    Check if it's safe to color `vertex` with `color`.
    graph is adjacency matrix: graph[u][v] == 1 if u and v are adjacent.
    colors holds assigned colors for vertices (0 if unassigned).
    """
    for v in range(len(graph)):
        if graph[vertex][v] == 1 and colors[v] == color:
            return False
    return True

def solve_m_coloring(
    graph: List[List[int]],
    m: int,
    colors: Optional[List[int]] = None,
    vertex: int = 0,
    find_all: bool = False,
    solutions: Optional[List[List[int]]] = None
) -> List[List[int]]:
    """
    Backtracking solver.
    - graph: adjacency matrix (n x n)
    - m: number of colors
    - colors: working list of length n (0 = unassigned)
    - vertex: current vertex to color
    - find_all: if True, collect ALL solutions; otherwise stop at first
    Returns a list of solutions; each solution is a list of colors (1..m).
    """
    n = len(graph)
    if colors is None:
        colors = [0] * n
    if solutions is None:
        solutions = []

    if vertex == n:
        solutions.append(colors.copy())
        return solutions if find_all else solutions

    for c in range(1, m + 1):
        if is_safe(vertex, c, colors, graph):
            colors[vertex] = c
            solve_m_coloring(graph, m, colors, vertex + 1, find_all, solutions)
            if solutions and not find_all:
                return solutions
            colors[vertex] = 0

    return solutions

def can_color(graph: List[List[int]], m: int) -> Optional[List[int]]:
    """
    Convenience: return one valid coloring (list of colors) if possible, else None.
    """
    sols = solve_m_coloring(graph, m, find_all=False)
    return sols[0] if sols else None

def print_coloring(sol: List[int]) -> None:
    print("Vertex : Color")
    for i, c in enumerate(sol):
        print(f"{i} : {c}")

if __name__ == "__main__":
    graph_example = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0]
    ]

    m = 3  
    solution = can_color(graph_example, m)

    if solution:
        print(f"Graph can be colored with {m} colors. One coloring:")
        print_coloring(solution)
    else:
        print(f"Graph cannot be colored with {m} colors.")

    all_solutions = solve_m_coloring(graph_example, m, find_all=True)
    print(f"\nFound {len(all_solutions)} solution(s) with {m} colors.\n")
    for idx, sol in enumerate(all_solutions, start=1):
        print(f"Solution {idx}: {sol}")
