# 🤖 RoboMind: Rational Agent Simulation

**SE444 - Artificial Intelligence Course Project**

## 📋 Project Overview

Welcome to RoboMind! In this project, you will build an intelligent agent that navigates a 2D grid world using the AI techniques you've learned in class.

Your agent will use:
- **Search Algorithms** (BFS, UCS, A*) to plan paths
- **Logical Reasoning** to infer safe moves
- **Probabilistic Reasoning** to handle uncertainty

## 🎯 Learning Objectives

By completing this project, you will:
1. Implement and compare classical search algorithms
2. Apply propositional logic for reasoning
3. Use Bayesian inference to handle sensor uncertainty
4. Build a rational agent that integrates multiple reasoning techniques
5. Evaluate and analyze agent performance

## 🏗️ Project Structure

```
RoboMind/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── main.py                     # Main entry point to run simulations
├── environment.py              # Grid world simulator (PROVIDED)
├── agents/
│   ├── search_agent.py         # TODO: Implement search-based agent
│   ├── logic_agent.py          # TODO: Implement logic-based agent
│   ├── probabilistic_agent.py  # TODO: Implement probabilistic agent
│   └── hybrid_agent.py         # TODO: Integrate all techniques
├── ai_core/
│   ├── search_algorithms.py    # TODO: Implement BFS, UCS, A*
│   ├── knowledge_base.py       # TODO: Implement logic KB
│   └── bayes_reasoning.py      # TODO: Implement Bayesian updates
├── utils/
│   ├── visualize.py            # Visualization helpers (PROVIDED)
│   └── metrics.py              # Performance measurement (PROVIDED)
└── maps/
    ├── simple.txt              # Simple test map
    ├── maze.txt                # Complex maze
    └── uncertain.txt           # Map with uncertain areas
```

## 🚀 Getting Started

### Step 1: Setup Environment

1. Install Python 3.8+ (if not already installed)
2. Install required libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Test the Simulator

Run the demo to see the environment:

```bash
python main.py --demo
```

You should see a grid world with:
- 🟩 Green cell: Start position
- 🟥 Red cell: Goal position
- ⬛ Black cells: Obstacles
- ⬜ White cells: Free space

### Step 3: Read the Code

1. **Start with `environment.py`**: Understand how the grid world works
2. **Check `main.py`**: See how agents interact with the environment
3. **Look at agent skeletons**: See what you need to implement

## 📝 Implementation Tasks

### **Phase 1: Search Algorithms (Week 1-2)**

**File**: `ai_core/search_algorithms.py`

Implement three search algorithms:

#### 1.1 Breadth-First Search (BFS)
```python
def bfs(grid, start, goal):
    """
    Find shortest path using BFS.
    
    Args:
        grid: 2D list (0=free, 1=obstacle)
        start: tuple (row, col)
        goal: tuple (row, col)
    
    Returns:
        path: list of (row, col) tuples
        cost: total path cost
        expanded: number of nodes expanded
    """
    # TODO: Implement BFS
    pass
```

#### 1.2 Uniform Cost Search (UCS)
```python
def ucs(grid, start, goal):
    """
    Find lowest cost path using UCS.
    (Movement costs can vary: normal=1, rough=2)
    """
    # TODO: Implement UCS
    pass
```

#### 1.3 A* Search
```python
def astar(grid, start, goal, heuristic='manhattan'):
    """
    Find optimal path using A* with heuristic.
    
    Heuristics:
        - 'manhattan': |x1-x2| + |y1-y2|
        - 'euclidean': sqrt((x1-x2)² + (y1-y2)²)
    """
    # TODO: Implement A*
    pass
```

**Deliverable**: Working search algorithms that can navigate from start to goal.

**Test**: `python main.py --test-search`

---

### **Phase 2: Logic-Based Reasoning (Week 3-4)**

**File**: `ai_core/knowledge_base.py`

Implement a simple knowledge base for logical inference:

```python
class KnowledgeBase:
    def __init__(self):
        self.facts = set()      # Known facts: "Safe(2,3)", "Obstacle(4,5)"
        self.rules = []         # Rules: "If A and B then C"
    
    def tell(self, fact):
        """Add a fact to the KB."""
        # TODO: Implement
        pass
    
    def ask(self, query):
        """Check if query can be inferred."""
        # TODO: Implement
        pass
    
    def infer(self):
        """Apply forward chaining to derive new facts."""
        # TODO: Implement
        pass
```

**Example Rules**:
- "If cell is Free AND Explored → Safe"
- "If cell has Obstacle → NOT Safe"
- "If all neighbors of cell are Safe → Safe to move"

**Deliverable**: Logic agent that reasons about safe moves.

**Test**: `python main.py --test-logic`

---

### **Phase 3: Probabilistic Reasoning (Week 5-6)**

**File**: `ai_core/bayes_reasoning.py`

Implement Bayesian belief updates for uncertain sensor readings:

```python
def bayes_update(prior, likelihood, evidence):
    """
    Update belief using Bayes' rule:
    P(H|E) = P(E|H) * P(H) / P(E)
    
    Args:
        prior: P(Hypothesis) - prior probability
        likelihood: P(Evidence|Hypothesis)
        evidence: P(Evidence)
    
    Returns:
        posterior: P(Hypothesis|Evidence)
    """
    # TODO: Implement Bayes' rule
    pass

def update_belief_map(belief_map, sensor_reading, position):
    """
    Update entire grid belief map based on noisy sensor reading.
    
    Sensor model:
        - 90% accurate: P(reading=obstacle | obstacle=true) = 0.9
        - 10% false positive: P(reading=obstacle | obstacle=false) = 0.1
    """
    # TODO: Implement belief propagation
    pass
```

