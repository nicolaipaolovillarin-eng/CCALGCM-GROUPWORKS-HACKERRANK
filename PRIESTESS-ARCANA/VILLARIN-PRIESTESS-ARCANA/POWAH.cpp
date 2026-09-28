#include <bits/stdc++.h>
using namespace std;

const long long MOD = 10000000LL;

long long solve(long long e, long long t) {
    e %= MOD;
    long long result = 1;

    while (t > 0) {
        if (t & 1) {
            result = (result * e) % MOD;
        }

        e = (e * e) % MOD;
        t >>= 1;
    }

    return result;
}

int main() {
    long long e, t;
    cin >> e >> t;

    cout << solve(e, t) << '\n';
}
