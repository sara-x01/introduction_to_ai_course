"""
Search Agent - RoboMind Project
SE444 - Artificial Intelligence Course Project

Agent that uses search algorithms to navigate the grid world.
"""

from typing import Tuple, List, Optional
import sys
import os

# Add the parent directory to path to import ai_core
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ai_core.search_algorithms import bfs, ucs, astar


class SearchAgent:
    """
    An AI agent that uses search algorithms to find paths in the grid world.
    """
    
    def __init__(self, env):
        """
        Initialize the search agent.
        
        Args:
            env: GridWorld environment
        """
        self.env = env
        self.path = None
        self.current_step = 0
    
    def search(self, algorithm: str, heuristic: str = 'manhattan') -> Tuple[Optional[List], float, int]:
        """
        Perform search from start to goal using specified algorithm.
        
        Args:
            algorithm: 'bfs', 'ucs', or 'astar'
            heuristic: 'manhattan' or 'euclidean' (for A* only)
        
        Returns:
            path: List of positions from start to goal
            cost: Total path cost
            expanded: Number of nodes expanded
        """
        start = self.env.start
        goal = self.env.goal
        
        print(f"Searching with {algorithm.upper()} from {start} to {goal}...")
        
        if algorithm == 'bfs':
            path, cost, expanded = bfs(self.env, start, goal)
        elif algorithm == 'ucs':
            path, cost, expanded = ucs(self.env, start, goal)
        elif algorithm == 'astar':
            path, cost, expanded = astar(self.env, start, goal, heuristic)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")
        
        self.path = path
        self.current_step = 0
        
        # Update environment for visualization
        if path:
            self.env.path = path
            self.env.expanded = expanded
        else:
            self.env.path = []
            self.env.expanded = expanded
            
        return path, cost, expanded
    
    def get_next_move(self) -> Optional[Tuple[int, int]]:
        """
        Get the next position in the planned path.
        
        Returns:
            Next position (row, col) or None if no path or at goal
        """
        if self.path is None or self.current_step >= len(self.path):
            return None
        
        next_pos = self.path[self.current_step]
        self.current_step += 1
        return next_pos
    
    def has_path(self) -> bool:
        """Check if the agent has a valid path."""
        return self.path is not None and len(self.path) > 0
    
    def is_at_goal(self) -> bool:
        """Check if the agent has reached the goal."""
        if not self.has_path():
            return False
        return self.current_step >= len(self.path)
    
    def reset(self):
        """Reset the agent's state."""
        self.path = None
        self.current_step = 0
