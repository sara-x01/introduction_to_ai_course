"""
Logic Agent - RoboMind Project
SE444 - Artificial Intelligence Course Project

Enhanced agent that uses logical reasoning for decision making.
Phase 2 of the project (Week 3-4)
"""

import sys
import os
from typing import Tuple, List, Optional, Set

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from environment import GridWorld
from ai_core.knowledge_base import KnowledgeBase


class LogicAgent:
    """
    An agent that uses propositional logic to reason about the world.
    Enhanced with proper grid world reasoning.
    """
    
    def __init__(self, environment: GridWorld):
        """Initialize the logic agent."""
        self.env = environment
        self.kb = KnowledgeBase()
        self.position = environment.start
        self.visited_positions: Set[Tuple[int, int]] = set([self.position])
        self.safe_positions: Set[Tuple[int, int]] = set([self.position])
        self.obstacle_positions: Set[Tuple[int, int]] = set()
        self.setup_rules()
        
    def setup_rules(self):
        """Set up the inference rules for grid world navigation."""
        # Clear any existing rules
        self.kb.rules.clear()
        
        # Basic safety rules
        self.kb.add_rule(["Visited(X,Y)"], "Safe(X,Y)")
        self.kb.add_rule(["Free(X,Y)"], "Safe(X,Y)")
        
        # Movement capability rules
        self.kb.add_rule(["At(X,Y)", "Safe(X+1,Y)"], "CanMoveDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Safe(X-1,Y)"], "CanMoveUp(X,Y)") 
        self.kb.add_rule(["At(X,Y)", "Safe(X,Y+1)"], "CanMoveRight(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Safe(X,Y-1)"], "CanMoveLeft(X,Y)")
        
        # Goal proximity rules
        self.kb.add_rule(["At(X,Y)", "Goal(X+1,Y)", "CanMoveDown(X,Y)"], "PriorityDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(X-1,Y)", "CanMoveUp(X,Y)"], "PriorityUp(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(X,Y+1)", "CanMoveRight(X,Y)"], "PriorityRight(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(X,Y-1)", "CanMoveLeft(X,Y)"], "PriorityLeft(X,Y)")
        
        # Exploration rules for unvisited safe cells
        self.kb.add_rule(["CanMoveRight(X,Y)", "NotVisited(X,Y+1)"], "ExploreRight(X,Y)")
        self.kb.add_rule(["CanMoveDown(X,Y)", "NotVisited(X+1,Y)"], "ExploreDown(X,Y)")
        self.kb.add_rule(["CanMoveUp(X,Y)", "NotVisited(X-1,Y)"], "ExploreUp(X,Y)")
        self.kb.add_rule(["CanMoveLeft(X,Y)", "NotVisited(X,Y-1)"], "ExploreLeft(X,Y)")
        
        # General goal direction rules (when not adjacent)
        self.kb.add_rule(["At(X,Y)", "Goal(GX,GY)", "GX > X", "CanMoveDown(X,Y)"], "GoalDirectionDown(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(GX,GY)", "GY > Y", "CanMoveRight(X,Y)"], "GoalDirectionRight(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(GX,GY)", "GX < X", "CanMoveUp(X,Y)"], "GoalDirectionUp(X,Y)")
        self.kb.add_rule(["At(X,Y)", "Goal(GX,GY)", "GY < Y", "CanMoveLeft(X,Y)"], "GoalDirectionLeft(X,Y)")
        
        # Final decision rules - ORDER MATTERS (higher priority first)
        self.kb.add_rule(["PriorityRight(X,Y)"], "MoveRight")
        self.kb.add_rule(["PriorityDown(X,Y)"], "MoveDown")
        self.kb.add_rule(["PriorityUp(X,Y)"], "MoveUp")
        self.kb.add_rule(["PriorityLeft(X,Y)"], "MoveLeft")
        
        self.kb.add_rule(["ExploreRight(X,Y)"], "MoveRight")
        self.kb.add_rule(["ExploreDown(X,Y)"], "MoveDown")
        self.kb.add_rule(["ExploreUp(X,Y)"], "MoveUp")
        self.kb.add_rule(["ExploreLeft(X,Y)"], "MoveLeft")
        
        self.kb.add_rule(["GoalDirectionRight(X,Y)"], "MoveRight")
        self.kb.add_rule(["GoalDirectionDown(X,Y)"], "MoveDown")
        self.kb.add_rule(["GoalDirectionUp(X,Y)"], "MoveUp")
        self.kb.add_rule(["GoalDirectionLeft(X,Y)"], "MoveLeft")
        
        self.kb.add_rule(["CanMoveRight(X,Y)"], "MoveRight")
        self.kb.add_rule(["CanMoveDown(X,Y)"], "MoveDown")
        self.kb.add_rule(["CanMoveUp(X,Y)"], "MoveUp")
        self.kb.add_rule(["CanMoveLeft(X,Y)"], "MoveLeft")
    
    def perceive(self):
        """Perceive the environment and update knowledge base with current state."""
        row, col = self.position
        goal_row, goal_col = self.env.goal
        
        # Clear facts but keep rules
        self.kb.clear_facts()
        
        # Add current position facts
        self.kb.tell(f"At({row},{col})")
        self.kb.tell(f"Visited({row},{col})")
        
        # Add goal information
        self.kb.tell(f"Goal({goal_row},{goal_col})")
        
        # Mark current position as visited
        self.visited_positions.add(self.position)
        
        # Check all four directions
        directions = [
            (-1, 0, "Up"), (1, 0, "Down"), 
            (0, -1, "Left"), (0, 1, "Right")
        ]
        
        for dr, dc, direction in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)
            
            if self.env.is_valid(new_pos):
                # Cell is free and safe
                self.kb.tell(f"Free({new_row},{new_col})")
                self.kb.tell(f"Safe({new_row},{new_col})")
                
                if new_pos not in self.visited_positions:
                    self.kb.tell(f"NotVisited({new_row},{new_col})")
            else:
                # Cell is obstacle
                self.kb.tell(f"Obstacle({new_row},{new_col})")
                self.obstacle_positions.add(new_pos)
        
        # Add comparison facts for goal direction
        if goal_row > row:
            self.kb.tell("GX > X")
        elif goal_row < row:
            self.kb.tell("GX < X")
            
        if goal_col > col:
            self.kb.tell("GY > Y")
        elif goal_col < col:
            self.kb.tell("GY < Y")
        
        # Perform inference
        self.kb.infer()
    
    def reason(self) -> Optional[str]:
        """Use logic inference to make movement decisions."""
        # Check for movement decisions (these don't need position parameters)
        decision_queries = ["MoveRight", "MoveDown", "MoveUp", "MoveLeft"]
        
        for query in decision_queries:
            if self.kb.ask(query):
                return query.replace("Move", "").lower()
        
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
            return False, "No valid action found through reasoning"
        
        row, col = self.position
        
        # Calculate new position based on action
        if action == "up":
            new_pos = (row - 1, col)
        elif action == "down":
            new_pos = (row + 1, col)
        elif action == "left":
            new_pos = (row, col - 1)
        elif action == "right":
            new_pos = (row, col + 1)
        else:
            return False, f"Unknown action: {action}"
        
        # Validate and execute move
        if self.env.is_valid(new_pos):
            old_position = self.position
            self.position = new_pos
            self.visited_positions.add(new_pos)
            self.safe_positions.add(new_pos)
            return True, f"Moved {action} from {old_position} to {new_pos}"
        else:
            return False, f"Cannot move {action} to blocked position {new_pos}"
    
    def run_to_goal(self, max_steps: int = 100) -> Tuple[bool, int, List[str]]:
        """
        Run the agent until it reaches goal or max steps.
        
        Returns:
            (success, steps_taken, path_history)
        """
        self.position = self.env.start  # Reset position
        self.visited_positions = set([self.position])
        self.safe_positions = set([self.position])
        self.obstacle_positions = set()
        
        path_history = []
        steps = 0
        
        print(f"Starting at {self.position}, Goal: {self.env.goal}")
        
        while steps < max_steps and self.position != self.env.goal:
            success, description = self.act()
            path_history.append(description)
            
            if not success:
                path_history.append("Stuck - no valid moves found through reasoning")
                break
                
            steps += 1
            
            # Debug output every 10 steps
            if steps % 10 == 0:
                print(f"Step {steps}: {self.position}")
        
        success = self.position == self.env.goal
        return success, steps, path_history
    
    def get_knowledge_summary(self) -> dict:
        """Get summary of current knowledge state."""
        return {
            "position": self.position,
            "goal": self.env.goal,
            "visited_positions": len(self.visited_positions),
            "safe_positions": len(self.safe_positions),
            "obstacle_positions": len(self.obstacle_positions),
            "facts": len(self.kb.get_facts()),
            "rules": len(self.kb.get_rules())
        }
    
    def print_reasoning_debug(self):
        """Print debug information about current reasoning state."""
        print("\n" + "="*50)
        print("REASONING DEBUG INFO")
        print("="*50)
        print(f"Position: {self.position}")
        print(f"Goal: {self.env.goal}")
        
        # Check what moves are possible
        row, col = self.position
        moves = []
        for dr, dc, direction in [(-1,0,"Up"), (1,0,"Down"), (0,-1,"Left"), (0,1,"Right")]:
            if self.env.is_valid((row+dr, col+dc)):
                moves.append(direction)
        
        print(f"Possible moves: {moves}")
        print(f"Visited positions: {len(self.visited_positions)}")
        
        # Check what the KB knows
        print("\nKnowledge Base Facts:")
        facts = sorted(self.kb.get_facts())
        for fact in facts[:10]:  # Show first 10 facts
            print(f"  {fact}")
        if len(facts) > 10:
            print(f"  ... and {len(facts) - 10} more facts")
        
        print(f"Decision: {self.reason()}")
        print("="*50)


