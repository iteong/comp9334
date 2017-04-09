import math

def main():

    jobs = 3
    
    # transition rates
    cpu1 = 1/(50/1000)
    cpu2 = 1/(100/1000)
    disk = 1/(50/1000)

    print("Transition rate of CPU1 is: " + str(cpu1) + " jobs/sec")
    print("Transition rate of CPU2 is: " + str(cpu2) + " jobs/sec")
    print("Transition rate of Disk is: " + str(disk) + " jobs/sec")

    states = ((jobs + 1)*(jobs + 2))/2
    print("Number of states: " + str(states))
    


if __name__ == "__main__":
    main()

