def equalize_lengths(lst):
    max_len = max([len(s) for s in lst])
    new_lst = []
    for s in lst:
        if len(s) < max_len:
            s += '_' * (max_len - len(s))
        new_lst.append(s)
    return sorted(new_lst, key=lambda x: x.count('_'))
