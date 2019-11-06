#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct suffix {
    int index;  // To store original index
    int rank[2]; // To store ranks and next rank pair
};

int cmp(struct suffix a, struct suffix b) {
    return (a.rank[0] == b.rank[0])? (a.rank[1] < b.rank[1] ?1: 0):
           (a.rank[0] < b.rank[0] ?1: 0);
}

/*
Suffix array gives a sorting of the suffixes. Can be used to get longest
repeated substring, longest common substring, longest palindrome.
All of them are using LCP as well.
*/
vector<int> buildSuffixArray(string txt, int n) {
    struct suffix suffixes[n];
    for (int i = 0; i < n; i++) {
        suffixes[i].index = i;
        suffixes[i].rank[0] = (int) txt[i] - 'a';
        suffixes[i].rank[1] = ((i+1) < n)? (txt[i + 1] - 'a'): -1000;
    }
    sort(suffixes, suffixes+n, cmp);
    int ind[n];
    for (int k = 4; k < 2*n; k = k*2) {
        int rank = 0;
        int prev_rank = suffixes[0].rank[0];
        suffixes[0].rank[0] = rank;
        ind[suffixes[0].index] = 0;

        for (int i = 1; i < n; i++) {
            if (suffixes[i].rank[0] == prev_rank &&
                    suffixes[i].rank[1] == suffixes[i-1].rank[1]) {
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = rank;
            } else {
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = ++rank;
            }
            ind[suffixes[i].index] = i;
        }
        for (int i = 0; i < n; i++) {
            int nextindex = suffixes[i].index + k/2;
            suffixes[i].rank[1] = (nextindex < n)?
                                  suffixes[ind[nextindex]].rank[0]: -1;
        }
        sort(suffixes, suffixes+n, cmp);
    }

    vector<int>suffixArr;
    for (int i = 0; i < n; i++)
        suffixArr.push_back(suffixes[i].index);

    return  suffixArr;
}

/*
Returns the longest common prefix between two consecutive suffixes from
the suffix array.
*/
vector<ll> longestCommonPrefix(string txt, vector<int> suffixArr) {
    int n = (int) suffixArr.size();

    vector<ll> lcp(n, 0);
    vector<int> invSuff(n, 0);
    for (int i=0; i < n; i++) invSuff[suffixArr[i]] = i;

    int k = 0;
    for (int i=0; i<n; i++) {
        if (invSuff[i] == n-1) {
            k = 0;
            continue;
        }
        int j = suffixArr[invSuff[i]+1];
        while (i+k<n && j+k<n && txt[i+k]==txt[j+k]) k++;

        lcp[invSuff[i]] = k;
        if (k>0) k--;
    }
    return lcp;
}
