def count_partition(n, k):
    ''' nuumber of partitions of n, using parts upto k (all parts are positive)'''
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        with_m = count_partition(n - k, k)
        without_m = count_partition(n, k - 1)
        return with_m + without_m
