#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll INF = 1e18;

struct Edge{
    int node;
    ll dist;
};

class Graph {
public:
    int V;
    vector<vector<Edge> > adj;
    Graph(int V){
        this->V = V;
        adj.assign(V, vector<Edge>());
    }

    void addEdge(int from, int to, ll dist){
        adj[from].push_back({to, dist}); 
    }
    
    pair<ll,int> bellmanFord(int source, int sink){
        vector<int> numVisits(V,0);
        vector<int> dist(V, INF);
        dist[source] = 0;
        vector<bool> inqueue(V,false);
        queue<int> que;
        que.push(source);
        
        while(!que.empty()){
            int u = que.front();
            que.pop();
            numVisits[u]++;
            if(numVisits[u] == V) return {dist[sink],u};
            inqueue[u] = false;
            for (int i=0;i<adj[u].size();i++){
                Edge e = adj[u][i];
                int v = e.node;
                ll ndist = dist[u] + e.dist;
                if (dist[v] > ndist){
                    dist[v] = ndist;
                    if (!inqueue[v]){
                        inqueue[v] = true;
                        que.push(v);
                    }
                }
            }
        }
        return {dist[sink],-1};
    }
};
int main(){
    int N,M,Q,S; cin >> N >> M >> Q >> S;
    while(N != 0 && M != 0 && Q != 0){
        Graph G(N);
        for(int i = 0; i < M; i++){
            int u,v; ll w; cin >> u >> v >> w;
            G.addEdge(u,v,w);
        }
        
        cin >> N >> M >> Q >> S;
    }
    return 0;
}
