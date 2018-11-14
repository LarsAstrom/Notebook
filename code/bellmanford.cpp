#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll INF = 1e18;

struct Edge{
    int from,to;
    ll d;
};

class BellmanFord{
public:
    vector<ll> dists;
    int N; 
    vector<vector<int> > adj;
    vector<Edge> edgs; 
    BellmanFord(int N){
        this->N = N;
        adj.assign(N,vector<int>());
        dists.assign(N,INF);
    }
    //Edges are directed.
    void addEdge(int from, int to, ll d){
        adj[from].push_back(to);
        edgs.push_back({from,to,d});
    }
    void bellmanFord(int s){
        dists[s] = 0;
        for(int i = 0; i < N-1; i++){
            for(auto e : edgs){
                int u = e.from, v = e.to; ll w = e.d;
                if(dists[u] + w < dists[v]) dists[v] = dists[u]+w;
            }
        }
        //Skip if no negative cycles are guaranteed.
        for(auto e : edgs){
            int u = e.from, v = e.to; ll w = e.d;
            if(dists[v] == -INF) continue;
            if(dists[u] + w < dists[v] && dists[v] < INF/2) bfs(v);
        }
        for(int i = 0; i < N; i++){
            if(dists[i] > INF/2) dists[i] = INF;
        }
    }
    //Skip if no negative cycles are guaranteed.
    void bfs(int cur){
        vector<bool> vis(N,false);
        queue<int> q; q.push(cur);
        vis[cur] = true;
        while(!q.empty()){
            int c = q.front(); q.pop();
            dists[c] = -INF;
            for(auto ne : adj[c]){
                if(!vis[ne]){
                    vis[ne]=true; 
                    q.push(ne);
                }
            }
        }
    }
};
