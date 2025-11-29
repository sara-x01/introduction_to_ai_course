"""
Search Algorithms - RoboMind Project
SE444 - Artificial Intelligence Course Project

Implemented search algorithms:
1. Breadth-First Search (BFS)
2. Uniform Cost Search (UCS)
3. A* Search
"""

from typing import Tuple, List, Optional
from collections import deque
import heapq


def bfs(env, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], float, int]:
    """Breadth-First Search implementation."""
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    expanded = 0
    
    while queue:
        current = queue.popleft()
        expanded += 1
        
        if current == goal:
            path = reconstruct_path(parent, start, goal)
            cost = len(path) - 1
            return path, cost, expanded
        
        for neighbor in env.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return None, float('inf'), expanded


def ucs(env, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], float, int]:
    """Uniform Cost Search implementation."""
    frontier = [(0, start)]
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
            path = reconstruct_path(parent, start, goal)
            return path, current_cost, expanded
        
        for neighbor in env.get_neighbors(current):
            new_cost = current_cost + env.get_cost(current, neighbor)
            
            if neighbor not in explored:
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(frontier, (new_cost, neighbor))
    
    return None, float('inf'), expanded


def astar(env, start: Tuple[int, int], goal: Tuple[int, int], 
          heuristic='manhattan') -> Tuple[Optional[List], float, int]:
    """A* Search implementation."""
    if heuristic == 'manhattan':
        h = lambda pos: env.manhattan_distance(pos, goal)
    elif heuristic == 'euclidean':
        h = lambda pos: env.euclidean_distance(pos, goal)
    else:
        raise ValueError(f"Unknown heuristic: {heuristic}")
    
    g_score = {start: 0}
    f_score = {start: h(start)}
    frontier = [(f_score[start], start)]
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
            path = reconstruct_path(parent, start, goal)
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


def reconstruct_path(parent: dict, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Reconstruct path from parent pointers."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path