**Deliverable**: Probabilistic agent that handles sensor noise.

**Test**: `python main.py --test-probability`

---

### **Phase 4: Hybrid Rational Agent (Week 7-8)**

**File**: `agents/hybrid_agent.py`

Integrate all three reasoning techniques:

```python
class HybridAgent:
    def __init__(self, environment):
        self.env = environment
        self.kb = KnowledgeBase()
        self.beliefs = {}  # probability map
        
    def perceive(self):
        """Get sensor readings (may be noisy)."""
        pass
    
    def plan(self):
        """Use search to find path to goal."""
        pass
    
    def reason(self):
        """Use logic to infer safe moves."""
        pass
    
    def update_beliefs(self):
        """Use probability to handle uncertainty."""
        pass
    
    def act(self):
        """Decide and execute next action."""
        # TODO: Integrate search + logic + probability
        pass
```

**Decision Strategy**:
1. If goal is visible and path is clear → use **search**
2. If uncertain about obstacles → use **probability**
3. If need to infer hidden information → use **logic**

**Deliverable**: Complete rational agent.

**Test**: `python main.py --test-hybrid`

---

## 🧪 Evaluation & Experiments

Run comprehensive tests:

```bash
python main.py --experiment all
```

### Metrics to Measure:

| Metric | Description | Goal |
|--------|-------------|------|
| **Path Cost** | Total cost from start to goal | Minimize |
| **Nodes Expanded** | Number of nodes explored | Minimize (efficiency) |
| **Success Rate** | % of runs reaching goal | Maximize |
| **Execution Time** | Time to find solution | Minimize |
| **Belief Accuracy** | Correctness of probability estimates | Maximize |

### Expected Results:

Create a comparison table and plots showing:
1. BFS vs UCS vs A* performance
2. Logic agent decision correctness
3. Probabilistic agent belief convergence
4. Hybrid agent overall performance

## 📊 Final Report Requirements

Submit a PDF report (5-10 pages) including:

### 1. Introduction (10%)
- Project overview
- Your approach summary

### 2. Implementation (40%)
- Search algorithms explanation
- Logic reasoning approach
- Probabilistic inference method
- Hybrid agent integration strategy

### 3. Experiments & Results (30%)
- Performance comparisons (tables + graphs)
- Analysis of results
- Discussion of strengths/weaknesses

### 4. Reflection (20%)
- What makes your agent "rational"?
- Limitations and improvements
- Real-world applications
- Ethical considerations

## 🎓 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Search Algorithms** | 25 | Correctness, efficiency, comparisons |
| **Logic Reasoning** | 20 | Valid inference, rule consistency |
| **Probabilistic Reasoning** | 20 | Correct Bayes updates, belief accuracy |
| **Hybrid Integration** | 20 | Coherent decision-making, rationality |
| **Report & Analysis** | 10 | Clarity, depth, visualizations |
| **Code Quality** | 5 | Comments, structure, readability |
| **TOTAL** | 100 | |

## 💡 Tips for Success

1. **Start Early**: Begin with Phase 1 immediately
2. **Test Incrementally**: Test each function as you write it
3. **Use Print Statements**: Debug by printing intermediate values
4. **Visualize**: Use the provided visualization tools
5. **Ask Questions**: Use office hours and discussion forums
6. **Collaborate Ethically**: Discuss concepts, but write your own code
7. **Document**: Add comments explaining your reasoning

## 🆘 Getting Help

- **Office Hours**: [Schedule TBD]
- **Discussion Forum**: [Link TBD]
- **Email**: [Instructor email]

## 📚 Relevant Lectures

- **Lecture 3**: Search Algorithms (BFS, DFS, UCS, A*)
- **Lecture 7**: Logical Agents & Knowledge Representation
- **Lecture 10**: Uncertainty & Probability Theory
- **Lecture 10.5**: Bayesian Inference (optional advanced topic)

## 🚨 Important Dates

| Milestone | Due Date | Deliverable |
|-----------|----------|-------------|
| Phase 1: Search | Week 3 | Working search algorithms |
| Phase 2: Logic | Week 5 | Logic-based agent |
| Phase 3: Probability | Week 7 | Probabilistic agent |
| Phase 4: Integration | Week 9 | Hybrid agent |
| Final Report | Week 10 | Complete report + code |
| Presentation | Week 11 | 10-min demo + Q&A |

## 🎯 Bonus Challenges (Optional - Extra Credit)

1. **Implement Bidirectional Search** (+5 points)
2. **Add First-Order Logic** with predicates (+10 points)
3. **Implement Particle Filter** for localization (+10 points)
4. **Multi-Agent Coordination** (2+ agents) (+15 points)
5. **Machine Learning Integration** (learn from experience) (+20 points)

---

## ⚖️ Academic Integrity

- You may discuss concepts with classmates
- You **must** write your own code
- Cite any external resources or libraries used
- Do not share complete solutions
- Plagiarism will result in zero grade + disciplinary action

---

## 🏆 Success Story

> "This project helped me understand how AI agents actually work. Seeing my agent navigate and reason through uncertainty was amazing!" 
> — Former SE444 Student

---

**Good luck! Build something intelligent! 🚀🤖**

*Prof. [Your Name]*  
*SE444 - Artificial Intelligence*  
*[University Name]*

