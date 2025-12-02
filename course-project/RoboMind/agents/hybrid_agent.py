"""
Hybrid Agent - RoboMind Project
SE444 - Artificial Intelligence Course Project

Phase 4: Hybrid Integration
Integrates Search + Logic + Probabilistic Reasoning
"""

from environment import GridWorld
from agents.search_agent import SearchAgent
from ai_core.knowledge_base import KnowledgeBase
from ai_core.bayes_reasoning import bayes_update  # placeholder import


class HybridAgent:
    """
    A rational agent that integrates search, logic, and probabilistic reasoning.
    """

    def __init__(self, environment: GridWorld):
        """Initialize the hybrid agent."""
        self.env = environment

        # --- Components ---
        self.search_agent = SearchAgent(environment)
        self.kb = KnowledgeBase()

        # --- Internal State ---
        self.beliefs = {}            # Probabilistic beliefs (e.g., cell -> P(safe))
        self.position = self.env.get_agent_position()
        self.goal = self.env.get_goal_position()
        self.last_observation = None

        # --- Parameters ---
        self.uncertainty_threshold = 0.6  # if below, use probability reasoning

    # ============================================================
    # PHASE 4 STRUCTURE — can be run before Phase 3 is implemented
    # ============================================================

    def perceive(self):
        """
        Get sensor readings from environment.
        May be noisy — for now, simulate a perfect or placeholder sensor.
        """
        try:
            observation = self.env.get_sensor_data(self.position)
        except AttributeError:
            # If env doesn't have noisy sensors yet, mock simple perception
            observation = {"around": self.env.get_neighbors(self.position)}
        self.last_observation = observation
        return observation

    def reason(self):
        """
        Use logic to infer safe or unsafe cells.
        This can be run even without probabilistic reasoning.
        """
        # Example: simple inference rule
        # (You can expand these rules later)
        if self.last_observation:
            for cell, info in self.last_observation["around"].items():
                if info == "obstacle":
                    self.kb.tell(f"Obstacle({cell})")
                else:
                    self.kb.tell(f"Safe({cell})")

        inferred_safe = self.kb.ask("Safe")
        return inferred_safe

    def update_beliefs(self):
        """
        Use Bayesian inference to handle uncertain sensor readings.
        Stub: works even before Phase 3 is done.
        """
        if not self.last_observation:
            return self.beliefs

        # Placeholder — assign uniform beliefs if not using bayes_update yet
        for cell, info in self.last_observation["around"].items():
            if cell not in self.beliefs:
                self.beliefs[cell] = 0.5  # unknown cells start uncertain

        # Once Phase 3 is complete, plug in:
        # self.beliefs = bayes_update(self.beliefs, self.last_observation)
        return self.beliefs

    def plan(self):
        """
        Use search algorithms to plan a path to the goal.
        (Runs even without probabilistic info.)
        """
        path = self.search_agent.plan(start=self.position, goal=self.goal)
        return path

    def act(self):
        """
        Integrate all reasoning techniques to decide next action.

        Strategy:
            1. If goal is visible and path is clear → use search
            2. If uncertain about obstacles → use probability
            3. If need to infer hidden info → use logic
        """
        # --- Perceive environment ---
        observation = self.perceive()

        # --- Update beliefs (stubbed if Phase 3 not ready) ---
        beliefs = self.update_beliefs()

        # --- Logic reasoning ---
        inferred_safe = self.reason()

        # --- Decision logic ---
        if self.goal in inferred_safe:
            print("Goal inferred safe → using search to reach goal.")
            path = self.plan()
            action = path[1] if len(path) > 1 else None
        elif any(p < self.uncertainty_threshold for p in beliefs.values()):
            print("Uncertain environment → using probabilistic reasoning.")
            # Placeholder: pick the cell with highest belief of being safe
            safe_cell = max(beliefs, key=beliefs.get)
            action = safe_cell
        else:
            print("No clear information → exploring logically inferred safe cells.")
            action = inferred_safe[0] if inferred_safe else None

        if action:
            self.position = action
            print(f"Agent moves to {action}")
        else:
            print("No action decided — waiting for more info.")

        return action


# Example usage
if __name__ == "__main__":
    print("Hybrid Agent - combines Search + Logic + Probability")
    print("This is the final phase - integrate everything!")

    # Mock environment (you can replace with actual GridWorld)
    try:
        env = GridWorld("maps/simple.txt")
        agent = HybridAgent(env)
        agent.act()
    except Exception as e:
        print("HybridAgent initialized without full environment for testing.")
        print("Reason:", e)
