"""
RoboMind Environment - Grid World Simulator
SE444 - Artificial Intelligence Course Project

This file provides the simulation environment for the RoboMind project.
Students should NOT modify this file - use it to test your agents.
"""

import pygame
import numpy as np
from typing import Tuple, List, Optional

# Colors
WHITE = (255, 255, 255)
BLACK = (50, 50, 50)
GREEN = (76, 175, 80)
RED = (244, 67, 54)
BLUE = (33, 150, 243)
GRAY = (200, 200, 200)
YELLOW = (255, 235, 59)
ORANGE = (255, 152, 0)

# Cell types
FREE = 0
OBSTACLE = 1
START = 2
GOAL = 3
PATH = 4
VISITED = 5
UNCERTAIN = 6


class GridWorld:
    """
    A 2D grid world environment for AI agents.
    """
    
    def __init__(self, width=10, height=10, cell_size=50):
        """
        Initialize grid world.
        
        Args:
            width: Number of columns
            height: Number of rows
            cell_size: Size of each cell in pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # Create empty grid
        self.grid = np.zeros((height, width), dtype=int)
        
        # Agent position
        self.start = (0, 0)
        self.goal = (height-1, width-1)
        self.agent_pos = self.start
        
        # State tracking
        self.path = []
        self.visited = set()
        self.expanded = 0
        
        # Pygame setup
        self.screen = None
        self.clock = None
        self.running = False
        
    def load_map(self, map_file: str):
        """
        Load a map from a text file.
        
        Format:
            0 = free space
            1 = obstacle
            S = start
            G = goal
            ? = uncertain
        """
        with open(map_file, 'r') as f:
            lines = f.readlines()
        
        self.height = len(lines)
        self.width = len(lines[0].strip().split())
        self.grid = np.zeros((self.height, self.width), dtype=int)
        
        for i, line in enumerate(lines):
            cells = line.strip().split()
            for j, cell in enumerate(cells):
                if cell == '1':
                    self.grid[i][j] = OBSTACLE
                elif cell == 'S':
                    self.start = (i, j)
                    self.agent_pos = self.start
                elif cell == 'G':
                    self.goal = (i, j)
                elif cell == '?':
                    self.grid[i][j] = UNCERTAIN
    
    def add_obstacle(self, row: int, col: int):
        """Add an obstacle at (row, col)."""
        if 0 <= row < self.height and 0 <= col < self.width:
            self.grid[row][col] = OBSTACLE
    
    def add_random_obstacles(self, num_obstacles: int):
        """Add random obstacles to the grid."""
        count = 0
        while count < num_obstacles:
            row = np.random.randint(0, self.height)
            col = np.random.randint(0, self.width)
            
            # Don't place obstacle on start or goal
            if (row, col) != self.start and (row, col) != self.goal:
                if self.grid[row][col] == FREE:
                    self.add_obstacle(row, col)
                    count += 1
    
    def is_valid(self, pos: Tuple[int, int]) -> bool:
        """Check if position is valid (within bounds and not obstacle)."""
        row, col = pos
        return (0 <= row < self.height and 
                0 <= col < self.width and 
                self.grid[row][col] != OBSTACLE)
    
    def is_goal(self, pos: Tuple[int, int]) -> bool:
        """Check if position is the goal."""
        return pos == self.goal
    
    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions (4-connected: up, down, left, right)."""
        row, col = pos
        neighbors = []
        
        # Four directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self.is_valid(new_pos):
                neighbors.append(new_pos)
        
        return neighbors
    
    def get_cost(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Get movement cost between two adjacent positions."""
        # Base cost is 1
        # You can modify this for terrain costs (e.g., rough terrain = 2)
        return 1.0
    
    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Calculate Manhattan distance heuristic."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def euclidean_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Calculate Euclidean distance heuristic."""
        return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def reset(self):
        """Reset agent to start position."""
        self.agent_pos = self.start
        self.path = []
        self.visited = set()
        self.expanded = 0
    
    def init_display(self):
        """Initialize Pygame display."""
        pygame.init()
        screen_width = self.width * self.cell_size
        screen_height = self.height * self.cell_size + 100  # Extra space for info
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("RoboMind - Grid World Simulator")
        self.clock = pygame.time.Clock()
        self.running = True
    
    def draw_cell(self, row: int, col: int, color: Tuple[int, int, int]):
        """Draw a single cell."""
        x = col * self.cell_size
        y = row * self.cell_size
        pygame.draw.rect(self.screen, color, 
                        (x, y, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, GRAY, 
                        (x, y, self.cell_size, self.cell_size), 1)
    
    def draw_agent(self):
        """Draw the agent as a blue circle."""
        row, col = self.agent_pos
        center_x = col * self.cell_size + self.cell_size // 2
        center_y = row * self.cell_size + self.cell_size // 2
        pygame.draw.circle(self.screen, BLUE, 
                          (center_x, center_y), 
                          self.cell_size // 3)
    
    def draw_text(self, text: str, pos: Tuple[int, int], size: int = 24):
        """Draw text on screen."""
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, BLACK)
        self.screen.blit(text_surface, pos)
    
    def render(self):
        """Render the current state of the grid."""
        if not self.running:
            return
        
        # Fill background
        self.screen.fill(WHITE)
        
        # Draw grid cells
        for row in range(self.height):
            for col in range(self.width):
                pos = (row, col)
                
                # Determine color based on cell type
                if pos == self.start:
                    color = GREEN
                elif pos == self.goal:
                    color = RED
                elif pos in self.visited:
                    color = (200, 230, 255)  # Light blue for visited
                elif pos in self.path:
                    color = YELLOW
                elif self.grid[row][col] == OBSTACLE:
                    color = BLACK
                elif self.grid[row][col] == UNCERTAIN:
                    color = ORANGE
                else:
                    color = WHITE
                
                self.draw_cell(row, col, color)
        
        # Draw agent
        self.draw_agent()
        
        # Draw info panel
        info_y = self.height * self.cell_size + 10
        self.draw_text(f"Position: {self.agent_pos}", (10, info_y), 20)
        self.draw_text(f"Goal: {self.goal}", (10, info_y + 25), 20)
        self.draw_text(f"Path Length: {len(self.path)}", (10, info_y + 50), 20)
        self.draw_text(f"Expanded Nodes: {self.expanded}", (250, info_y + 25), 20)
        
        # Update display
        pygame.display.flip()
        self.clock.tick(60)  # 60 FPS
    
    def handle_events(self) -> bool:
        """Handle Pygame events. Returns False if window is closed."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return False
            elif event.type == pygame.KEYDOWN:
                # Manual control for testing
                if event.key == pygame.K_UP:
                    new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                    if self.is_valid(new_pos):
                        self.agent_pos = new_pos
                elif event.key == pygame.K_DOWN:
                    new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                    if self.is_valid(new_pos):
                        self.agent_pos = new_pos
                elif event.key == pygame.K_LEFT:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                    if self.is_valid(new_pos):
                        self.agent_pos = new_pos
                elif event.key == pygame.K_RIGHT:
                    new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                    if self.is_valid(new_pos):
                        self.agent_pos = new_pos
                elif event.key == pygame.K_r:
                    self.reset()
        
        return True
    
    def close(self):
        """Close the display."""
        if self.running:
            pygame.quit()
            self.running = False


def demo():
    """Run a simple demo of the environment."""
    # Create a small grid world
    env = GridWorld(width=10, height=10, cell_size=60)
    
    # Add some obstacles
    env.add_obstacle(2, 2)
    env.add_obstacle(2, 3)
    env.add_obstacle(2, 4)
    env.add_obstacle(5, 5)
    env.add_obstacle(6, 5)
    env.add_obstacle(7, 5)
    
    # Set start and goal
    env.start = (1, 1)
    env.goal = (8, 8)
    env.agent_pos = env.start
    
    # Initialize display
    env.init_display()
    
    print("=== RoboMind Environment Demo ===")
    print("Use arrow keys to move the agent")
    print("Press 'R' to reset")
    print("Close window to exit")
    
    # Main loop
    while env.running:
        if not env.handle_events():
            break
        env.render()
    
    env.close()
    print("Demo ended!")


if __name__ == "__main__":
    demo()

