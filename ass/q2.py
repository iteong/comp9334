# E = utilisation = arr_rate/service_rate; N = number of operators/terminals
def ErlangB(E, N):
    InvB = 1.0
    for j in range(1, N + 1):
        InvB = 1.0 + InvB * (j / E)
    return (1.0 / InvB)

def QueuingSeries(E, i, M):
    result = 0.0
    for i in range(0, M+1):
        result += ((1/4)**i)*(E**(4+i))
    result = result*(1/24)
    return result

def p0(E, i, M):
    denominator = 1 + E + (1/2)*(E**2) + (1/6)*(E**3) + QueuingSeries(E, i, M)
    p0 = 1/denominator
    return p0

def main():
    # number of operators
    N = 4
    
    # arrival rate, arr_rate = calls/hour
    arr_rate = 20
    
    # mean service time, svc_mean (hour)
    svc_mean = 10/60
    # service rate = 1/mean service time
    svc_rate = 1/svc_mean
    
    # state transition for M/M/m/m queue with no waiting room/buffer => Erlang B formula
    # probability an arriving call is blocked = probability 4 customers in system (since there is 4 operators)
    E = arr_rate/svc_rate

    print("(Q2a)")
    prob_rejected = ErlangB(E, N)
    print("Probability that incoming call is rejected is: " + str(prob_rejected))

    print("(Q2b iv)")
    P0 = 0
    prob_rejected_new = 0
    
    for M in range(1000):
        # solve for P0
        P0 = p0(E, 0, M)
        
        # find probability of last node
        Prob = ((1/4)**M)*(1/24)*(E**(4+M))*P0

        # if probability of last node is < 50% of prob_rejected from Q2(a)
        if Prob < prob_rejected/2:
            prob_rejected_new = Prob
            print("Smallest value of M is found! M = " + str(M) + ", where P0 is: " + str(P0) + " and P4+M is: " + str(Prob) + ". P4+M is < 50% of the probability that an incoming call is rejected from Q2(a).")
            break
        else:
            print("Smallest value of M not found yet. M = " + str(M) + ", where P0 is: " + str(P0) + " and P4+M is: " + str(Prob))

    print("(Q2b v)")
    throughput = arr_rate * (1 - prob_rejected_new)
    mean_num_customers = (1*0 + E*1 + (1/2)*(E**2)*2 + (1/6)*(E**3)*3 + (1/24)*((1/4)**0)*(E**(4+0))*4 + (1/24)*((1/4)**1)*(E**(4+1))*5 + (1/24)*((1/4)**2)*(E**(4+2))*6 + (1/24)*((1/4)**3)*(E**(4+3))*7) * P0
    resp_time = mean_num_customers / throughput
    wait_time = resp_time - svc_mean
    print("Rejected rate is: " + str(prob_rejected_new))
    print("Throughput is: " + str(throughput) + " calls/hour")
    print("Mean number of customers in queue is: " + str(mean_num_customers))
    print("Mean response time: " + str(resp_time) + " hour")
    print("Waiting time that an accepted call needs to wait before it will be served by the operator: " + str(wait_time) + " hour")

    
if __name__ == "__main__":
    main()

