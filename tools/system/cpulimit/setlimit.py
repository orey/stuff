import subprocess, time, sys

QUOTA = 70 #percent
DELAY = 30 #seconds
FILEROOT = "processes"


procs = {} # key = procid, value = quota

AVERAGE_ALGO = 1
THRESHOLD_ALGO = 0


#--------------------------------------------------- limit
def limit(software, threshold, algo, verbose=False):
    filename = FILEROOT + '_' + software + ".pid"
    # get the list of pids in a file to read the output
    with open(filename, "w") as f:
        comp = subprocess.run(["pgrep", software],
                              stdout = f)
    pids = []
    # read the output
    with open(filename, "r") as g:
        pids = g.read().split("\n")
        if verbose:
            print(pids)
    # remove void strings
    pids = [x for x in pids if x]
    if verbose:
        print(pids)
    # remove processes that are no longer existing
    keys_to_delete = []
    for p in procs:
        if p not in pids:
            keys_to_delete.append(p)
    for k in keys_to_delete:
        del procs[k]
        print(k + " is no longer existing. Removed.")
    # determine per process quota
    if algo == AVERAGE_ALGO:
        squota = str(round(float(threshold) / len(pids), 0))
    else: # THRESHOLD_ALGO:
        squota = threshold
    # launch an instance of each limiter
    for pid in pids:
        if pid not in procs:
            subprocess.Popen([ "cpulimit", "--pid", pid, "--limit", squota+"%" ])
            procs[pid] = squota
    if verbose:
        print(procs)

#--------------------------------------------------- main
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python setlimit.py [program name] [threshold in %]")
        sys.exit()
    software = sys.argv[1]
    threshold = sys.argv[2]
    run = 0
    while True:
        print(f"|{run+1}|",end="")
        run += 1
        limit(software, threshold, THRESHOLD_ALGO)
        time.sleep(DELAY)
    

               
