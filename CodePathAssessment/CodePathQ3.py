def counts(teamA, teamB):
    teamA.sort()
    result = []
    for i in range(len(teamB)):
        left, right = 0, len(teamA)
        while left < right:
            mid = (left + right) // 2
            if teamA[mid] > teamB[i]:
                right = mid
            else:
                left = mid + 1
        result.append(left)
    return result

print(counts([2, 10, 5, 4, 8], [3,1,7,8]))