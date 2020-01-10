def distance(strand_a, strand_b):
    i = 0
    if len(strand_a) == len(strand_b):
        for j in range(len(strand_a)):
            if strand_a[j] != strand_b[j]:
                i += 1
    else:
        raise ValueError('ValueError')
    return i
