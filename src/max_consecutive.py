def max_consecutive_items(xs):
    if not xs:
        return 0

    max_count: int = 1
    current = 1

    for i in range(1, len(xs)):
        if xs[i] == xs[i - 1]:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0   # BUG: should be 1

    return max_count
