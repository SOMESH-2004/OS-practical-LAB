def priority_non_preemptive(processes, n, bt, at, priority):
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n  # Completion time
    is_completed = [False] * n

    t = 0
    complete = 0

    while complete != n:
        idx = -1
        best_priority = 999999999

        # Find process with highest priority among arrived & not completed
        for i in range(n):
            if at[i] <= t and not is_completed[i]:
                if priority[i] < best_priority:
                    best_priority = priority[i]
                    idx = i
                elif priority[i] == best_priority:  # tie-breaker: earlier arrival
                    if at[i] < at[idx]:
                        idx = i

        if idx == -1:  # No process has arrived yet
            t += 1
            continue

        # Execute whole process (non-preemptive)
        t += bt[idx]
        ct[idx] = t  # Completion time
        tat[idx] = ct[idx] - at[idx]  # Turnaround time
        wt[idx] = tat[idx] - bt[idx]  # Waiting time
        if wt[idx] < 0:
            wt[idx] = 0
        is_completed[idx] = True
        complete += 1

    # Print table
    print("\n--- Priority Scheduling (Non-Preemptive) ---")
    print("Process\tAT\tBT\tPri\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time = {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time = {sum(tat) / n:.2f}")


# Example (same as your preemptive one)
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]
priority = [2, 1, 4, 3]   # Lower = Higher priority

priority_non_preemptive(processes, n, burst_time, arrival_time, priority)
