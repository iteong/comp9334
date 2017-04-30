import numpy as np


# processor sharing simulation, where s = number of operating servers
def simulation(s):
    return

def ps_server(jobs):

    # base case for recursion
    if len(jobs) == 0:
        return
    
    # master clock jumps to next job
    global master
    master = jobs[0][0]
    
    global next_departure
    next_departure = master + jobs[0][1]
    global job_list
    job = jobs[0]
    job_list.append(job)

    # if job list is not empty
    if len(job_list) != 0:
        global server
        server = True

        global next_arrival

        if len(jobs) > 1:
            next_arrival = jobs[1][0]

        print("master clock: " + str(master) + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))
        
        jobs.pop(0)
        # recursion
        ps_server(jobs)

jobs = [(1, 2.1),(2, 3.3),(3, 1.1),(5, 0.5),(15, 1.7)]

# master clock
master = 0
# server = true when busy, server = false when idle
server = False

next_arrival = jobs[0][0]
# assuming no future arrivals
next_departure = np.inf
   
job_list = []

print("initialization: master clock: " + str(master) + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))
ps_server(jobs)
