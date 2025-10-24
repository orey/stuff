import subprocess, time

QUOTA = 60 #percent
SOFT = "opera"
#SOFT = "chromium"
DELAY = 30 #seconds


procs = {} # key = procid, value = quota

AVERAGE = 1
THRESHOLD = 0



def limit(algo, verbose=False):
    # get the list of pids in a file to read the output
    with open("processes.txt", "w") as f:
        comp = subprocess.run(["pgrep", SOFT],
                              stdout = f)
    pids = []
    # read the output
    with open("processes.txt", "r") as g:
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
    if algo == AVERAGE:
        squota = str(round(QUOTA / len(pids), 0))
    else: # THRESHOLD:
        squota = str(QUOTA)
    # launch an instance of each limiter
    for pid in pids:
        if pid not in procs:
            subprocess.Popen([ "cpulimit", "--pid", pid, "--limit", squota+"%" ])
            procs[pid] = squota
    if verbose:
        print(procs)


if __name__ == "__main__":
    run = 0
    while True:
        print(f"************** Run {run+1}")
        run += 1
        limit(THRESHOLD)
        time.sleep(DELAY)
    

               
