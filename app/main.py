def newman_conway_helper(n, memo):
    # base case, return 1 for P(1) and P(2)
    if n == 1 or n == 2:
        return 1

    # grab P(N) from our memo if it exists
    if len(memo) > n:
        return memo[n]

    # P(n) = P(P(n - 1)) + P(n - P(n - 1))
    p_of_n_minus_one = memo[n - 1]
    return newman_conway_helper(p_of_n_minus_one, memo) + newman_conway_helper(n - p_of_n_minus_one, memo)
    
def newman_conway(n):
    # edge case, return empty list for any input <= 0
    if n <= 0:
        return []

    # set our resulting array/memo
    # offset by 1 so each index matches the resulting
    # output, i.e. P(1) = result[1], P(2) = result[2]...
    result = [None, 1, 1]
    # if we are looking for P(1) or P(2), return 
    # the list of results accordingly
    if n <= 2:
        return result[1: n + 1]

    # starting from P(3), start accumulating our values
    for i in range(3, n + 1):
        # calculate the next number via the helper
        next_num = newman_conway_helper(i, result)
        # append the next number to our list of results
        result.append(next_num)
        # since we offset our list by 1, return from the first element to the end of the list
    return result[1:]