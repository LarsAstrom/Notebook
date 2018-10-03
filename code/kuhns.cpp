#include <bits/stdc++.h>

using namespace std;

int A;
int B;
vector<bool> used;
vector<vector<int> > G;
vector<int> M;
vector<bool> matchedA;

bool tryKuhn(int a){
  if (used[a]) return false;
  used[a] = true;

  for (auto b : G[a]){
    if (M[b] == -1) {
      M[b] = a;
      return true;
    }
  }
  for (auto b : G[a]){
    if (tryKuhn(M[b])) {
      M[b] = a;
      return true;
    }
  }
  return false;
}

void greedyMatching(){
  M.assign(B, -1);
  matchedA.assign(A, false);
  for (int i=0;i<A;i++){
    for (auto b : G[i]){
      if (M[b] == -1){
        M[b] = i;
        matchedA[i] = true;
        break;
      }
    }
  }
  return;
}

void matching(){
  greedyMatching();
  for (int i=0;i<A;i++){
    if (matchedA[i]) continue;
    used.assign(A, false);
    if(tryKuhn(i)) matchedA[i] = true;
  }
  return;
}



int main(){


  cin >> A >> B;
  G.assign(A, vector<int>());

  for (int i=0;i<A;i++){
    while (true){
      int k;
      cin >> k;
      if (k  == 0) break;
      G[i].push_back(k-1);
    }
  }

  matching();

  int ans = 0;
  for (auto a : M){
    if (a != -1) ans++;
  }
  cout << ans << endl;

  for (int i=0;i<B;i++){
    if (M[i] != -1){
      cout << M[i]+1 << " " << i + 1 << endl;
    }
  }

  return 0;
}
