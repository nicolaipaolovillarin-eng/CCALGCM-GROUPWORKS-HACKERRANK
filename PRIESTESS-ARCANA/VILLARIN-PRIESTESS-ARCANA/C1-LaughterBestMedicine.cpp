#include <bits/stdc++.h>
using namespace std;

using u128 = __uint128_t;

char solve(int n, unsigned long long k) {
    if (n == 0) return 'H';
    if (n == 1) return 'A';

    /*
       Lengths are capped at k + 1.
       This is enough because we only need to know whether
       a block length is greater than k.
    */
    constexpr int LIMIT = 128;
    u128 cap = static_cast<u128>(k) + 1;

    array<u128, LIMIT + 1> length{};

    length[0] = 1;
    length[1] = 1;

    for (int i = 2; i <= LIMIT; i++) {
        u128 sum = length[i - 1] + length[i - 2];
        length[i] = min(cap, sum);
    }

    int firstLarge = 0;
    while (length[firstLarge] < cap) {
        firstLarge++;
    }

    while (n >= 2) {
        /*
           For sufficiently large n, length[n - 2] is definitely
           greater than k, so we can skip several identical steps.
        */
        if (n - 2 >= firstLarge) {
            long long steps =
                (static_cast<long long>(n) - 2 - firstLarge) / 2 + 1;

            n -= static_cast<int>(2 * steps);
            continue;
        }

        u128 leftLength = length[n - 2];

        if (static_cast<u128>(k) < leftLength) {
            n -= 2;
        } else {
            k -= static_cast<unsigned long long>(leftLength);
            n -= 1;
        }
    }

    return n == 0 ? 'H' : 'A';
}

int main() {
    int n;
    unsigned long long k;

    cin >> n >> k;
    cout << solve(n, k) << '\n';
}
