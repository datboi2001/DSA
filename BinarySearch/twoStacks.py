import sys
def twoStacks(maxSum, a, b):
    # Write your code here
    # Write your code here
    count_a = count_b = 0
    ans = 0
    run_sum = 0
    for num in a:
        if run_sum + num > maxSum:
            break
        run_sum += num
        count_a += 1
    ans = count_a
    for i in range(len(b)):
        run_sum += b[i]
        count_b += 1
        while run_sum > maxSum and count_a != 0:
            run_sum -= a[count_a - 1]
            count_a -= 1
        if run_sum > maxSum:
            break
        ans = max(ans, count_a + count_b)
    return ans

print(twoStacks(10, [4,2,4,6,1], [2,1,8,5]))
        
