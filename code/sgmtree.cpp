#include <bits/stdc++.h>
using namespace std;

class sgmtree {
public:
  vector<ll> vals;
  vector<ll> tree;
  ll n;
  sgmtree(vector<ll> x) {
    vals=x;
    n=x.size();
    tree.assign(4*n+4,0);
    build(1,0,n-1);
  }
  ll que(ll L, ll R) {
    return que(1,0,n-1,L,R);
  }
  void update(ll ind, ll val) {
    vals[ind]=val;
    update(1,0,n-1,ind);
  }
private:
  ll I = 0; // I
  void build(ll node, ll l, ll r) {
    if (l==r) {tree[node]=vals[l]; return;}
    ll mid=(l+r)/2;
    build(2*node,l,mid);
    build(2*node+1,mid+1,r);
    tree[node]=tree[2*node]+tree[2*node+1]; // op
  }
  ll que(ll node, ll l, ll r, ll L, ll R) {
    if (l>R || r<L) return I; // I
    if (l>=L && r<=R) return tree[node];
    ll mid=(l+r)/2;
    return que(2*node,l,mid,L,R)+que(2*node+1,mid+1,r,L,R); // op
  }
  void update(ll node, ll l, ll r, ll ind) {
    if (l==r && l==ind) {tree[node]=vals[ind]; return;}
    if (l>ind || r<ind) return;
    ll mid=(l+r)/2;
    update(2*node,l,mid,ind);
    update(2*node+1,mid+1,r,ind);
    tree[node]=tree[2*node]+tree[2*node+1]; // Op
  }
};
