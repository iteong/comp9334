import math

def main():

    jobs = 3

    print("(Q3a)")
    # transition rates
    cpu1 = 1/(50/1000)
    cpu2 = 1/(100/1000)
    disk = 1/(50/1000)
    print("Transition rate of CPU1 is: " + str(cpu1) + " jobs/sec")
    print("Transition rate of CPU2 is: " + str(cpu2) + " jobs/sec")
    print("Transition rate of Disk is: " + str(disk) + " jobs/sec")

    states = ((jobs + 1)*(jobs + 2))/2
    print("Number of states: " + str(states))

    print("(Q3d)")
    # Considering equilibrium, Throughput of the system = throughput of the disk = sum of throughput in the CPUs
    # Since there are 2 CPUs with different service times, let's use the disk throughput to get the system throughput

    # Disk utilisation calculated using states where there is a job at disk
    disk_util = 0.1379 + 0 + 0.1552 + 0.1034 + 0.1782 + 0.2299
    service_time_disk = 50/1000
    service_rate_disk = 1/service_time_disk
    # system throughput = disk throughput
    system_throughput = disk_util * service_rate_disk

    print("Disk utilisation is: " + str(disk_util))
    print("System throughput is: " + str(system_throughput) + " jobs/sec")

    print("(Q3e)")
    # CPU1 utilisation calculated using states where there is a job at CPU1
    cpu1_util = 0 + 0.1379 + 0.1954 + 0.1552 + 0 + 0.1782
    service_time_cpu1 = 50/1000
    service_rate_cpu1 = 1/service_time_cpu1
    cpu1_throughput = cpu1_util * service_rate_cpu1
    print("CPU1 throughput is: " + str(cpu1_throughput) + " jobs/sec")
    
    # Little's Law R = N/X, where R = response time, N = number of jobs, X = throughput
    cpu1_resp_time = jobs/cpu1_throughput
    print("Mean response time of CPU1 is: " + str(cpu1_resp_time) + " sec")

    print("(Q3f)")
    disk_resp_time = jobs/system_throughput
    wait_time = disk_resp_time - service_time_disk
    print("Waiting time for user before it gets served at the disk is: " + str(wait_time) + " sec")
    
    
if __name__ == "__main__":
    main()