# ============================================================================
# Enhanced Testing Code
# ============================================================================

def test_with_map(map_file: str, max_steps: int = 50):
    """Test the logic agent with a specific map."""
    print(f"\n🧪 Testing with map: {map_file}")
    print("=" * 60)
    
    env = GridWorld()
    env.load_map(map_file)
    
    agent = LogicAgent(env)
    
    print(f"Map: {env.width}x{env.height}")
    print(f"Start: {env.start}, Goal: {env.goal}")
    print(f"Obstacles: {(env.grid == 1).sum()}")
    
    success, steps, history = agent.run_to_goal(max_steps)
    
    print(f"\nResults:")
    print(f"  Goal reached: {'✅ YES' if success else '❌ NO'}")
    print(f"  Steps taken: {steps}")
    print(f"  Final position: {agent.position}")
    
    if history:
        print(f"\nFirst 10 actions:")
        for i, action in enumerate(history[:10]):
            print(f"  {i+1}: {action}")
    
    if not success and steps >= max_steps:
        print(f"\n⚠️  Hit step limit ({max_steps})")
    
    # Show knowledge summary
    summary = agent.get_knowledge_summary()
    print(f"\nKnowledge Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    return success, steps


if __name__ == "__main__":
    print("=" * 60)
    print("  Testing Enhanced Logic Agent")
    print("=" * 60)
    
    # Test with simple map
    test_with_map("maps/simple.txt", max_steps=30)
    
    # Test with maze map (more challenging)
    test_with_map("maps/maze.txt", max_steps=50)
    
    print("\n" + "=" * 60)
    print("  Logic Agent Testing Complete!")
    print("=" * 60)
