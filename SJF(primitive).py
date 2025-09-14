# Preemptive SJF (Shortest Remaining Time First - SRTF) Scheduling

def find_waiting_time(processes, n, bt, at):
    rt = bt[:]  # Remaining times (copy of burst times)
    wt = [0] * n
    complete = 0
    t = 0
    minm = 999999999
    shortest = 0
    check = False

    while complete != n:
        # Find process with minimum remaining time at current time
        for j in range(n):
            if at[j] <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                shortest = j
                check = True

        if not check:
            t += 1
            continue

        # Reduce remaining time
        rt[shortest] -= 1
        minm = rt[shortest]
        if minm == 0:
            minm = 999999999

        # If process finishes
        if rt[shortest] == 0:
            complete += 1
            check = False
            finish_time = t + 1
            wt[shortest] = finish_time - bt[shortest] - at[shortest]
            if wt[shortest] < 0:
                wt[shortest] = 0

        t += 1

    return wt


def find_turnaround_time(processes, n, bt, at, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat


def sjf_preemptive(processes, n, bt, at):
    wt = find_waiting_time(processes, n, bt, at)
    tat = find_turnaround_time(processes, n, bt, at, wt)

    total_wt = sum(wt)
    total_tat = sum(tat)

    print("\nProcess\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i]}\t{at[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")


# Example
processes = [1, 2, 3, 4]
n = len(processes)
burst_time = [5, 3, 8, 6]
arrival_time = [0, 1, 2, 3]

sjf_preemptive(processes, n, burst_time, arrival_time)
