# Priority Scheduling - Preemptive

def priority_preemptive(processes, n, bt, at, priority):
    rt = bt[:]  # Remaining burst times
    wt = [0] * n
    tat = [0] * n
    complete = 0
    t = 0
    finish_time = 0
    is_completed = [False] * n

    while complete != n:
        idx = -1
        best_priority = 999999999

        # Find process with highest priority at current time
        for i in range(n):
            if at[i] <= t and not is_completed[i]:
                if priority[i] < best_priority:
                    best_priority = priority[i]
                    idx = i
                elif priority[i] == best_priority:  # tie-breaker: earlier arrival
                    if at[i] < at[idx]:
                        idx = i

        if idx == -1:
            t += 1
            continue

        # Execute process for 1 unit
        rt[idx] -= 1
        t += 1

        # If process finishes
        if rt[idx] == 0:
            complete += 1
            finish_time = t
            tat[idx] = finish_time - at[idx]
            wt[idx] = tat[idx] - bt[idx]
            if wt[idx] < 0:
                wt[idx] = 0
            is_completed[idx] = True

    # Print table
    print("\n--- Priority Scheduling (Preemptive) ---")
    print("Process\tAT\tBT\tPri\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{at[i]}\t{bt[i]}\t{priority[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time = {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time = {sum(tat) / n:.2f}")


# Example
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]
priority = [2, 1, 4, 3]   # Lower = Higher priority

priority_preemptive(processes, n, burst_time, arrival_time, priority)
