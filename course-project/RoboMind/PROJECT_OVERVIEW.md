# 📚 RoboMind Project Overview (For Instructors)

## Project Summary

**RoboMind** is a Python-based educational project where students build a rational AI agent that navigates a 2D grid world. The project is designed to integrate three key AI reasoning paradigms taught in SE444:

1. **Search Algorithms** (Lectures 3-5)
2. **Logical Reasoning** (Lecture 7)
3. **Probabilistic Inference** (Lecture 10)

## Key Features

✅ **Progressive Difficulty**: 4 phases, each building on the previous
✅ **Starter Code Provided**: Environment and skeleton code ready
✅ **Visual & Interactive**: Pygame-based visualization
✅ **Minimal Dependencies**: Only pygame, numpy, matplotlib
✅ **Self-Contained Testing**: Built-in test modes
✅ **Clear Documentation**: README, QUICKSTART, inline comments

## Project Phases

### Phase 1: Search Algorithms (Weeks 1-2)
**Students Implement:**
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search with heuristics

**Files to Modify:**
- `ai_core/search_algorithms.py`

**Test Command:**
```bash
python main.py --test-search
```

**Learning Outcomes:**
- Understand frontier/explored distinction
- Implement priority queues correctly
- Choose appropriate heuristics
- Analyze algorithm efficiency

---

### Phase 2: Logic Reasoning (Weeks 3-4)
**Students Implement:**
- Propositional knowledge base
- Forward chaining inference
- Rule-based decision making

**Files to Modify:**
- `ai_core/knowledge_base.py`
- `agents/logic_agent.py`

**Test Command:**
```bash
python main.py --test-logic
```

**Learning Outcomes:**
- Represent knowledge as propositions
- Apply inference rules automatically
- Reason about partial information
- Design effective rule sets

---

### Phase 3: Probabilistic Reasoning (Weeks 5-6)
**Students Implement:**
- Bayes' rule for belief updates
- Sensor model with noise
- Belief map maintenance

**Files to Modify:**
- `ai_core/bayes_reasoning.py`
- `agents/probabilistic_agent.py`

**Test Command:**
```bash
python main.py --test-probability
```

**Learning Outcomes:**
- Apply Bayes' rule correctly
- Handle sensor uncertainty
- Update beliefs over time
- Visualize probability distributions

---

### Phase 4: Hybrid Integration (Weeks 7-8)
**Students Implement:**
- Integrated decision-making
- Strategy switching (search/logic/probability)
- Complete rational agent

**Files to Modify:**
- `agents/hybrid_agent.py`

**Test Command:**
```bash
python main.py --test-hybrid
```

**Learning Outcomes:**
- Integrate multiple reasoning techniques
- Make rational decisions under uncertainty
- Balance exploration vs exploitation
- Design complete AI systems

---

## What's Provided (Starter Code)

### ✅ Complete Files (Students Don't Modify)

1. **`environment.py`** - Full grid world simulator
   - Pygame visualization
   - Map loading
   - Movement validation
   - Neighbor generation
   - Distance heuristics

2. **`main.py`** - Testing framework
   - Command-line interface
   - Multiple test modes
   - Agent integration
   - Results display

3. **`utils/visualize.py`** - Plotting helpers (optional)
4. **`utils/metrics.py`** - Performance tracking (optional)
5. **`maps/*.txt`** - Test maps (simple, maze, uncertain)

### 🚧 Skeleton Files (Students Implement)

1. **`ai_core/search_algorithms.py`**
   - Functions: `bfs()`, `ucs()`, `astar()`, `reconstruct_path()`
   - Extensive comments and hints provided

2. **`ai_core/knowledge_base.py`**
   - Class: `KnowledgeBase`
   - Methods: `tell()`, `ask()`, `infer()`

3. **`ai_core/bayes_reasoning.py`**
   - Functions: `bayes_update()`, `compute_evidence()`, `update_belief_map()`

4. **`agents/search_agent.py`**
   - Class: `SearchAgent`
   - Uses search algorithms to navigate

5. **`agents/logic_agent.py`**
   - Class: `LogicAgent`
   - Uses KB for reasoning

6. **`agents/probabilistic_agent.py`**
   - Class: `ProbabilisticAgent`
   - Uses Bayes for uncertainty

7. **`agents/hybrid_agent.py`**
   - Class: `HybridAgent`
   - Integrates all techniques

---

