def funky_sum(a, b, mix):
    return (1 - mix) * b + mix * a


def total(n):
    if n < 0:
        return None;
    else:
        result = 0;
        for i in range(n + 1):
            result += i;
        return result;