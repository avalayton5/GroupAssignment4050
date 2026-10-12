import itertools
# HELPER FUNCTIONS (for part one)
def overlaps(a, b):
    return a[0] < b[1] and b[0] < a[1]

def fits(job, chosen):
    for c in chosen:
        if overlaps(job, c):
            return False
    return True

# function to check entire subset of jobs is mutually compatible (used for part two)
def validSubset(subset):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if overlaps(subset[i], subset[j]): #checking for time conflict
                return False
    return True

# -----PART ONE--------
def greedy(jobs, keys):
    pairs = []
    for i in range(len(jobs)):
        pairs.append((keys[i], i))   
    pairs.sort()                     

    chosen = []
    for key, i in pairs:
        if fits(jobs[i], chosen):
            chosen.append(jobs[i])
    return chosen

#all four algorithms are O(n^2), sorting is O(nlogn) but fits() loops over every chosen job

#uses greedy and selects jobs with the earliest finish time
#ties go to earlier start, then lower index
def earliestFinish(jobs):
    keys = []
    for (s, f) in jobs:
        keys.append((f, s))          
    return greedy(jobs, keys)

#uses greedy and selects jobs with the earliest start time
#ties go to earlier finish, then lower index
def earliestStart(jobs):
    keys = []
    for (s, f) in jobs:
        keys.append((s, f))          
    return greedy(jobs, keys)

#uses greedy and selects jobs with the shortest time duration
#ties go to earlier finish, then earlier start, then lower index
def shortestDuration(jobs):
    keys = []
    for (s, f) in jobs:
        keys.append((f - s, f, s))   
    return greedy(jobs, keys)

#uses greedy and selects jobs with the earliest middle point of the job
#ties go to earlier finish, then earlier start, then lower index
def earliestMidpoint(jobs):
    keys = []
    for (s, f) in jobs:
        keys.append((s + f, f, s))   
    return greedy(jobs, keys)

#----PART TWO----
#O(2^n * n^2), 2^n subsets, and validSubset compares every pair in a subset
#not practical for large n
def exactSolver(jobs):
    #im using the brute force method to find the optimal solution
    n = len(jobs) #n equals how many elements in jobs

    for r in range(n, 0, -1):   #subtracting one after each iteration
        for subset in itertools.combinations(jobs, r):  #generates every possible unique grouping
            if validSubset(subset):
                return list(subset)
    return []

# ----SANITY TESTS----
if __name__ == "__main__":
    test1 = [(0, 10), (1, 2), (2, 3), (3, 4), (4, 5)]   # sanity test 1
    test2 = [(2, 4), (0, 3), (3, 6)]                     # sanity test 2
    test3 = [(0, 6), (3, 4), (4, 5), (5, 6)]             # midpoint failure
    test4 = [(5, 6), (0, 1)]                             # catches the "last chosen only" bug

    opt1 = exactSolver(test1)
    opt2 = exactSolver(test2)
    opt3 = exactSolver(test3)

    print("Test 1 OPT size:", len(opt1), "| Solution:", opt1)
    print("Test 2 OPT size:", len(opt2), "| Solution:", opt2)
    print("Test 3 OPT size:", len(opt3), "| Solution:", opt3)

    print("Sanity test 1 (earliestStart gets 1, OPT is 4): ", len(earliestStart(test1)) == 1 and len(opt1) == 4)
    print("earliestFinish matches OPT on test1: ", len(earliestFinish(test1)) == len(opt1))

    print("Sanity test 2 (shortestDuration gets 1, OPT is 2): ", len(shortestDuration(test2)) == 1 and len(opt2) == 2)
    print("earliestFinish matches OPT on test2: ", len(earliestFinish(test2)) == len(opt2))

    print("shortestDuration keeps both non-overlapping jobs: ", len(shortestDuration(test4)) == 2)

    print("Midpoint fails on test3 (gets 1, OPT is 3): ", len(earliestMidpoint(test3)) == 1 and len(opt3) == 3)
    print("earliestFinish matches OPT on test3: ", len(earliestFinish(test3)) == len(opt3))