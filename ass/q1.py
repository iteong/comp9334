def main():
    # observation period, T (sec)
    T = 30 * 60
    
    # utilisation of device, util (%) = busy time/observation time
    util_cpu = 1102/T
    util_disk1 = 929/T
    util_disk2 = 1017/T
    util_disk3 = 1265/T

    # output rate of system, out_sys (trans/sec) = number of completed jobs/T
    out_sys = 1231/T

    # SERVICE DEMAND LAW
    # service demand of device, svc_dd (sec) = util/output rate
    svc_dd_cpu = util_cpu / out_sys
    svc_dd_d1 = util_disk1 / out_sys
    svc_dd_d2 = util_disk2 / out_sys
    svc_dd_d3 = util_disk3 / out_sys

    print("(Q1a)")
    print("Service demand for CPU is: " + str(svc_dd_cpu) + " sec")
    print("Service demand for Disk 1 is: " + str(svc_dd_d1) + " sec")
    print("Service demand for Disk 2 is: " + str(svc_dd_d2) + " sec")
    print("Service demand for Disk 3 is: " + str(svc_dd_d3) + " sec")

    # number of active terminals = number of interactive clients = number of users
    N = 40
    
    # maximum of service demands in the system given system output rate
    max_of_svc_dds = max(svc_dd_cpu, svc_dd_d1, svc_dd_d2, svc_dd_d3)
    # bound1 = 1 / (max Di) ==> don't depend on N
    bound1 = 1 / max_of_svc_dds

    # bound2, slope = N / (summation of i=1 to i=K) Di)
    think_time_job = 27
    sum_svc_dds = sum([svc_dd_cpu, svc_dd_d1, svc_dd_d2, svc_dd_d3])
    bound2 = N / (sum_svc_dds + think_time_job)
    slope = 1 / (sum_svc_dds + think_time_job)

    # asymptotic bound is minimum of bound1 or bound2
    asymp_bound_throughput = min(bound1, bound2)

    print("(Q1b)")
    print("Bound 1 is: " + str(bound1))
    print("Bound 2 is: " + str(bound2))
    print("Slope at Bound2 is: " + str(slope))
    print("Asymptotic bound on system throughput is: " + str(asymp_bound_throughput) + " jobs/sec")
          
    # number of terminals = max system throughput x (think time + min response time)
    min_resp_time = (N/asymp_bound_throughput) - think_time_job
    
    print("(Q1c)")
    print("Minimum possible response time when number of terminals is 40: " + str(min_resp_time) + " sec")

if __name__ == "__main__":
    main()
