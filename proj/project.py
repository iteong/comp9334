import numpy as np
import operator
import random
import math
from datetime import datetime


###### 1) HELPER FUNCTIONS TO SEED AND GENERATE RANDOM ARRIVAL AND SERVICE TIME ######


# INTER-ARRIVAL TIMES FOR EACH JOB
mean_arrival_rate = 7.2

def randExponential(rateLambda):
    return -math.log(1.0 - random.random()) / rateLambda

def randUniform(a, b):
    return random.uniform(a, b)

def readSeed(n):
    f = open('seed.txt', 'r')
    for i, line in enumerate(f):
        if i == n:
            return line
    f.close()

def interArrival():
    a1 = randExponential(mean_arrival_rate)
    a2 = randUniform(0.75, 1.17)
    interarrival_time = round(a1 * a2, 2)
    return interarrival_time

def serviceTime(s):
    power_budget = 2000
    power_level = power_budget/s

    # generating clock frequency (GHz)
    freq = 1.25 + (0.31 * ((power_level/200) - 1))

    alpha1 = 0.43
    alpha2 = 0.98
    beta = 0.86
    
    r = randUniform(0, 1)
    gamma = (1 - beta)/( (alpha2**(1-beta)) - (alpha1**(1-beta)) )
    
    # inversed CDF (generated from given PDF)
    t = (( ((r*(1-beta))/gamma) + (alpha1 ** (1-beta)) )**(1/(1-beta)))/freq

    return t


###### 2) WRITING SEED INTO FILE AND LENGTH OF SIMULATION BASED ON COMPLETED JOBS ######


# seeding random based on current time and writing into text file for reproducibility
seed = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
f = open('seed.txt', 'a')
#f.write(seed + '\n')
f.close()
random.seed(seed)

# chosen simulation duration parameter to stop simulation
completed_stop = int(input("Choose the maximum number of completed jobs after a job departure (length of simulation): "))


###### 3) CHOOSE LIST OF JOBS USING TEST CASE OR THROUGH RANDOM GENERATION ######


# master clock
master = 0
new_arrival = master

# generate a list of jobs with randomly-generated arrival times and service times
def generateJobList(s, new_arrival, jobs, max_num_jobs):
    for x in range(max_num_jobs):
        # GENERATE A NEW JOB: randomly-generated arrival (incremental) and service times
        new_interarrival = round(interArrival(), 2)
        new_arrival += new_interarrival
        new_service = round(serviceTime(s), 2)
        jobs.append([new_arrival, new_service])
    return jobs

# choose if you want test case for the jobs, or choose to generate jobs
choice = int(input("Choose 1 for test case's jobs, or choose 2 to generate jobs for trace-driven simulation: "))
if choice == 1:
    jobs = [[1, 2.1],[2, 3.3],[3, 1.1],[5, 0.5],[15, 1.7]]
else:
    # chosen number of jobs being fed into the simulation
    max_num_jobs = int(input("Choose the number of jobs to generate that will be fed into the simulation in a list: "))
    # number of servers switched on is s; power consumption (Watt) is power_budget or power_level
    s = int(input("Choose the number of servers to switch on: ")) # 3, 4, 5, 6, 7, 8, 9, 10
    
    jobs_init = []
    jobs = generateJobList(s, new_arrival, jobs_init, max_num_jobs)
    print("\nList of jobs to be fed into the simulation: " + str(jobs))


###### 4) SIMULATION OF PS SERVER WITH TRACE-DRIVEN SIMULATION USING LIST OF JOBS ######


# next arrival = first job in arriving jobs
next_arrival = jobs[0][0]
# assuming no future arrivals, we use Inf (= infinity) to denote an empty departure event
next_departure = np.inf
# jobs to be fed into the processor sharing server waiting
job_list = []
# server = True when busy, False when idle
server = False
# first event at master clock = 0 with no departure time
first_event = True
# cumulative response time for departing events from time of their arrivals
response = 0
# number of completed jobs at the end of simulation
completed = 0

def ps_server(jobs, master, next_arrival, next_departure, job_list, server, first_event, response, completed, completed_stop):

    # BASE CASE FOR RECURSION
    # number of completed jobs reached its chosen limit after a job departs
    if completed == completed_stop:
        return    
    else:
        print("List of jobs being fed into simulation: " + str(jobs))
        # no jobs left to process after last job departs
        if first_event == False and len(jobs) == 0 and len(job_list) == 0:
            next_arrival = np.inf       
            event_type = "DEPARTURE"
            master = next_departure
            next_departure = np.inf
            response += (master - job_list[0][0])
            completed += 1
            job_list.pop(0)
            server = False
            print("master: " + str(master) + ", type: " + event_type + ", next arrival: " + str(next_arrival) + ", next departure: " + str(next_departure) + ", job list: " + str(job_list)  + ", cumulative response: " + str(response) + ", completed jobs: " + str(completed) + ", server busy: " + str(server) + "\n")
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

        # add to completed jobs when a job departs
        completed += 1
        
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
            # if only left last job to process, next_arrival time equals to inf
            next_arrival = np.inf

        # only remove job from jobs if there is an arrival next
        jobs.pop(0)

    print("master: " + str(master) + ", type: " + event_type + ", next arrival: " + str(next_arrival) + ", next departure: " + str(next_departure) + ", job list: " + str(job_list)  + ", cumulative response: " + str(response) + ", completed jobs: " + str(completed) + ", server busy: " + str(server) + "\n")
    
    if first_event == True:
        # prepare for base case in recursion
        first_event = False
    
    # recursion
    ps_server(jobs, master, next_arrival, next_departure, job_list, server, first_event, response, completed, completed_stop)


# maximum number of completed jobs must not exceed number of new jobs, otherwise equal them to each other
if completed_stop > len(jobs):
    completed_stop = len(jobs)
    print("\nInput of max number of completed jobs is larger than number of new jobs in list, so reduced max number from " + str(completed_stop) + " to the same number as number of jobs fed into simulation: " + str(len(jobs)))

# initial round
print("\nList of jobs being fed into simulation: " + str(jobs))
print("master: " + str(master) + ", type: NAN, next arrival: " + str(next_arrival) + ", next departure: " + str(next_departure) + ", job list: " + str(job_list)  + ", cumulative response: " + str(response) + ", completed jobs: " + str(completed) + ", server busy: " + str(server) + "\n")
ps_server(jobs, master, next_arrival, next_departure, job_list, server, first_event, response, completed, completed_stop)
