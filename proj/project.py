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
    global response

    # base case for recursion when no jobs left to process after last job departs
    if first_event == False and len(jobs) == 0:
        next_arrival = np.inf       
        event_type = "DEPARTURE"
        master = next_departure
        next_departure = np.inf
        job_list.pop(0)
        server = False
        print("master clock: " + str(master) + ", event type: " + event_type + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list) + ", cumulative response time: " + str(response) + ", server busy: " + str(server))
        return
    
    # tracking time of last event
    last_event = master

    # determining event type for the next event of which master clock jumps to
    if next_arrival < next_departure:
        event_type = "ARRIVAL"   
        master = next_arrival       
    else:
        event_type = "DEPARTURE"
        master = next_departure 
    
    # tracking time lapsed since last event, after master clock's jump
    time_lapsed = round(master - last_event, 2)

    # tracking number of jobs in server since last event
    num_jobs = len(job_list)

    if event_type == "ARRIVAL":
        # only add job to job_list if current event is an arrival
        job = jobs[0]
        job_list.append(job)       
    elif event_type == "DEPARTURE":
        # depart job with lowest service time if current event is a departure, removing it from job_list after servicing
        depart_list = []
        for job in job_list:
            depart_list.append(job[1])
        min_index, min_value = min(enumerate(depart_list), key=operator.itemgetter(1))
        time_lapsed = round(time_lapsed - min_value, 2)
        
        # calculate cumulative response time based on departing job's arrival and departure times
        response += (master - job_list[min_index][0])
        
        job_list.pop(min_index)
    
    # if current iteration is not the first round
    if first_event == False:
        # update service time of jobs based on event_type before the arrival of new job in job_list
        if event_type == "ARRIVAL":
            for i in range(0, num_jobs):
                diff = time_lapsed/num_jobs
                job_list[i][1] = round(job_list[i][1] - diff, 2)       
        elif event_type == "DEPARTURE":
            for i in range(0, len(job_list)):
                diff = time_lapsed/(len(job_list))
                job_list[i][1] = round(job_list[i][1] - diff, 2)

    # copy out jobs from job_list to min_list without its arrival_time to find next job to depart based on indexing
    min_list = []
    for job in job_list:
        min_list.append(job[1])

    if len(min_list) != 0:
        min_index, min_value = min(enumerate(min_list), key=operator.itemgetter(1))
        # next departing job's service time times number of jobs (processor sharing so slowed down by number of jobs)
        next_departure = master + (min_value * len(job_list))
    else:
        # if no more jobs to depart
        next_departure = np.inf

    # if job_list is not empty
    if len(job_list) != 0:
        server = True
    else:
        server = False

    # only update next_arrival time if there is an arrival next
    if event_type == "ARRIVAL" and len(jobs) != 0:
        if len(jobs) > 1:
            next_arrival = jobs[1][0]
        else:
            # if only left last job to process, next_arrival time equals that job's time
            next_arrival = jobs[0][0]

        # only remove job from jobs if there is an arrival next
        jobs.pop(0)

    print("master clock: " + str(master) + ", event type: " + event_type + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list) + ", cumulative response time: " + str(response) + ", server busy: " + str(server))
    
    if first_event == True:
        # prepare for base case in recursion
        first_event = False
    
    # recursion
    ps_server(jobs)

jobs = [[1, 2.1],[2, 3.3],[3, 1.1],[5, 0.5],[15, 1.7]]

# INITIALISATION
first_event = True
# master clock
master = 0
# server = True when busy, server = False when idle
server = False
# next arrival = first job in arriving jobs
next_arrival = jobs[0][0]
# assuming no future arrivals
next_departure = np.inf
# cumulative response time for departing events from time of their arrivals
response = 0
   
job_list = []

print("master clock: " + str(master) + ", next arrival time: " + str(next_arrival) + ", next departure time: " + str(next_departure) + ", job list: " + str(job_list)  + ", cumulative response time: " + str(response) + ", server busy: " + str(server))
ps_server(jobs)
