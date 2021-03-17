ackerman_dict = {}

def ackerman(m, n):
    if (m, n) in ackerman_dict:
        return ackerman_dict[(m, n)]
    if m < 1:
        ackerman_dict[(m, n)] = n + 1
        return n + 1
    elif m > 0 and n < 1:
        acker_var = ackerman(m -1, 1)
        ackerman_dict[(m, n)] = acker_var
        return ackerman(m -1, 1)
    else:
        acker_var = ackerman(m - 1, ackerman(m, n -1))
        ackerman_dict[(m, n)] = acker_var
        return acker_var
print(ackerman(3, 8))