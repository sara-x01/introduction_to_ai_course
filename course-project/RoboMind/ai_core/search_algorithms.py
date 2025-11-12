"""
Search Algorithms - RoboMind Project
SE444 - Artificial Intelligence Course Project

TODO: Implement the following search algorithms:
1. Breadth-First Search (BFS)
2. Uniform Cost Search (UCS)
3. A* Search

This is the CORE of Phase 1 (Week 1-2)
"""

from typing import Tuple, List, Optional
from collections import deque
import heapq


def bfs(env, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], float, int]:
    """
    Breadth-First Search - Find shortest path in terms of number of steps.
    
    Algorithm:
        1. Use a queue (FIFO) to explore nodes level by level
        2. Keep track of visited nodes to avoid cycles
        3. Store parent pointers to reconstruct path
        4. Return when goal is found
    
    Args:
        env: GridWorld environment
        start: Starting position (row, col)
        goal: Goal position (row, col)
    
    Returns:
        path: List of (row, col) tuples from start to goal (None if no path)
        cost: Total path cost
        expanded: Number of nodes expanded
    
    Example:
        >>> env = GridWorld(10, 10)
        >>> path, cost, expanded = bfs(env, (0,0), (9,9))
        >>> print(f"Path length: {len(path)}, Cost: {cost}")
    """
    
    # TODO: Implement BFS
    # 
    # Hints:
    # - Use collections.deque() for the queue
    # - Keep a visited set to track explored nodes
    # - Store parent pointers in a dictionary: parent[child] = parent_node
    # - Use env.get_neighbors(pos) to get valid adjacent cells
    # - Count expanded nodes
    # - Reconstruct path by following parent pointers backwards
    
    # Your code here:
    
    raise NotImplementedError("BFS not implemented yet - this is your task!")
    
    # Example structure (delete this and implement properly):
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    expanded = 0
    
    while queue:
        current = queue.popleft()
        expanded += 1
        
        if current == goal:
            # Reconstruct path
            path = []
            # ... your code to build path from parent pointers ...
            cost = len(path) - 1  # BFS cost is number of steps
            return path, cost, expanded
        
        for neighbor in env.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return None, float('inf'), expanded  # No path found
    """


def ucs(env, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], float, int]:
    """
    Uniform Cost Search - Find path with lowest total cost.
    
    Algorithm:
        1. Use a priority queue (heap) ordered by path cost
        2. Always expand the lowest-cost node first
        3. Update costs when better paths are found
        4. Return when goal is expanded (not just added to frontier)
    
    Args:
        env: GridWorld environment
        start: Starting position (row, col)
        goal: Goal position (row, col)
    
    Returns:
        path: List of (row, col) tuples from start to goal (None if no path)
        cost: Total path cost
        expanded: Number of nodes expanded
    
    Note:
        UCS is essentially Dijkstra's algorithm.
        It finds the optimal path when edge costs are non-negative.
    """
    
    # TODO: Implement UCS
    #
    # Hints:
    # - Use heapq for priority queue: heapq.heappush(heap, (priority, item))
    # - Priority should be cumulative path cost: g(n)
    # - Keep track of best cost to reach each node
    # - Use env.get_cost(pos1, pos2) to get edge costs
    # - Don't return immediately when goal is added to frontier!
    # - Only return when goal is EXPANDED (popped from heap)
    
    # Your code here:
    
    raise NotImplementedError("UCS not implemented yet - this is your task!")
    
    # Example structure (delete and implement properly):
    """
    frontier = [(0, start)]  # (cost, position)
    explored = set()
    cost_so_far = {start: 0}
    parent = {start: None}
    expanded = 0
    
    while frontier:
        current_cost, current = heapq.heappop(frontier)
        
        if current in explored:
            continue
        
        explored.add(current)
        expanded += 1
        
        if current == goal:
            # Reconstruct path
            # ... your code ...
            return path, current_cost, expanded
        
        for neighbor in env.get_neighbors(current):
            new_cost = current_cost + env.get_cost(current, neighbor)
            
            if neighbor not in explored:
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(frontier, (new_cost, neighbor))
    
    return None, float('inf'), expanded
    """


def astar(env, start: Tuple[int, int], goal: Tuple[int, int], 
          heuristic='manhattan') -> Tuple[Optional[List], float, int]:
    """
    A* Search - Find optimal path using cost + heuristic.
    
    Algorithm:
        1. Like UCS but uses f(n) = g(n) + h(n)
        2. g(n) = cost from start to n
        3. h(n) = heuristic estimate from n to goal
        4. Expands nodes in order of f(n) value
    
    Args:
        env: GridWorld environment
        start: Starting position (row, col)
        goal: Goal position (row, col)
        heuristic: 'manhattan' or 'euclidean'
    
    Returns:
        path: List of (row, col) tuples from start to goal (None if no path)
        cost: Total path cost (actual g(n), not f(n))
        expanded: Number of nodes expanded
    
    Heuristics:
        Manhattan: |x1-x2| + |y1-y2| (for 4-connected grid)
        Euclidean: sqrt((x1-x2)² + (y1-y2)²)
    
    Properties:
        - If h(n) is admissible (never overestimates), A* is optimal
        - If h(n) is consistent (monotonic), A* is optimally efficient
        - Manhattan distance is admissible for 4-connected grids
    """
    
    # TODO: Implement A*
    #
    # Hints:
    # - Very similar to UCS, but priority is f(n) = g(n) + h(n)
    # - Use env.manhattan_distance(pos, goal) or env.euclidean_distance(pos, goal)
    # - Store g(n) separately (actual cost from start)
    # - Priority queue contains f(n), but track g(n) for path cost
    # - When reconstructing path, return actual g(goal), not f(goal)
    
    # Your code here:
    
    raise NotImplementedError("A* not implemented yet - this is your task!")
    
    # Example structure (delete and implement properly):
    """
    # Choose heuristic function
    if heuristic == 'manhattan':
        h = lambda pos: env.manhattan_distance(pos, goal)
    elif heuristic == 'euclidean':
        h = lambda pos: env.euclidean_distance(pos, goal)
    else:
        raise ValueError(f"Unknown heuristic: {heuristic}")
    
    # A* uses f(n) = g(n) + h(n) as priority
    g_score = {start: 0}
    f_score = {start: h(start)}
    frontier = [(f_score[start], start)]  # (f_score, position)
    explored = set()
    parent = {start: None}
    expanded = 0
    
    while frontier:
        current_f, current = heapq.heappop(frontier)
        
        if current in explored:
            continue
        
        explored.add(current)
        expanded += 1
        
        if current == goal:
            # Reconstruct path and return ACTUAL cost (g_score), not f_score
            # ... your code ...
            return path, g_score[current], expanded
        
        for neighbor in env.get_neighbors(current):
            if neighbor in explored:
                continue
            
            tentative_g = g_score[current] + env.get_cost(current, neighbor)
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor)
                parent[neighbor] = current
                heapq.heappush(frontier, (f_score[neighbor], neighbor))
    
    return None, float('inf'), expanded
    """


def reconstruct_path(parent: dict, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Reconstruct path from parent pointers.
    
    Args:
        parent: Dictionary mapping child -> parent
        start: Starting position
        goal: Goal position
    
    Returns:
        path: List of positions from start to goal
    
    Example:
        >>> parent = {(0,1): (0,0), (1,1): (0,1), (2,1): (1,1)}
        >>> reconstruct_path(parent, (0,0), (2,1))
        [(0,0), (0,1), (1,1), (2,1)]
    """
    # TODO: Implement path reconstruction
    #
    # Hint: Follow parent pointers backwards from goal to start, then reverse
    
    raise NotImplementedError("Path reconstruction not implemented yet!")


