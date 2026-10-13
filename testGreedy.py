import random
import itertools

from greedy import overlaps, fits, exactSolver, earliestFinish, earliestStart, shortestDuration,earliestMidpoint
# FUNCTIONS FOR GENERATING INSTANCES
#relatively sparse
def generateSparseInstances(num_jobs=10, max_time=100):
    jobs = []
    while len(jobs) < num_jobs:
        s = random.randint(0, max_time-10)
        Jlength = random.randint(1,5)
        jobs.append((s, s+Jlength))
    return jobs
#heavily overlapping
def generateOverlapInstances(num_jobs=12, max_time=15):
    jobs = []
    while len(jobs) < num_jobs:
        s = random.randint(0, max_time-1)
        f = random.randint(s+1, max_time)
        jobs.append((s, f))
    return jobs
#instances with varying lengeth
def generateVaryingInstances(num_jobs=10, max_time=50):
    jobs = []
    while len(jobs) < num_jobs:
        s = random.randint(0, max_time-1)
        if random.random() < 0.8:
            duration = random.randint(1, 3)
        else:
            duration = random.randint(15, 30)
        jobs.append((s, min(s + duration, max_time)))
    return jobs
#generate instances with clustered start times
def generateClusteredInstances(num_jobs=10, max_time=50):
    jobs = []
    clusters = [5, 20, 35]
    while len(jobs) < num_jobs:
        mid = random.choice(clusters)
        s = max(0, int(random.gauss(mid, 2)))
        duration = random.randint(2, 8)
        jobs.append((s, s + duration))
    return jobs

#PART FIVE EXECUTION

#FUNCTION FOR TESTING GREEDY ALGORITHM
def testGreedyAlgorithm(num_tests=25):
    random.seed(42) #needed to keep solutions reproducable

    heuristics = { 
        "Earliest Finish": earliestFinish,
        "Earliest Start": earliestStart,
        "Shortest Duration": shortestDuration,
        "Earliest Midpoint": earliestMidpoint,
    }
    generators = [
        ("Sparse", generateSparseInstances),
        ("Dense", generateOverlapInstances),
        ("Varied", generateVaryingInstances),
        ("Clustered", generateClusteredInstances),
    ]

    instances = []
    for dist_name, gen_func in generators:        
        for _ in range(num_tests):
            instances.append((dist_name, gen_func()))
            
    for h_name, h_func in heuristics.items():
        optimal_count = 0
        ratios = []
        worst_ratio = 1.0
        worst_instance = None
        worst_opt_len = 0
        worst_h_len = 0

        for dist_name, instance in instances:
            opt_sol = exactSolver(instance)
            opt_len = len(opt_sol)

            if opt_len == 0:
                continue

            h_sol = h_func(instance)
            h_len = len(h_sol)

            ratio = h_len / opt_len
            ratios.append(ratio)

            if h_len == opt_len:
                optimal_count += 1
            
            if ratio < worst_ratio:
                worst_ratio = ratio
                worst_instance = instance
                worst_opt_len = opt_len
                worst_h_len = h_len

        pct_optimal = (optimal_count / len(instances)) * 100
        avg_ratio = sum(ratios) / len(ratios)

        print(f"\nHEURISTIC: {h_name}")
        print(f"  • Optimal Matches : {optimal_count}/{len(instances)} ({pct_optimal:.1f}%)")
        print(f"  • Avg Ratio |H|/OPT: {avg_ratio:.4f}")
        if worst_instance:
            print(f"  • Worst Ratio     : {worst_ratio:.2f} (|H|={worst_h_len}, OPT={worst_opt_len})")
            print(f"  • Worst Instance  : {worst_instance}")
        else:
            print(f"  • Worst Ratio     : 1.00 (No suboptimal instances found)")

if __name__ == "__main__":
    testGreedyAlgorithm()

