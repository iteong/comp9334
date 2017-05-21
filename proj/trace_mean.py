from itertools import dropwhile

trace = str(input("Enter the name of the trace file to calculate mean response time: "))
start = int(input("Enter the line number (data point) that you want to start calculating from: "))

print("\nReading filename " + str(trace) + " and start iterating from the " + str(start) + "th data point (line) of response time till the end of file to calculate mean response time...\n")

def iterate_from_line(f, start_from_line):
    return (l for i, l in dropwhile(lambda x: x[0] < start_from_line, enumerate(f)))

responses = []

# Iterate from nth line (data point) / completed job
for line in iterate_from_line(open(trace, "r"), start):
    line = line.rstrip('\n')
    line = float(line)
    responses.append(line)

num_jobs = len(responses)
mean = sum(responses) / num_jobs
first = start - 1
print("Mean response time after ignoring the values from the first " + str(first) + " jobs to remove transient values: " + str(mean))
