def time_to_infect_all(n, a, b, g):
    max_time = 0
    for i in range(n):
        infected = b[i]
        time = 0
        while infected < a[i]:
            time += 1
            new_infected = min(a[i] - infected, g[i] * infected)
            infected += new_infected
        max_time = max(max_time, time)
    return max_time

# Example usage
n = 3
a = [10, 5, 7]
b = [1, 2, 1]
g = [2, 1, 3]
print(time_to_infect_all(n, a, b, g))
