#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
constexpr ll INF = 9999999999999;

class Treap {
public:
  ll prio, val,size;
  Treap *l, *r;
  Treap(ll v) {
    val=v;
    l=NULL;
    r=NULL;
    size=1;
    prio=(ll) rand();
  }
  void update() {
    size=1;
    if (l!=NULL) size += l->size;
    if (r!=NULL) size += r->size;
  }
  void print(){
    cout << "_______________" << endl;
    Hprint();
    cout << "_______________" << endl;
  }
  void Hprint() {
    if (l!=NULL) l->Hprint();
    cout << val << " " << prio << endl;
    if(r != NULL) r->Hprint();
  }
};

//Split on index
pair<Treap*, Treap*> splitIndex(Treap *cur, ll i) {
  if (i > cur->size) assert(false);
  Treap *left = cur->l;
  Treap *right = cur ->r;
  ll lsize = left != NULL ? left->size : 0L;
  if (lsize == i){
    cur->l = NULL;
    cur->update();
    return {left, cur};
  }
  if (lsize +1 == i) {
    cur->r = NULL;
    cur->update();
    return {cur,right};
  }
  if (lsize > i){
    auto p = splitIndex(left, i);
    cur->l = p.second;
    cur->update();
    return {p.first, cur};
  }
  auto p = splitIndex(right, i - lsize - 1);
  cur->r = p.first;
  cur->update();
  return {cur, p.second};
}
//Split on value
pair<Treap*, Treap*> split(Treap *cur, ll val){
  Treap *left = cur->l;
  Treap *right = cur ->r;
  if (cur->val >= val){
    if (left == NULL) return {NULL, cur};
    auto p = split(left, val);
    cur->l = p.second;
    cur->update();
    return {p.first, cur};
  }
  if (cur->val < val){
    if (right == NULL) return {cur, NULL};
    auto p = split(right, val);
    cur->r = p.first;
    cur->update();
    return {cur, p.second};
  }
}

Treap* meld(Treap *a, Treap *b) { // all in b is bigger than a
  if (a==NULL) return b;
  if (b == NULL) return a;
  if (a->prio < b->prio) { //a root
    a->r = (a->r == NULL) ? b : meld(a->r, b);
    a->update();
    return a;
  }
  //b root
  b->l = (b->l == NULL) ? a : meld(a, b->l);
  b->update();
  return b;
}

Treap* insert(Treap* a, ll val){
  if (a==NULL) return new Treap(val);
  auto p = split(a, val);
  Treap *t = new Treap(val);
  return meld(p.first, meld(t, p.second));
}

Treap* del(Treap *root, ll val) {
  pair<Treap*,Treap*> saker1 = split(root,val);
  if (saker1.second == NULL) return saker1.first;
  pair<Treap*,Treap*> saker2 = split(saker1.second,val+1);
  return meld(saker1.first,saker2.second);
}

pair<bool, Treap*> exists(Treap *root, ll val) {
  pair<Treap*,Treap*> firstSplit = split(root,val);
  if (firstSplit.second == NULL) return {false, firstSplit.first};
  pair<Treap*,Treap*> secondSplit = split(firstSplit.second,val+1);
  return {secondSplit.first != NULL,meld(firstSplit.first,
          meld(secondSplit.first,secondSplit.second))};
}

ll next(Treap *root, ll val){
  if(root == NULL) return INF;
  if(val >= root->val) return next(root->r,val);
  return min(root->val,next(root->l,val));
}

ll prev(Treap *root, ll val){
  if(root == NULL) return -INF;
  if(val > root->val) return max(root->val,prev(root->r,val));
  return prev(root->l,val);
}
