#include <bits/stdc++.h>
using namespace std;

#define MAX_N 100000

int n, k;
int d_i[MAX_N], s_i[MAX_N];
int answers[MAX_N];
int answer_line_count = 0;

void solve() {
    vector<long long> health(n);

    for (int i = 0; i < n; i++) {
        health[i] = s_i[i];
    }

    int attack = 0;

    while (true) {
        for (int i = 0; i < n; i++) {
            health[i] -= d_i[attack];
        }

        int standing = 0;

        for (int i = 0; i < n; i++) {
            if (health[i] > 0) {
                standing++;
            }
        }

        answers[answer_line_count++] = standing;

        if (standing == 0) {
            break;
        }

        attack = (attack + 1) % k;
    }
}

int main() {
    scanf("%d%d", &n, &k);

    for (int i = 0; i < k; i++) {
        scanf("%d", &d_i[i]);
    }

    for (int i = 0; i < n; i++) {
        scanf("%d", &s_i[i]);
    }

    solve();

    for (int i = 0; i < answer_line_count; i++) {
        printf("%d\n", answers[i]);
    }
}
