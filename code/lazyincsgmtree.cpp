#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//This is a lazy sgmtree, update query increments 
//all values between L and R
class sgmtree {
public:
  vector<ll> vals;
  vector<ll> tree;
  vector<ll> lazyupdts;
  ll n;
  sgmtree(vector<ll> x) {
    vals=x;
    n=x.size();
    tree.assign(4*n+4,0);
    lazyupdts.assign(4*n+4,0);
    build(1,0,n-1);
  }
  ll que(ll L, ll R) {
    return que(1,0,n-1,L,R);
  }
  void update(ll L, ll R, ll val) {
    //Inc with val for all nodes L to R
    update(1,0,n-1,L,R,val);
  }
private:
  ll I = -9999999; // I
  void build(ll node, ll l, ll r) {
    if (l==r) {tree[node]=vals[l]; return;}
    ll mid=(l+r)/2;
    build(2*node,l,mid);
    build(2*node+1,mid+1,r);
    tree[node]=max(tree[2*node],tree[2*node+1]); // op
  }
  ll que(ll node, ll l, ll r, ll L, ll R) {
    if (l>R || r<L) return I; // I
    if (l>=L && r<=R) return tree[node];
    ll mid=(l+r)/2;
    if (lazyupdts[node]!=0) {
      update(node*2,l,mid,l,mid,lazyupdts[node]);
      update(2*node+1,mid+1,r,mid+1,r,lazyupdts[node]);
      lazyupdts[node]=0;
    }
    return max(que(2*node,l,mid,L,R),que(2*node+1,mid+1,r,L,R)); // op
  }
  void update(ll node, ll l, ll r, ll L, ll R, ll val) {
    if (l>R || r<L) return;
    if (l>=L && r<=R) {
      //Lazy update this
      tree[node]+=val; //Op
      if (l==r) {return;}
      lazyupdts[node]+=val;
      return;
    }
    //if (l==r && l==ind) {tree[node]=vals; return;}
    //if (l>ind || r<ind) return;
    ll mid=(l+r)/2;
    if (lazyupdts[node]!=0) { //propagate down current lazyvalues
      update(2*node,l,mid,l,mid,lazyupdts[node]);
      update(2*node+1,mid+1,r,mid+1,r,lazyupdts[node]);
      lazyupdts[node]=0;
    }
    update(2*node,l,mid,L,R,val);
    update(2*node+1,mid+1,r,L,R,val);
    tree[node]=max(tree[2*node],tree[2*node+1]); // Op
  }
};
