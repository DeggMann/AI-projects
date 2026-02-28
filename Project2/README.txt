
CAP4630 Project 2 – Path Finder

This project implements pathfinding algorithms on a 50x50 grid with obstacles (enclosures) 
and variable terrain costs (turfs). It compares four search algorithms:
  - BFS (Breadth-First Search): Uninformed, guarantees shortest path
  - DFS (Depth-First Search): Uninformed, explores depth-first
  - GBFS (Greedy Best-First Search): Informed, uses heuristic only
  - A*: Optimal informed search, combines actual cost with heuristic


HOW TO RUN
1. Navigate to the project directory:
   cd CAP4630_Project2_SUBMISSION_READY

2. Run the program:
   python search.py

   Or explicitly with Python 3.11:
   python3.11 search.py


The program generates the following outputs:

1. summary.txt
   - Text file containing path costs and nodes expanded for each algorithm
   
2. Visualization Files (in TestingGrid/ folder):
   - DFS.png: Visual representation of DFS path solution
   - BFS.png: Visual representation of BFS path solution
   - GBFS.png: Visual representation of GBFS path solution
   - ASTAR.png: Visual representation of A* path solution
   
   Each visualization shows:
   - The 50x50 grid
   - Start point (source)
   - Goal point (destination)
   - Enclosures (red lines - obstacles)
   - Turfs (green lines - high-cost terrain)
   - Computed path (blue lines)


The program uses test data from the TestingGrid/ folder:
- world1_enclosures.txt: Polygon coordinates for obstacles
- world1_turfs.txt: Polygon coordinates for variable terrain
- custom_enclosures.txt: Custom obstacle definitions (alternative data)
- custom_turfs.txt: Custom terrain definitions (alternative data)

To use custom test data, modify the file paths in the __main__ section of search.py


