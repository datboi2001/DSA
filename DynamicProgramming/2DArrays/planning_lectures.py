def planning_lectures(t: list[int], E: list[list[int]], M: int):
    """
    :param topic_times: the time to teach each topic. Note that you have to teach all the topics and teach them in
    order
    :param lecture_limit: the maximum time per lecture
    :param engagement_matrix: the engagement matrix. engagement_matrix[i][j] is the engagement when you cover
    topics i through j in the same lecture given that i <= j. You can assume that engagement_matrix[i][j] = -inf
    whenever topics i ... j do not fit into a single lecture spot
    :return the maximum total engagement
    """  

    # Main idea: We can use dynamic programming to solve this problem. Let dp[i] be the maximum engagement we can
    # achieve by teaching all the topics in order. Then, we can calculate dp[i] as follows:
    # dp[i] = max(dp[i], dp[j] + E[j][i-1]) where j < i and t[j] + ... + t[i-1] <= M
    # The base case is dp[0] = 0
    # The recurrence relation is dp[i] = max(dp[i], dp[j] + E[j][i-1]) where j < i and t[j] + ... + t[i-1] <= M
    # dp[j] is the maximum engagement we can achieve by teaching all the topics in order up to topic j
    # E[j][i-1] is the engagement when you cover topics j through i-1 in the same lecture given that j < i-1

    n = len(t)
    # dp[i] is the maximum engagement we can achieve by teaching all the topics in order
    dp = [-float('inf')] * (n + 1)
    # Base case: dp[0] = 0 since we can achieve 0 engagement by teaching 0 topics
    dp[0] = 0
    # Loop through all the possible combinations of topics 
    for i in range(1, n + 1):
        total_time = 0
        for j in range(i):
            # Calculate the total time to teach topics j through i
            total_time += t[j]
            # If the total time is greater than the lecture limit, we cannot teach topics j through i in the same
            # lecture
            if total_time > M:
                break
            # Update the maximum engagement we can achieve by teaching all the topics in order
            dp[i] = max(dp[i], dp[j] + E[j][i-1])
    # Return the maximum engagement we can achieve by teaching all the topics in order
    return dp[n]

# Sample inputs
if __name__ == '__main__':
    topic_times = [1, 2, 3, 4, 5]
    lecture_limit = 5
    engagement_matrix = [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 0, 0, 1, 2], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
    # The answer is 4
    print(planning_lectures(topic_times, engagement_matrix, lecture_limit))