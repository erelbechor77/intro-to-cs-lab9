
def max_free_time(tasks, total_duration):
    tasks.sort(key=lambda x: x[0])
    start_to_first=tasks[0][0]
    last_to_end=total_duration - tasks[-1][1]
    for i in range(2, len(tasks)):
        free_time=tasks[i][0]-tasks[i-1][1]
        if free_time>start_to_first:
            start_to_first=free_time
    a=max(start_to_first, last_to_end)
    return a
tasks = [[10, 15], [2, 5], [20, 30], [40, 45]]
total_duration = 50
print(max_free_time(tasks, total_duration))