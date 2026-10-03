from decimal import Decimal, getcontext

getcontext().prec = 50

OPERATIONS_PER_SECOND = Decimal(100000000)
LOG_2 = Decimal(2).ln()


def compute_ans(seconds):
    limit = Decimal(seconds) * OPERATIONS_PER_SECOND

    def can_sort(size):
        if size <= 1:
            return True

        value = Decimal(size)
        operations = value * (value.ln() / LOG_2)

        return operations <= limit

    low = 1
    high = 1

    while can_sort(high):
        high *= 2

    while low <= high:
        mid = (low + high) // 2

        if can_sort(mid):
            low = mid + 1
        else:
            high = mid - 1

    return high


n = int(input())
print(compute_ans(n))
