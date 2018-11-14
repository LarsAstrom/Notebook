#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class fwtree {
public:
  vector<ll> tree;
  ll n;
  fwtree(ll N) {
    n=N;
    tree.assign(n+1,0);
  }
  void update(ll ind, ll val) {
      ind++;
      while(ind <= n){
          tree[ind] += val;
          ind += ind&(-ind);
      }
  }
  ll que(ll ind) {
    ll ret = 0;
    ind++;
    while(ind > 0){
        ret += tree[ind];
        ind -= ind&(-ind);
    }
    return ret;
  }
};
