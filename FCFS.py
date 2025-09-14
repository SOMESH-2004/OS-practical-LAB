# First Come First Serve (FCFS) Scheduling in Python

def find_waiting_time(processes, n, burst_time, arrival_time):
    waiting_time = [0] * n
    service_time = [0] * n
    service_time[0] = arrival_time[0]

 # Calculate waiting time
    for i in range(1, n):
        service_time[i] = service_time[i-1] + burst_time[i-1]
        waiting_time[i] = service_time[i] - arrival_time[i]

# If waiting time is negative, make it zero
        if waiting_time[i] < 0:
            waiting_time[i] = 0
            service_time[i] = arrival_time[i]

    return waiting_time


def find_turnaround_time(n, burst_time, arrival_time, waiting_time):
    turnaround_time = [0] * n
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]
    return turnaround_time


def fcfs_scheduling(processes, n, burst_time, arrival_time):
# Find waiting time
    waiting_time = find_waiting_time(processes, n, burst_time, arrival_time)

# Find turnaround time
    turnaround_time = find_turnaround_time(n, burst_time, arrival_time, waiting_time)

# Calculate average times
    total_wt = sum(waiting_time)
    total_tat = sum(turnaround_time)

    print("\nProcess\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")


# Example
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]  
arrival_time = [0, 1, 2, 3]  

fcfs_scheduling(processes, n, burst_time, arrival_time)
