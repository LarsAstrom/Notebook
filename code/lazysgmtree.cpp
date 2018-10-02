//WIP
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//This is a lazy sgmtree, but updates doesnt inc, it sets all values in segment
class sgmtree {
public:
  vector<int> vals;
  vector<int> tree;
  vector<int> lazyupdts;
  int n;
  sgmtree(vector<int> x) {
    vals=x;
    n=x.size();
    tree.assign(3*n+4,0);
    lazyupdts.assign(3*n+4,-1);
    build(1,0,n-1);
  }
  int que(int L, int R) {
    return que(1,0,n-1,L,R);
  }
  void update(int L, int R, int val) {
    //vals[ind]=val; //Set value val for all nodes L to R
    update(1,0,n-1,L,R,val);
  }
private:
  int I = -9999999; // I
  void build(int node, int l, int r) {
    if (l==r) {tree[node]=vals[l]; return;}
    int mid=(l+r)/2;
    build(2*node,l,mid);
    build(2*node+1,mid+1,r);
    tree[node]=max(tree[2*node],tree[2*node+1]); // op
  }
  int que(int node, int l, int r, int L, int R) {
    if (l>R || r<L) return I; // I
    if (l>=L && r<=R) return tree[node];
    int mid=(l+r)/2;
    if (lazyupdts[node]!=-1) {
      update(node*2,l,mid,l,mid,lazyupdts[node]);
      update(2*node+1,mid+1,r,mid+1,r,lazyupdts[node]);
      lazyupdts[node]=-1;
    }
    return max(que(2*node,l,mid,L,R),que(2*node+1,mid+1,r,L,R)); // op
  }
  void update(int node, int l, int r, int L, int R, int val) {
    if (l>R || r<L) return;
    if (l>=L && r<=R) {
      //Lazy update this
      tree[node]=val; //Op
      if (l==r) {return;}
      lazyupdts[node]=val;
      return;
    }
    //if (l==r && l==ind) {tree[node]=vals; return;}
    //if (l>ind || r<ind) return;
    int mid=(l+r)/2;
    update(2*node,l,mid,L,R,val);
    update(2*node+1,mid+1,r,L,R,val);
    tree[node]=max(tree[2*node],tree[2*node+1]); // Op
  }
};
int main() {   //0 1 2 3 4 5 6 7  8 9
  vector<int> x={1,5,5,5,2,4,3,32,2,15};
  sgmtree s(x);
  cout << s.que(0,9) << endl; //32;
  cout << s.que(2,5) << endl; //5
  s.update(0,4,10);
  cout << s.que(4,5) << endl; //10
  cout << s.que(5,6) << endl; //4
  s.update(4,8,7);
  cout << s.que(4,8) << endl; //7
  cout << s.que(8,9) << endl; //15
}
