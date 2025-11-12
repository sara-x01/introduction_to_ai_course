# 🚀 RoboMind Quick Start Guide

**Get up and running in 5 minutes!**

## Step 1: Install Python & Dependencies (2 minutes)

Make sure you have Python 3.8+ installed:

```bash
python --version
```

Install required libraries:

```bash
pip install -r requirements.txt
```

## Step 2: Test the Environment (1 minute)

Run the demo to see the grid world:

```bash
python main.py --demo
```

You should see a window with a grid. Use arrow keys to move the agent!

## Step 3: Understand the Project Structure (2 minutes)

```
RoboMind/
├── main.py                    ← Run this to test
├── environment.py             ← Grid world (don't modify)
├── agents/                    ← Your agent implementations
│   ├── search_agent.py       ← Phase 1: START HERE
│   ├── logic_agent.py        ← Phase 2
│   ├── probabilistic_agent.py ← Phase 3
│   └── hybrid_agent.py       ← Phase 4: Final integration
└── ai_core/                   ← Core AI algorithms
    ├── search_algorithms.py  ← Phase 1: IMPLEMENT THESE
    ├── knowledge_base.py     ← Phase 2
    └── bayes_reasoning.py    ← Phase 3
```

## Step 4: Start Phase 1 - Search Algorithms

Open `ai_core/search_algorithms.py` and implement BFS:

```python
def bfs(env, start, goal):
    # TODO: Your code here
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    # ... rest of BFS
```

Test your implementation:

```bash
python main.py --test-search
```

## Step 5: Iterative Development

1. **Implement BFS** first (simplest)
2. Test it: `python ai_core/search_algorithms.py`
3. **Then UCS** (adds costs)
4. **Finally A*** (adds heuristics)
5. Compare all three!

## 📖 Key Files to Read First

1. **`README.md`** - Full project description
2. **`environment.py`** - Understand the grid world API
3. **`ai_core/search_algorithms.py`** - See what to implement

## 🎯 Your First Goal

**Complete Phase 1 (Week 1-2):**
- Implement BFS, UCS, and A*
- Get all tests passing
- Compare performance

**Success Criteria:**
```bash
$ python main.py --test-search

Testing BFS...
  ✓ Path found! Length: 18, Cost: 17, Expanded: 42

Testing UCS...
  ✓ Path found! Length: 18, Cost: 17, Expanded: 38

Testing A* (Manhattan)...
  ✓ Path found! Length: 18, Cost: 17, Expanded: 24
```

## 🆘 Getting Help

**Common Issues:**

**Q: Import errors?**
```bash
# Make sure you're in the RoboMind directory
cd RoboMind
python main.py --demo
```

**Q: Pygame not working?**
```bash
# Reinstall pygame
pip install --upgrade pygame
```

**Q: Don't know where to start?**
1. Read the BFS algorithm hints in `search_algorithms.py`
2. Look at lecture notes on BFS
3. Start with the queue and visited set
4. Add parent pointers for path reconstruction

## 💡 Pro Tips

1. **Test incrementally**: Don't write all code at once
2. **Use print statements**: Debug by printing variables
3. **Draw on paper**: Sketch how BFS/UCS/A* work
4. **Start simple**: Test on small grids first
5. **Compare with classmates**: Discuss approaches (but write your own code!)

## 📚 Related Lectures

- **Lecture 3**: Search Algorithms
  - BFS, DFS, UCS, A*
  - Heuristics and admissibility

## 🎓 Deliverables Timeline

| Week | Deliverable | Test Command |
|------|-------------|--------------|
| 1-2  | Search Algorithms | `python main.py --test-search` |
| 3-4  | Logic Agent | `python main.py --test-logic` |
| 5-6  | Probabilistic Agent | `python main.py --test-probability` |
| 7-8  | Hybrid Agent | `python main.py --test-hybrid` |
| 9    | Final Report | Submit PDF + code |

---

**Now get started! Open `ai_core/search_algorithms.py` and start coding! 🚀**

Questions? Check `README.md` or ask in office hours!