# ============================================================================
# Testing Code (You can run this file directly to test your implementations)
# ============================================================================

if __name__ == "__main__":
    from environment import GridWorld
    
    print("=" * 60)
    print("  Testing Search Algorithms")
    print("=" * 60 + "\n")
    
    # Create a test environment
    env = GridWorld(width=10, height=10)
    
    # Add obstacles
    for i in range(3, 8):
        env.add_obstacle(i, 5)
    
    start = (0, 0)
    goal = (9, 9)
    
    print(f"Grid: {env.width}x{env.height}")
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print(f"Obstacles: {(env.grid == 1).sum()}\n")
    
    # Test each algorithm
    algorithms = [
        ('BFS', lambda: bfs(env, start, goal)),
        ('UCS', lambda: ucs(env, start, goal)),
        ('A* (Manhattan)', lambda: astar(env, start, goal, 'manhattan')),
        ('A* (Euclidean)', lambda: astar(env, start, goal, 'euclidean')),
    ]
    
    results = []
    
    for name, algo_func in algorithms:
        print(f"\nTesting {name}...")
        print("-" * 40)
        try:
            path, cost, expanded = algo_func()
            if path:
                print(f"✓ Success!")
                print(f"  Path length: {len(path)} steps")
                print(f"  Path cost: {cost:.2f}")
                print(f"  Nodes expanded: {expanded}")
                results.append((name, True, len(path), cost, expanded))
            else:
                print(f"✗ No path found")
                results.append((name, False, 0, 0, 0))
        except NotImplementedError:
            print(f"⚠️  Not implemented yet")
            results.append((name, False, 0, 0, 0))
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            results.append((name, False, 0, 0, 0))
    
    # Summary table
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(f"{'Algorithm':<20} {'Status':<10} {'Length':<8} {'Cost':<8} {'Expanded':<10}")
    print("-" * 60)
    
    for name, success, length, cost, expanded in results:
        status = "✓" if success else "✗"
        length_str = str(length) if success else "-"
        cost_str = f"{cost:.2f}" if success else "-"
        expanded_str = str(expanded) if success else "-"
        print(f"{name:<20} {status:<10} {length_str:<8} {cost_str:<8} {expanded_str:<10}")
    
    print("-" * 60)
    print("\n💡 Tip: Implement the algorithms one at a time and test each one!")
    print("   Start with BFS (simplest), then UCS, then A*\n")

