#include <bits/stdc++.h>
using namespace std;

const string IMPOSSIBLE =
    "Sweet spot cannot be reached! Those cheeky developers!";

long double evaporation(
    long double z,
    long double d,
    long double k,
    long double a
) {
    long double sigmoid =
        1.0L / (1.0L + expl(-k * (z - 0.5L)));

    return 1.0L - powl(sigmoid, a) + d;
}

void solve(double s, double d, double k, double a) {
    const long double EPS = 1e-10L;

    long double target = s;

    long double valueAtZero =
        evaporation(0.0L, d, k, a);

    long double valueAtOne =
        evaporation(1.0L, d, k, a);

    if (target < valueAtOne - EPS ||
        target > valueAtZero + EPS) {
        cout << IMPOSSIBLE << '\n';
        return;
    }

    long double low = 0.0L;
    long double high = 1.0L;

    for (int iteration = 0; iteration < 150; iteration++) {
        long double mid = (low + high) / 2.0L;
        long double current =
            evaporation(mid, d, k, a);

        // The function is decreasing.
        if (current > target) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(12)
         << (low + high) / 2.0L << '\n';
}

int main() {
    int n;
    scanf("%d", &n);

    while (n--) {
        double s, d, k, a;
        scanf("%lf%lf%lf%lf", &s, &d, &k, &a);
        solve(s, d, k, a);
    }
}
