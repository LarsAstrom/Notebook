#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool comp(pair<ll,ll> p1, pair<ll,ll> p2){
    if(p1.second != p2.second) return p1.second < p2.second;
    return p1.first < p2.first;
}

/**
 *  Returns the number of jobs that can be completed with k
 *  working stations. jobs is a vector of pairs, that contain
 *  start and end time.
 *
 *  Time-complexity: O(n log k), where n is the number of jobs
 *  Space-complexity: O(n + k)
 */
int schedule(vector<pair<ll,ll> > jobs, int k){
    int no_scheduled = 0;
    sort(jobs.begin(),jobs.end(),comp);
    set<pair<ll,int> > stations;
    for(int i = 0; i < k; i++) stations.insert({0,i});
    for(auto job : jobs){
        auto it = stations.lower_bound({job.first,k});
        if(it == stations.begin()) continue;
        pair<ll,int> toins = {job.second,(--it)->second};
        stations.erase(it);
        stations.insert(toins);
        no_scheduled++;
    }
    return no_scheduled;
}

int main(){
    int n,k; cin >> n >> k;
    vector<pair<ll,ll> > jobs;
    for(int i = 0; i < n; i++){
        ll s,t; cin >> s >> t; jobs.push_back({s,t});
    }
    cout << schedule(jobs,k) << endl;
}
