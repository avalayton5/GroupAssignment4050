import random
import time
import csv
import statistics
from greedy import earliestFinish, earliestStart, shortestDuration, earliestMidpoint

# short jobs spread over a long timeline, so many jobs get chosen (a demanding case)
def timingJobs(n, seed):
    rng = random.Random(seed)            # fixed seed = same instances every run
    jobs = []
    for _ in range(n):
        s = rng.randint(0, 10 * n)
        f = s + rng.randint(1, 20)
        jobs.append((s, f))
    return jobs

# times one run of an algorithm, in seconds
def timeOnce(algo, jobs):
    start = time.perf_counter()
    result = algo(jobs)
    elapsed = time.perf_counter() - start
    return elapsed, len(result)

SIZES = [100, 1000, 10000, 100000]
REPEATS = 3
SLOW_LIMIT = 10000   # C and D are O(n^2), so skip sizes above this if too slow

algorithms = [
    ("Earliest Finish", earliestFinish),
    ("Earliest Start", earliestStart),
    ("Shortest Duration", shortestDuration),
    ("Earliest Midpoint", earliestMidpoint),
]

if __name__ == "__main__":
    rows = []
    for n in SIZES:
        jobs = timingJobs(n, seed=n)      # seed = n, document this in the README
        for name, algo in algorithms:
            slow = name in ("Shortest Duration", "Earliest Midpoint")
            if slow and n > SLOW_LIMIT:
                print(n, name, "skipped (O(n^2))", flush=True)
                continue
            times = []
            numChosen = 0
            for r in range(REPEATS):
                elapsed, numChosen = timeOnce(algo, jobs)
                times.append(elapsed)
            median = statistics.median(times)
            print(n, name, "median seconds:", round(median, 5), flush=True)
            rows.append([n, name, REPEATS, median, min(times), max(times), numChosen])

    with open("runtime_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["n", "algorithm", "repeats", "median_sec", "min_sec", "max_sec", "jobs_chosen"])
        writer.writerows(rows)
    print("saved runtime_results.csv")