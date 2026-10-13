#University of Missouri CS 4050 - GEA 1: Greedy Algorithms Under Pressure
#interval scheduling
**Language:** Python 3
**Dependencies:** Standard Python library (`random`, `itertools`, `time`, `csv`, `statistics`).  
No external packages required.

## Files
| File | Purpose |
|---|---|
| `greedy.py` | Core helper functions (`overlaps`, `fits`, `validSubset`), four greedy algorithms (`earliestFinish`, `earliestStart`, `shortestDuration`, `earliestMidpoint`), and brute-force exact solver (`exactSolver`). |
| `testGreedy.py` | Generator functions (sparse, dense, varied lengths, clustered starts) and execution logic for Parts 4 & 5 empirical testing. |
| `counterexamples.py` | Part 3: Automated counterexample search for greedy failure modes and timeline visualization drawer. |
| `runtime.py` | Part 6: Runtime benchmarks across problem sizes ($n=100$ to $n=100,000$) exporting results to `runtime_results.csv`. |
| `README.md` | Repository documentation and reproduction instructions. |

## Input format
the algorithms take a list of time intervals `(start, finish)` the are logically half open time intervals `[s, f)`

## Algorithms
from the "python greedy.py" file get earliestFinish, exactSolver
jobs = [(0, 10), (1, 2), (2, 3), (3, 4), (4, 5)]
earliestFinish(jobs)   # -> [(1, 2), (2, 3), (3, 4), (4, 5)]
exactSolver(jobs)     # -> [(1, 2), (2, 3), (3, 4), (4, 5)]

#replicate results
first run greedy.py for sanity tests
second run "python counterexamples.py" counterexamples and visualization
third run "python testGreedy.py" for the testing
fourth run "python runtime.py" for the evaluation of how the algorithm runs
