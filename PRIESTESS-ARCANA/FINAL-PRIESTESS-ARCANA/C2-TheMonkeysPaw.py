import sys
from array import array

read = sys.stdin.buffer.readline

n = int(read())

durations = []
for _ in range(n):
    runtime, credits = map(int, read().split())
    durations.append(runtime - credits)

# Coordinate compression
sorted_values = sorted(set(durations))
compression = {value: i for i, value in enumerate(sorted_values)}
compressed = [compression[value] for value in durations]

m = len(sorted_values)
bits = max(1, (m - 1).bit_length())

prefixes = []
zero_counts = []

current = compressed

# Build wavelet matrix
for shift in range(bits - 1, -1, -1):
    mask = 1 << shift
    prefix = array("I", [0])
    zeros_part = []
    ones_part = []
    zero_count = 0

    for value in current:
        if value & mask:
            ones_part.append(value)
            prefix.append(zero_count)
        else:
            zeros_part.append(value)
            zero_count += 1
            prefix.append(zero_count)

    prefixes.append(prefix)
    zero_counts.append(zero_count)
    current = zeros_part + ones_part


def kth_smallest(left, right, k):
    """0-based kth smallest value in [left, right)."""
    answer = 0

    for level in range(bits):
        prefix = prefixes[level]

        zeros_before_left = prefix[left]
        zeros_before_right = prefix[right]
        zeros_in_range = zeros_before_right - zeros_before_left

        if k < zeros_in_range:
            left = zeros_before_left
            right = zeros_before_right
        else:
            k -= zeros_in_range
            answer |= 1 << (bits - 1 - level)

            left = zero_counts[level] + (
                left - zeros_before_left
            )
            right = zero_counts[level] + (
                right - zeros_before_right
            )

    return answer


q = int(read())
output = []

for _ in range(q):
    s, e, budget, price = map(int, read().split())

    tickets = budget // price
    length = e - s + 1

    if tickets == 0:
        output.append("-1")
        continue

    watched = min(tickets, length)

    # kth largest is the (length - watched)-th smallest
    compressed_answer = kth_smallest(
        s,
        e + 1,
        length - watched
    )

    output.append(str(sorted_values[compressed_answer]))

sys.stdout.write("\n".join(output))
