/* Find bridges of graph in O(N+M) */

constexpr int N = 100010;
vector<int> G[N];
int L[N], H[N], ND[N], ID[N];

// Precomputes bridges of G
void compute_bridges(int cur, int par, int id) {
  ID[cur] = id;
  ND[cur] = 1;
  L[cur] = id;
  H[cur] = id;
  for (int v : G[cur]) {
    if (v == par) continue;
    if (L[v] == -1) {
      compute_bridges(v, cur, id + ND[cur]);
      ND[cur] += ND[v];
      H[cur] = max(H[cur], H[v]);
      L[cur] = min(L[v], L[cur]);
    }
    else{
      H[cur] = max(H[cur], ID[v]);
      L[cur] = min(L[cur], ID[v]);
    }
  }
}

// Assumes there is exactly one edge from a to b
bool is_bridge(int a, int b) {
  int w = (ID[a] > ID[b]) ? a : b;
  return L[w] == ID[w] && H[w] < ID[w] + ND[w];
}

// How to use
memset(&L, -1, sizeof(L));
compute_bridges(0, -1, 0);
