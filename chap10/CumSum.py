def cum_sum(list):
    new_list = []
    rolling_sum = 0
    for value in list:
        rolling_sum += value
        new_list.append(rolling_sum)
    return new_list


t = [1, 2, 3]
print(cum_sum(t))
