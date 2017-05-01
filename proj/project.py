import numpy as np
import operator

def ps_server(jobs):
    # global variables used
    global master
    global next_arrival
    global next_departure
    global job_list
    global server
    global first_event

    # base case for recursion when no jobs left to process after last job departs
    if first_event == False and len(jobs) == 0:
        next_arrival = np.inf       
        event_type = "DEPARTURE"
        master = next_departure
        next_departure = np.inf
        server = False
        job_list.pop(0)
        print("master clock: " + str(master) + ", event type: " + event_type + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))
        return
    
    # keeping track of the time of last event
    last_event = master

    # determining event type for the next event
    if next_arrival < next_departure:
        event_type = "ARRIVAL"
        # master clock jumps to time of next job/arrival    
        master = next_arrival
        
    else:
        event_type = "DEPARTURE"
        # master clock jumps to time of next departure
        master = next_departure 
    
    # time lapsed since last event
    time_lapsed = round(master - last_event, 2)

    # keeping track of number of jobs in server since last event
    num_jobs = len(job_list)

    # only add job to job_list if event is an arrival
    if event_type == "ARRIVAL":
        job = jobs[0]
        job_list.append(job)
        
    elif event_type == "DEPARTURE":
    # depart job with lowest service time if event is a departure, removing it from job_list after service
        depart_list = []
        for job in job_list:
            depart_list.append(job[1])
        min_index, min_value = min(enumerate(depart_list), key=operator.itemgetter(1))
        time_lapsed = round(time_lapsed - min_value, 2)
        job_list.pop(min_index)
    
    # copy out job_list without arrival_time for finding next job to depart
    min_list = []
    
    # updating time of next departure with service time left
    if first_event == True:       
        for job in job_list:
            min_list.append(job[1])
        
        min_index, min_value = min(enumerate(min_list), key=operator.itemgetter(1))
        next_departure = master + (min_value * len(job_list))
    else:
        # update service time needed by jobs before arrival of new job in job list
        if event_type == "ARRIVAL":
            for i in range(0, num_jobs):
                diff = time_lapsed/num_jobs
                job_list[i][1] = round(job_list[i][1] - diff, 2)

            for job in job_list:
                min_list.append(job[1])
        
        elif event_type == "DEPARTURE":
            for i in range(0, len(job_list)):
                diff = time_lapsed/(len(job_list))
                job_list[i][1] = round(job_list[i][1] - diff, 2)

            for job in job_list:
                min_list.append(job[1])

        if len(min_list) != 0:
            min_index, min_value = min(enumerate(min_list), key=operator.itemgetter(1))
            next_departure = master + (min_value * len(job_list))
        else:
            next_departure = np.inf

    # if job list is not empty
    if len(job_list) != 0:
        server = True
    else:
        server = False

    if len(jobs) > 0:
        # only update arrival time if there is an arrival next
        if event_type == "ARRIVAL" and len(jobs) != 0:
            if len(jobs) > 1:
                next_arrival = jobs[1][0]
            else:
                # if only left 1 last job to process, next_arrival equals that job's time
                next_arrival = jobs[0][0]

    print("master clock: " + str(master) + ", event type: " + event_type + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list))

    # only remove job from jobs if it is an arrival next
    if event_type == "ARRIVAL":            
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
