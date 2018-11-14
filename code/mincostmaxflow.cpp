#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll INF = 1e18;
// Finds mincost maxflow using a queue based bellmanford
// The queue based is a lot faster than normal bellmanford
 
struct Edge {
    int to;
    int flow;
    ll cap; //capacity
    ll cost;
    int rev; //reverse edge index
};

class Graph {
public:
    int V;
    vector<vector<Edge> > adj;
    Graph(int V){
        this->V = V;
        adj.assign(V, vector<Edge>());
    }
    void addEdge(int from, int to, ll c, ll cost){
        Edge e = {to, 0, c, cost, adj[to].size()}; 
        Edge rev = {from, 0, 0, -cost, adj[from].size()};
        adj[from].push_back(e);
        adj[to].push_back(rev);
    }
    // Find augumenting path and send flow
    // Returns added flow and added cost 
    pair<ll,ll> bellmanFord(int source, int sink){
        vector<ll> dist(V, INF);
        vector<int> prev(V,-1);
        vector<int> prevEdge(V,-1);
        vector<ll> curFlow(V,INF);
        dist[source] = 0;
        vector<bool> inqueue(V,false);
        queue<int> que;
        que.push(source);
        while(que.size()%V != 0){
            int u = que.front();
            que.pop();
            inqueue[u] = false;
            for (int i=0;i<adj[u].size();i++){
                Edge e = adj[u][i];
                if (e.flow >= e.cap){
                    continue;
                }
                int v = e.to;
                ll ndist = dist[u] + e.cost;
                if (dist[v] > ndist){
                    dist[v] = ndist;
                    prev[v] = u;
                    prevEdge[v] = i;
                    curFlow[v] = min(curFlow[u], e.cap - e.flow);
                    if (!inqueue[v]){
                        inqueue[v] = true;
                        que.push(v);
                    }
                }
            }
        }
        if (dist[sink] == INF) return {0,0};
        ll flow = curFlow[sink];
        int v = sink;
        while (v != source){
            adj[prev[v]][prevEdge[v]].flow += flow;
            adj[v][adj[prev[v]][prevEdge[v]].rev].flow -= flow;
            v = prev[v];
        }
        return {flow, flow * dist[sink]};
    }
    pair<ll,ll> minCostMaxFlow(int S, int T){
        ll flow = 0, cost = 0;
        pair<ll,ll> temp = bellmanFord(S,T);
        while(temp.first > 0){
            flow += temp.first; 
            cost += temp.second;
            temp = bellmanFord(S,T);
        }
        return {flow,cost};
    }
};
