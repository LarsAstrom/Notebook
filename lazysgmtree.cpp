//WIP


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
    return(1,0,n-1,L,R);
  }
  void update(int L, int R, int val) {
    vals[ind]=val;
    update(1,0,n-1,ind);
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
    return max(que(2*node,l,mid,L,R),que(2*node+1,mid+1,r,L,R)); // op
  }
  void update(int node, int l, int r, int L, int R, int val) {
    if (l>R || r<L) return;
    if (l>=L && r<=R) {
      //Lazy update this
      lazyupdts(node)=val;
      return;
    }
    //if (l==r && l==ind) {tree[node]=vals; return;}
    //if (l>ind || r<ind) return;
    int mid=(l+r)/2;
    update(2*node,l,mid,ind);
    update(2*node+1,mid+1,r,ind);
    tree[node]=max(tree[2*node],tree[2*node+1]); // Op
  }
};
