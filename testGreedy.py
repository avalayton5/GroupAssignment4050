import random
import itertools

from greedy import overlaps, fits, exactSolver, earliestFinish
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

#FUNCTION FOR TESTING GREEDY ALGORITHM
def testGreedyAlgorithm(num_tests=25):
    random.seed(42) #needed to keep solutions reproducable

    distributions = {
        "Sparse Intervals": generateSparseInstances,
        "Heavily Overlapping": generateOverlapInstances,
        "Varied Interval Lengths": generateVaryingInstances,
        "Clustered Start Times": generateClusteredInstances,
    }

    tested = 0
    matched = 0
    print("testing part 4")

    for dist_name, gen_func in distributions.items():
        matched_in_dist = 0
        
        for _ in range(num_tests):
            instance = gen_func()
            
            opt_size = len(exactSolver(instance))
            greedy_size = len(earliestFinish(instance))
            
            tested += 1
            if greedy_size == opt_size:
                matched_in_dist += 1
                matched += 1
            else:
                
                print(f"FAILED {dist_name}, Instance: {instance}")

        print(f" Distribution: {dist_name:<25} Matched: {matched_in_dist}/{num_tests}")

testGreedyAlgorithm(num_tests=25)
