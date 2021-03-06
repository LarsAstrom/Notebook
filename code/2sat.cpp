#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;

class twosat{
public:
    //for variable i, two variables are assigned as 2*i and
    //2*i+1 in G. 2*i is i, and 2*i+1 is not i.
    //Note that this has to be taken care of when adding clauses.
    vector<vector<int> > G_forward, G_reverse;
    vector<int> x,y;
    ll N;
    twosat(ll var){
        N = var*2;
        G_forward.assign(N,vector<int>());
        G_reverse.assign(N,vector<int>());
        marked.assign(N,false);
        component.assign(N,-1);
    }
    //addClause(i,j) adds the clause from i to j. But negations have
    //to be considered in the main.
    void addClause(int i, int j){
        G_forward[i^1].push_back(j);
        G_forward[j^1].push_back(i);
        G_reverse[i].push_back(j^1);
        G_reverse[j].push_back(i^1);
        x.push_back(i); y.push_back(j);
    }
    bool solve(){
      for(int i = 0; i < N; i++)
          if(!marked[i]) dfsFirst(i);
      marked.assign(N, false);
      while(!stck.empty()){
        int v = stck.back();
        stck.pop_back();
        if (!marked[v]){
          counter++;
          dfsSecond(v);
        }
      }
      for(int i = 0; i < N; i+=2)
          if(component[i] == component[i+1]) return false;
      return true;
    }
private:
    vector<bool> marked;
    vector<int> stck,component;
    int counter = 0;
    void dfsFirst(int v){
        marked[v] = true;
        for(auto u : G_forward[v]){
            if(!marked[u]) dfsFirst(u);
        }
        stck.push_back(v);
    }
    void dfsSecond(int v){
        marked[v] = true;
        for(auto u : G_reverse[v])
            if(!marked[u]) dfsSecond(u);
        component[v] = counter;
    }
};
