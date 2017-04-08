# E = utilisation = arr_rate/service_rate; N = number of operators/terminals
def ErlangB(E, N):
    InvB = 1.0
    for j in range(1, N + 1):
        InvB = 1.0 + InvB * (j / E)
    return (1.0 / InvB)

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
    prob_rejected = ErlangB(E, N)

    print("(Q2a)")
    print("Probability that incoming call is rejected is: " + str(prob_rejected))

if __name__ == "__main__":
    main()

