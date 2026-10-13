import random
from greedy import earliestFinish, earliestStart, earliestMidpoint, shortestDuration, exactSolver

#creates a list of random job intervals
def randomJobs(n, maxTime, rng):
    jobs = []
    for _ in range(n):
        s = rng.randint(0, maxTime - 1)
        f = rng.randint(s + 1, maxTime)
        jobs.append((s,f))
    return jobs

#uses the heuristics in greedy.py to find what it would have picked
#uses exactSolver to find the optimal solutions
def findCounterExample(heuristic, seed, trialsPerSize = 5000):
    rng = random.Random(seed)
    for n in range(3, 9):
        for trial in range(trialsPerSize):
            jobs = randomJobs(n, 10, rng)
            heuristicSol = heuristic(jobs)
            optSol = exactSolver(jobs)
            if len(heuristicSol) < len(optSol):
                return(jobs, heuristicSol, optSol)
    return None

#creates a visual for the job intervals
#during a job time, there will be ## instead of ..
def drawTimeline(jobs, chosen):
    maxTime = 0
    for (s, f) in jobs:
        if f > maxTime:
            maxTime = f
    for (s, f) in jobs:
        row = ""
        for t in range(maxTime):
            if s <= t and t < f:
                row += "#"
            else:
                row += "."
        mark = ""
        if (s, f) in chosen:
            mark = "<- picked"
        print(row, (s,f), mark)

#create a report with all of the results
def report(heuristic, seed):
    result = findCounterExample(heuristic, seed)
    if result is None:
        print("No counterexample found in this search.")
        return
    jobs, heuristicSol, optSol = result
    print("Intervals: ", jobs)
    print("Heuristic selected: ", heuristicSol)
    print("Optimal Solution: ", optSol)
    print("|Greedy(I)| =", len(heuristicSol), ", OPT(I) =", len(optSol))
    print("Timeline of the heuristic's picks: ")
    drawTimeline(jobs, heuristicSol)
    print("Timeline of optimal solution: ")
    drawTimeline(jobs, optSol)

#print out the results in the report
SEED = 200000
print("Earliest Start")
report(earliestStart, SEED)
print()
print("Shortest Duration")
report(shortestDuration, SEED)
print()
print("Earliest Midpoint")
report(earliestMidpoint, SEED)
print()
print("Earliest Finish")
report(earliestFinish, SEED)
  
