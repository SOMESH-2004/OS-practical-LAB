# Round Robin (RR) Scheduling

from collections import deque

def round_robin(processes, n, bt, at, quantum):
    wt = [0] * n
    tat = [0] * n
    rem_bt = bt[:]  # Remaining burst times
    t = 0
    queue = deque()
    visited = [False] * n

    # Sort processes by arrival time
    proc_order = sorted([(at[i], i) for i in range(n)])
    idx = 0

    # Start simulation
    while True:
        # Add processes that have arrived
        while idx < n and proc_order[idx][0] <= t:
            queue.append(proc_order[idx][1])
            visited[proc_order[idx][1]] = True
            idx += 1

        if not queue:
            if idx < n:
                t = proc_order[idx][0]
                continue
            else:
                break

        # Get next process
        i = queue.popleft()

        # Execute for min(quantum, remaining burst)
        exec_time = min(quantum, rem_bt[i])
        rem_bt[i] -= exec_time
        t += exec_time

        # Add newly arrived processes during this execution
        while idx < n and proc_order[idx][0] <= t:
            if not visited[proc_order[idx][1]]:
                queue.append(proc_order[idx][1])
                visited[proc_order[idx][1]] = True
            idx += 1

        # If process not finished, push back to queue
        if rem_bt[i] > 0:
            queue.append(i)
        else:
            tat[i] = t - at[i]
            wt[i] = tat[i] - bt[i]

    # Print table
    print("\n--- Round Robin Scheduling ---")
    print("Process\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time = {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time = {sum(tat) / n:.2f}")
    

# Example
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]
quantum = 2   # time quantum

round_robin(processes, n, burst_time, arrival_time, quantum)
