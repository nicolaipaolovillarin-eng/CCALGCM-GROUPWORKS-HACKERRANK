#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long kx, ky;

    cin >> n >> kx >> ky;

    vector<long long> distances(n);

    for (int i = 0; i < n; i++) {
        long long x, y;
        cin >> x >> y;

        distances[i] =
            llabs(x - kx) + llabs(y - ky);
    }

    sort(distances.begin(), distances.end());

    int q;
    cin >> q;

    while (q--) {
        long long energy;
        cin >> energy;

        int answer = upper_bound(
            distances.begin(),
            distances.end(),
            energy
        ) - distances.begin();

        cout << answer << '\n';
    }
}
