#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class fwtree {
public:
  vector<ll> tree;
  ll n;
  fwtree(vector<ll> x) {
    n=x.size();
    tree = vector<ll>(n+1,0);
    for(int i = 0; i < n; i++) update(i,x[i]);
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