## Grading Rubric (100 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Phase 1: Search** | 25 | BFS (8), UCS (8), A* (9) |
| **Phase 2: Logic** | 20 | KB implementation (10), Inference (10) |
| **Phase 3: Probability** | 20 | Bayes' rule (10), Belief updates (10) |
| **Phase 4: Integration** | 20 | Hybrid agent (15), Rationality (5) |
| **Report** | 10 | Analysis, results, reflection |
| **Code Quality** | 5 | Comments, structure, style |

### Detailed Criteria:

**Search Algorithms (25 pts):**
- ✓ BFS finds shortest path (8 pts)
- ✓ UCS finds lowest-cost path (8 pts)
- ✓ A* is optimal and efficient (9 pts)

**Logic Reasoning (20 pts):**
- ✓ KB stores facts and rules (5 pts)
- ✓ Forward chaining works (10 pts)
- ✓ Agent makes logical decisions (5 pts)

**Probabilistic Reasoning (20 pts):**
- ✓ Bayes' rule implemented correctly (5 pts)
- ✓ Belief map updates properly (10 pts)
- ✓ Agent handles sensor noise (5 pts)

**Hybrid Integration (20 pts):**
- ✓ All components work together (10 pts)
- ✓ Appropriate strategy selection (5 pts)
- ✓ Demonstrates rational behavior (5 pts)

**Report (10 pts):**
- ✓ Clear explanation of approach (3 pts)
- ✓ Experimental results with analysis (4 pts)
- ✓ Reflection and discussion (3 pts)

**Code Quality (5 pts):**
- ✓ Well-commented code (2 pts)
- ✓ Proper structure and naming (2 pts)
- ✓ Follows Python conventions (1 pt)

---

## Timeline & Milestones

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 1-2 | Phase 1 | Search algorithms working |
| 3-4 | Phase 2 | Logic agent functional |
| 5-6 | Phase 3 | Probabilistic agent complete |
| 7-8 | Phase 4 | Hybrid agent integrated |
| 9 | Report | Final submission |
| 10 | Presentation | Demo + Q&A |

---

## Installation & Setup

### Prerequisites:
- Python 3.8+
- pip package manager

### Setup:
```bash
cd RoboMind
pip install -r requirements.txt
python main.py --demo
```

### Testing:
```bash
# Test individual components
python ai_core/search_algorithms.py
python ai_core/knowledge_base.py
python ai_core/bayes_reasoning.py

# Test agents
python main.py --test-search
python main.py --test-logic
python main.py --test-probability
python main.py --test-hybrid
```

---

## Common Student Questions

**Q: Can we use external libraries?**
A: Only those in `requirements.txt`. No AI/ML libraries that solve the problem for you.

**Q: Can we modify `environment.py`?**
A: No, work with the provided API. Grading uses original environment.

**Q: How detailed should comments be?**
A: Explain your reasoning, especially for complex algorithms.

**Q: Can we work in pairs?**
A: No, this is an individual project. Discuss concepts, but write your own code.

**Q: What if we can't finish all phases?**
A: Submit what you have. Partial credit given for each phase.

---

## Extension Ideas (Bonus/Advanced Students)

1. **Bidirectional Search** (+5 pts)
2. **First-Order Logic** with predicates (+10 pts)
3. **Particle Filter** for localization (+10 pts)
4. **Multi-Agent System** (+15 pts)
5. **Reinforcement Learning** (+20 pts)

---

## Support Materials

- 📁 Starter code: Complete skeleton with TODOs
- 📖 README.md: Full project description
- 🚀 QUICKSTART.md: 5-minute getting started
- 💻 Test maps: Simple, maze, uncertain scenarios
- 🧪 Built-in tests: Automated testing framework

---

## Instructor Notes

### Estimated Workload:
- **Student Time:** 40-50 hours total (5-6 hours/week)
- **Grading Time:** 30-45 minutes per submission

### Difficulty Level:
- **Phase 1:** Easy-Medium (suitable for beginners)
- **Phase 2:** Medium
- **Phase 3:** Medium-Hard
- **Phase 4:** Hard (requires integration skills)

### Keys to Success:
1. Emphasize **incremental development**
2. Encourage **testing each phase**
3. Provide **office hours** for debugging
4. Share **common pitfalls** early
5. Allow **resubmission** of Phase 1 (builds confidence)

---

## Reusability

This project can be reused semester after semester:
- Change maps and scenarios
- Adjust parameters and constraints
- Add new extensions
- Update grading rubric

---

**For questions or support:** [Instructor Email]

**Project Repository:** `/se444/course-project/RoboMind/`

