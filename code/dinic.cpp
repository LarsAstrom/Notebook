// C++ implementation of Dinic's Algorithm
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct Edge{
  ll v ;//to vertex
  ll flow ;
  ll C;//capacity
  ll rev;//reverse edge index
};
// Residual Graph
class Graph
{
public:
  ll V; // number of vertex
  ll *level ; // stores level of a node
  vector< Edge > *adj;
  Graph(ll V){
    adj = new vector<Edge>[V];
    this->V = V;
    level = new ll[V];
  }

  void addEdge(ll u, ll v, ll C){
    Edge a{v, 0, C, adj[v].size()};// Forward edge
    Edge b{u, 0, 0, adj[u].size()};// Back edge
    adj[u].push_back(a);
    adj[v].push_back(b); // reverse edge
  }

  bool BFS(ll s, ll t){
    for (ll i = 0 ; i < V ; i++)
        level[i] = -1;
    level[s] = 0;  // Level of source vertex
    list< ll > q;
    q.push_back(s);
    vector<Edge>::iterator i ;
    while (!q.empty()){
      ll u = q.front();
      q.pop_front();
      for (i = adj[u].begin(); i != adj[u].end(); i++){
        Edge &e = *i;
        if (level[e.v] < 0  && e.flow < e.C){
          level[e.v] = level[u] + 1;
          q.push_back(e.v);
        }
      }
    }
    return level[t] < 0 ? false : true; //can/cannot reach target
  }

  ll sendFlow(ll u, ll flow, ll t, ll start[]){
    // Sink reached
    if (u == t)
        return flow;
    // Traverse all adjacent edges one -by - one.
    for (  ; start[u] < adj[u].size(); start[u]++){
      Edge &e = adj[u][start[u]];
      if (level[e.v] == level[u]+1 && e.flow < e.C){
        // find minimum flow from u to t
        ll curr_flow = min(flow, e.C - e.flow);
        ll temp_flow = sendFlow(e.v, curr_flow, t, start);
        // flow is greater than zero
        if (temp_flow > 0){
          e.flow += temp_flow;//add flow
          adj[e.v][e.rev].flow -= temp_flow;//sub from reverse edge
          return temp_flow;
        }
      }
    }
    return 0;
  }
  ll DinicMaxflow(ll s, ll t){
    // Corner case
    if (s == t) return -1;
    ll total = 0;  // Initialize result
    while (BFS(s, t) == true){//while path from s to t
      // store how many edges are visited
      // from V { 0 to V }
      ll *start = new ll[V+1];
      // while flow is not zero in graph from S to D
      while (ll flow = sendFlow(s, 999999999, t, start))
        total += flow;// Add path flow to overall flow
    }
    return total;
  }
};


int main()
{
    ll N,M;
    cin >> N >> M;
    ll lo,hi;
    lo = -1;
    hi = (N+1)/2;
    vector<pair<ll,ll> > edgs;
    for(ll i = 0; i < M; i++){
        ll u,v;
        cin >> u >> v;
        edgs.push_back({u,v});
    }
    while (hi - lo > 1){
        Graph G(M+N+2);
        ll mid = (lo+hi)/2;
        for(ll i = 0; i < M; i++){
            G.addEdge(0,i+1,1);
        }
        for(ll i = 0; i < M; i++){
            ll u,v;
            u = edgs[i].first + M; v = edgs[i].second + M;
            G.addEdge(i+1,u,1);
            G.addEdge(i+1,v,1);
        }
        for(ll i = M+1; i <= M+N; i++){
            G.addEdge(i,M+N+1,mid);
        }
        if(G.DinicMaxflow(0,M+N+1)==M) hi = mid;
        else lo = mid;
        /*
        for(int i = 0; i <= N+M+1; i++){
            cout << "------------Node " << i << "-------------" << endl;
            for(int j = 0; j < G.adj[i].size(); j++){
                Edge a = G.adj[i][j];
                cout << "To: " << a.v << " " << a.flow << "/" << a.C << endl;
            }
        }
        */
    }

    Graph G(M+2+N);
    ll mid = hi;
    for(ll i = 0; i < M; i++){
        G.addEdge(0,i+1,1);
    }
    for(ll i = 0; i < M; i++){
        ll u,v;
        u = edgs[i].first + M; v = edgs[i].second + M;
        G.addEdge(i+1,u,1);
        G.addEdge(i+1,v,1);
    }
    for(ll i = M+1; i <= M+N; i++){
        G.addEdge(i,M+N+1,mid);
    }
    G.DinicMaxflow(0,M+N+1);
    cout << hi << endl;
    for(ll i = 1; i <= M; i++){
        if(G.adj[i][1].flow == 1) cout << 0 << " ";
        else cout << 1 << " ";
    }
    cout << endl;
    /*
    for(int i = 0; i <= N+M+1; i++){
        cout << "------------Node " << i << "-------------" << endl;
        for(int j = 0; j < G.adj[i].size(); j++){
            Edge a = G.adj[i][j];
            cout << "To: " << a.v << " " << a.flow << "/" << a.C << endl;
        }
    }
    */
    return 0;
}
