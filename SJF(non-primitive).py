# Non-Preemptive Shortest Job First (SJF) Scheduling

def sjf_non_preemptive(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n
    completed = [False] * n
    completion_time = [0] * n

    t = 0   # current time
    completed_count = 0

    while completed_count < n:
        idx = -1
        min_bt = 999999999

        # Select process with min burst time among available
        for i in range(n):
            if at[i] <= t and not completed[i]:
                if bt[i] < min_bt:
                    min_bt = bt[i]
                    idx = i

        if idx == -1:
            t += 1
            continue

        # Execute the chosen process
        t += bt[idx]
        completion_time[idx] = t
        tat[idx] = completion_time[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]

        completed[idx] = True
        completed_count += 1

    # Print table
    print("\nProcess\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time = {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time = {sum(tat) / n:.2f}")
    

# Example
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]

sjf_non_preemptive(processes, n, burst_time, arrival_time)
