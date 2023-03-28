def maximumPoints(k, costs):
    n = len(costs)
    points = 0
    total_cost = 0
    skipped_cost = float('inf')
    skipped = False
    for i in range(n):
        if not skipped and total_cost + costs[i] <= k:
            total_cost += costs[i]
            points += 1
        elif skipped and total_cost + costs[i] + skipped_cost <= k:
            total_cost += costs[i]
            skipped_cost = min(skipped_cost, costs[i-1])
        else:
            skipped = True
            skipped_cost = min(skipped_cost, costs[i])
    return points
