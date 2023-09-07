def inv_sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return 1/lst[0] + inv_sum_list(lst[1:])
