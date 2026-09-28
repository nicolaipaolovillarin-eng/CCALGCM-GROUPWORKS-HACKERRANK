#include <bits/stdc++.h>
using namespace std;

class WaveletMatrix {
private:
    int n;
    int bits;

    vector<vector<int>> zeroPrefix;
    vector<int> zeroCount;

public:
    WaveletMatrix(const vector<int>& values, int alphabetSize) {
        n = values.size();

        bits = 1;
        while ((1LL << bits) < alphabetSize) {
            bits++;
        }

        zeroPrefix.assign(bits, vector<int>(n + 1));
        zeroCount.assign(bits, 0);

        vector<int> current = values;
        vector<int> next(n);

        for (int level = 0; level < bits; level++) {
            int bit = bits - 1 - level;

            for (int i = 0; i < n; i++) {
                bool isZero = ((current[i] >> bit) & 1) == 0;
                zeroPrefix[level][i + 1] =
                    zeroPrefix[level][i] + isZero;
            }

            int zeros = zeroPrefix[level][n];
            zeroCount[level] = zeros;

            int zeroPosition = 0;
            int onePosition = zeros;

            for (int value : current) {
                if (((value >> bit) & 1) == 0) {
                    next[zeroPosition++] = value;
                } else {
                    next[onePosition++] = value;
                }
            }

            current.swap(next);
        }
    }

    // Returns the 0-based kth smallest value in [left, right).
    int kthSmallest(int left, int right, int k) const {
        int answer = 0;

        for (int level = 0; level < bits; level++) {
            int bit = bits - 1 - level;

            int zerosBeforeLeft = zeroPrefix[level][left];
            int zerosBeforeRight = zeroPrefix[level][right];

            int zerosInRange =
                zerosBeforeRight - zerosBeforeLeft;

            if (k < zerosInRange) {
                left = zerosBeforeLeft;
                right = zerosBeforeRight;
            } else {
                k -= zerosInRange;
                answer |= (1 << bit);

                left = zeroCount[level] +
                       (left - zerosBeforeLeft);

                right = zeroCount[level] +
                        (right - zerosBeforeRight);
            }
        }

        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<long long> movie(n);

    for (int i = 0; i < n; i++) {
        long long runtime, credits;
        cin >> runtime >> credits;
        movie[i] = runtime - credits;
    }

    vector<long long> sortedValues = movie;
    sort(sortedValues.begin(), sortedValues.end());
    sortedValues.erase(
        unique(sortedValues.begin(), sortedValues.end()),
        sortedValues.end()
    );

    vector<int> compressed(n);

    for (int i = 0; i < n; i++) {
        compressed[i] = lower_bound(
            sortedValues.begin(),
            sortedValues.end(),
            movie[i]
        ) - sortedValues.begin();
    }

    WaveletMatrix wavelet(
        compressed,
        sortedValues.size()
    );

    int q;
    cin >> q;

    while (q--) {
        int s, e;
        long long budget, price;

        cin >> s >> e >> budget >> price;

        long long tickets = budget / price;
        int rangeLength = e - s + 1;

        if (tickets == 0) {
            cout << -1 << '\n';
            continue;
        }

        int watched = min<long long>(tickets, rangeLength);

        // kth largest = (rangeLength - watched)-th smallest
        int kthSmallestIndex = rangeLength - watched;

        int compressedAnswer =
            wavelet.kthSmallest(
                s,
                e + 1,
                kthSmallestIndex
            );

        cout << sortedValues[compressedAnswer] << '\n';
    }
}
