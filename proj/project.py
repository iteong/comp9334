import numpy as np
from decimal import *

getcontext().prec = 2

# processor sharing simulation, where s = number of operating servers
def simulation(s):
    return

def ps_server(jobs):
    # global variables used
    global master
    global next_arrival
    global next_departure
    global job_list
    global server
    global first_event

    # base case for recursion
    if len(jobs) == 0:
        return

    # keeping track of the time of last event
    last_event = master

    # determining event type for the next event
    if next_arrival < next_departure:
        event_type = "ARRIVAL"
        # master clock jumps to time of next job/arrival    
        master = jobs[0][0]
    else:
        event_type = "DEPARTURE"
        # master clock jumps to time of next departure
        master = next_departure 
    
    # time lapsed since last event
    time_lapsed = round(master - last_event, 2)

    # keeping track of number of jobs in server since last event
    num_jobs = len(job_list)

    print("time lapsed: " + str(time_lapsed))
    print("number of jobs: " + str(num_jobs))

    # only add job to job_list if it is an arrival
    if event_type == "ARRIVAL":
        job = jobs[0]
        job_list.append(job)
    
    # updating time of next departure with service time left
    if first_event == True:
        next_departure = master + job_list[0][1]
    else:
        # update service time needed by jobs before arrival of new job in job list
        for i in range(0, num_jobs):
            print("i:" + str(i))
            
            diff = time_lapsed/num_jobs
            print("diff: " + str(diff))
            print("val: " + str(job_list[i][1]))
            job_list[i][1] = round(job_list[i][1] - diff, 2)
        next_departure = next_departure + job_list[0][1]

    # if job list is not empty
    if len(job_list) != 0:
        server = True

        if len(jobs) > 1:
            next_arrival = jobs[1][0]

        print("master clock: " + str(master) + ", event type: " + event_type + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))
        
        jobs.pop(0)
        # recursion
        first_event = False
        ps_server(jobs)

jobs = [[1, 2.1],[2, 3.3],[3, 1.1],[5, 0.5],[15, 1.7]]

# INITIALISATION
first_event = True
# master clock
master = 0
# server = true when busy, server = false when idle
server = False

next_arrival = jobs[0][0]
# assuming no future arrivals
next_departure = np.inf
   
job_list = []

print("master clock: " + str(master) + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))
ps_server(jobs)
