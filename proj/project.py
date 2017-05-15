import ps_server as ps
import numpy as np
import random
import math
from datetime import datetime

# INTER-ARRIVAL TIMES FOR EACH JOB
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

seed = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
f = open('seed.txt', 'a')
#f.write(seed + '\n')
f.close()

random.seed(1)
mean_arrival_rate = 7.2

a1 = randExponential(mean_arrival_rate)
a2 = randUniform(0.75, 1.17)
arr = a1 * a2

# SERVICE TIMES FOR EACH JOB
# number of servers switched on; power consumption (Watt)
s = [3, 4, 5, 6, 7, 8, 9, 10]
power = [150, 200, 250]

# generating clock frequency (GHz)
freq = 1.25 + (0.31 * ((power[0]/200) - 1))

# t = service time, when server's clock frequency = 1 GHz
#t = CDF
#service_time = t/freq

# jobs to be fed into the processor sharing server
jobs = [[1, 2.1],[2, 3.3],[3, 1.1],[5, 0.5],[15, 1.7]]
job_list = []
# first event at master clock = 0 with no departure time
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
# number of completed jobs
completed = 0

print("master: " + str(master) + ", next arrival: " + str(next_arrival) + ", next departure: " + str(next_departure) + ", job list: " + str(job_list)  + ", cumulative response: " + str(response) + ", completed jobs: " + str(completed) + ", server busy: " + str(server))
ps.ps_server(jobs, master, next_arrival, next_departure, job_list, server, first_event, response, completed)
