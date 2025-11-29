"""
Logic Agent - RoboMind Project
SE444 - Artificial Intelligence Course Project

TODO: Implement logic-based reasoning agent
Phase 2 of the project (Week 3-4)
"""

import sys
import os
from typing import Tuple, List, Optional

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from environment import GridWorld
from ai_core.knowledge_base import KnowledgeBase


class LogicAgent:
    """
    An agent that uses propositional logic to reason about the world.
    """
    
    def __init__(self, environment: GridWorld):
        """Initialize the logic agent."""
        self.env = environment
        self.kb = KnowledgeBase()
        self.position = environment.start
        self.visited_positions = set()
        self.setup_rules()
        
    def setup_rules(self):
        """Set up the initial inference rules for the agent."""
        # Basic movement rules
        self.kb.add_rule(["At(X,Y)", "Free(X+1,Y)"], "CanMoveDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Free(X-1,Y)"], "CanMoveUp(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Free(X,Y+1)"], "CanMoveRight(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Free(X,Y-1)"], "CanMoveLeft(X,Y)")
        
        # Goal direction rules
        self.kb.add_rule(["At(X,Y)", "Goal(Xg,Yg)", "Xg > X", "CanMoveDown(X,Y)"], "ShouldMoveDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(Xg,Yg)", "Xg < X", "CanMoveUp(X,Y)"], "ShouldMoveUp(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(Xg,Yg)", "Yg > Y", "CanMoveRight(X,Y)"], "ShouldMoveRight(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(Xg,Yg)", "Yg < Y", "CanMoveLeft(X,Y)"], "ShouldMoveLeft(X,Y)")
        
        # Exploration rules (when goal direction is blocked)
        self.kb.add_rule(["At(X,Y)", "CanMoveUp(X,Y)", "NotVisited(X-1,Y)"], "ExploreUp(X,Y)")
        self.kb.add_rule(["At(X,Y)", "CanMoveDown(X,Y)", "NotVisited(X+1,Y)"], "ExploreDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "CanMoveLeft(X,Y)", "NotVisited(X,Y-1)"], "ExploreLeft(X,Y)")
        self.kb.add_rule(["At(X,Y)", "CanMoveRight(X,Y)", "NotVisited(X,Y+1)"], "ExploreRight(X,Y)")
        
        # Safety rules
        self.kb.add_rule(["Visited(X,Y)"], "Safe(X,Y)")
        self.kb.add_rule(["Safe(X,Y)", "Free(X,Y)"], "CanRest(X,Y)")
    
    def perceive(self):
        """Perceive the environment and update knowledge base."""
        row, col = self.position
        goal_row, goal_col = self.env.goal
        
        # Clear previous position facts
        self.kb.clear_facts()
        
        # Add current position
        self.kb.tell(f"At({row},{col})")
        self.kb.tell(f"Goal({goal_row},{goal_col})")
        self.visited_positions.add(self.position)
        
        # Add visited facts
        for pos in self.visited_positions:
            r, c = pos
            self.kb.tell(f"Visited({r},{c})")
        
        # Check all four directions
        directions = [
            (-1, 0, "Up"), (1, 0, "Down"), 
            (0, -1, "Left"), (0, 1, "Right")
        ]
        
        for dr, dc, direction in directions:
            new_pos = (row + dr, col + dc)
            new_row, new_col = new_pos
            
            # Check if position is free
            if self.env.is_valid(new_pos):
                self.kb.tell(f"Free({new_row},{new_col})")
                if new_pos not in self.visited_positions:
                    self.kb.tell(f"NotVisited({new_row},{new_col})")
            else:
                self.kb.tell(f"Obstacle({new_row},{new_col})")
        
        # Perform inference
        self.kb.infer()
    
    def reason(self) -> Optional[str]:
        """Use logic inference to make decisions."""
        row, col = self.position
        
        # Check inference results in priority order
        queries = [
            (f"ShouldMoveUp({row},{col})", "move_up"),
            (f"ShouldMoveDown({row},{col})", "move_down"), 
            (f"ShouldMoveLeft({row},{col})", "move_left"),
            (f"ShouldMoveRight({row},{col})", "move_right"),
            (f"ExploreUp({row},{col})", "move_up"),
            (f"ExploreDown({row},{col})", "move_down"),
            (f"ExploreLeft({row},{col})", "move_left"),
            (f"ExploreRight({row},{col})", "move_right"),
            (f"CanMoveUp({row},{col})", "move_up"),
            (f"CanMoveDown({row},{col})", "move_down"),
            (f"CanMoveLeft({row},{col})", "move_left"),
            (f"CanMoveRight({row},{col})", "move_right")
        ]
        
        for query, action in queries:
            if self.kb.ask(query):
                return action
        
        return None
    
    def act(self) -> Tuple[bool, str]:
        """
        Decide and execute next action.
        
        Returns:
            (success, action_description)
        """
        self.perceive()
        
        action = self.reason()
        if action is None:
            return False, "No valid action found"
        
        # Execute the action
        row, col = self.position
        if action == "move_up":
            new_pos = (row - 1, col)
        elif action == "move_down":
            new_pos = (row + 1, col)
        elif action == "move_left":
            new_pos = (row, col - 1)
        elif action == "move_right":
            new_pos = (row, col + 1)
        else:
            return False, f"Unknown action: {action}"
        
        if self.env.is_valid(new_pos):
            self.position = new_pos
            return True, f"Moved {action.replace('move_', '')} to {new_pos}"
        else:
            return False, f"Cannot move {action.replace('move_', '')} to {new_pos}"
    
    def run_to_goal(self, max_steps: int = 100) -> Tuple[bool, int, List[str]]:
        """
        Run the agent until it reaches goal or max steps.
        
        Returns:
            (success, steps_taken, path_history)
        """
        path_history = []
        steps = 0
        
        while steps < max_steps and self.position != self.env.goal:
            success, description = self.act()
            path_history.append(description)
            
            if not success:
                path_history.append("Stuck - no valid moves")
                break
                
            steps += 1
        
        success = self.position == self.env.goal
        return success, steps, path_history
    
    def get_knowledge_summary(self) -> dict:
        """Get summary of current knowledge state."""
        return {
            "position": self.position,
            "visited": len(self.visited_positions),
            "facts": len(self.kb.get_facts()),
            "rules": len(self.kb.get_rules())
        }


# ============================================================================
# Testing Code
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  Testing Logic Agent")
    print("=" * 60 + "\n")
    
    # Create environment
    env = GridWorld(width=5, height=5)
    env.start = (0, 0)
    env.goal = (4, 4)
    
    # Create agent
    agent = LogicAgent(env)
    
    print("Initial knowledge summary:")
    print(agent.get_knowledge_summary())
    
    print("\nPerceiving environment...")
    agent.perceive()
    
    print("\nAfter perception:")
    print(agent.get_knowledge_summary())
    
    print("\nTesting reasoning...")
    action = agent.reason()
    print(f"Recommended action: {action}")
    
    print("\nTesting one action...")
    success, description = agent.act()
    print(f"Action result: {success} - {description}")
    
    print("\nCurrent knowledge:")
    print(agent.get_knowledge_summary())
    
    print("\n✅ Logic Agent is working!")
