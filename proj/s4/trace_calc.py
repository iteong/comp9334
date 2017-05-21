from itertools import dropwhile
import math

# number of replications
n = 5

transient = int(input("Enter the transient: "))
num_jobs = 100 - transient
start = transient + 1

def iterate_from_line(f, start_from_line):
    return (l for i, l in dropwhile(lambda x: x[0] < start_from_line, enumerate(f)))

# trace1: Iterate from the line after the transient (data point) / completed job
responses = []
for line in iterate_from_line(open("trace1", "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)
mean1 = sum(responses) / num_jobs
print("Mean response time for trace1 after ignoring the values from the first " + str(transient) + " jobs to remove transient values: " + str(mean1))

# trace2: Iterate from the line after the transient (data point) / completed job
responses = []
for line in iterate_from_line(open("trace2", "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)
mean2 = sum(responses) / num_jobs
print("Mean response time for trace2 after ignoring the values from the first " + str(transient) + " jobs to remove transient values: " + str(mean2))

# trace3: Iterate from the line after the transient (data point) / completed job
responses = []
for line in iterate_from_line(open("trace3", "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)
mean3 = sum(responses) / num_jobs
print("Mean response time for trace3 after ignoring the values from the first " + str(transient) + " jobs to remove transient values: " + str(mean3))

# trace4: Iterate from the line after the transient (data point) / completed job
responses = []
for line in iterate_from_line(open("trace4", "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)
mean4 = sum(responses) / num_jobs
print("Mean response time for trace4 after ignoring the values from the first " + str(transient) + " jobs to remove transient values: " + str(mean4))

# trace5: Iterate from the line after the transient (data point) / completed job
responses = []
for line in iterate_from_line(open("trace5", "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)
mean5 = sum(responses) / num_jobs
print("Mean response time for trace5 after ignoring the values from the first " + str(transient) + " jobs to remove transient values: " + str(mean5))

# calculating sample mean
sample_mean = sum([mean1,mean2,mean3,mean4,mean5])/n
print("\nSample Mean: " + str(sample_mean))

# calculating sample standard deviation
numerator = (sample_mean - mean1)**2 + (sample_mean - mean2)**2 + (sample_mean - mean3)**2 + (sample_mean - mean4)**2 + (sample_mean - mean5)**2
denominator = n - 1
x = numerator/denominator
sample_standard_dev = math.sqrt(x)
print("\nSample Standard Deviation: " + str(sample_standard_dev))

# compute confidence intervals based on input of t-table value for 95% confidence
tvalue = 2.776
confidence_interval = [ sample_mean - (tvalue * (sample_standard_dev/math.sqrt(n))), sample_mean + (tvalue* (sample_standard_dev/math.sqrt(n))) ]
print("\nConfidence Interval: " + str(confidence_interval))
