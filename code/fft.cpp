#include <bits/stdc++.h>
#include <math.h>
using namespace std;
typedef long long ll;

vector<complex<double> > omega;
vector<ll> r;
ll n;
double pi;

vector<complex<double> > fft(vector<complex<double> > inp){
    vector<complex<double> > ret;
    for(ll i = 0; i < (ll) inp.size(); i++) ret.push_back(inp[r[i]]);
    for(ll k = 1; k < n; k = k*2){
        for(ll i = 0; i < n; i = i + 2*k){
            for(ll j = 0; j < k; j++){
                complex<double> z = omega[j*n/(2*k)] * ret[i + j + k];
                ret[i + j + k] = ret[i + j] - z;
                ret[i + j] = ret[i + j] + z;
            }
        }
    }
    return ret;
}

vector<complex<double> > ifft(vector<complex<double> > inp){
    vector<complex<double> > temp;
    temp.push_back(inp[0]);
    for(ll i = n-1; i > 0; i--) temp.push_back(inp[i]);
    temp = fft(temp);
    for(ll i = 0; i < n; i++) temp[i] /= n;
    return temp;
}

int main(){
    pi = atan(1)*4;
    ll T, deg1, deg2; cin >> T >> deg1;
    vector<complex<double> > a1,a2;
    for(int i = 0; i <= deg1; i++){double c; cin >> c; a1.push_back({c,0});}
    cin >> deg2;
    for(int i = 0; i <= deg2; i++){double c; cin >> c; a2.push_back({c,0});}
    n = 2; ll counter = 1;
    while (n <= deg1 + deg2){n *= 2; counter++;}
    while ((ll) a1.size() < n) a1.push_back({0,0});
    while ((ll) a2.size() < n) a2.push_back({0,0});

    r.push_back(0);
    for(ll i = 1; i < n; i++) r.push_back(r[i/2]/2 + ((i&1) << (counter-1)));

    for(ll i = 0; i < n; i++) omega.push_back({cos(2*i*pi/n),sin(2*i*pi/n)});
    vector<complex<double> > b1, b2;
    b1 = fft(a1); b2 = fft(a2);
    vector<complex<double> > c;
    for(ll i = 0; i < n; i++) c.push_back(b1[i]*b2[i]);
    
    vector<complex<double> > out = ifft(c);
    vector<ll> outs;
    for(ll i = 0; i <= deg1 + deg2; i++) outs.push_back(round(out[i].real()));

    cout << deg1 + deg2 << endl;
    for(ll i = 0; i < (ll) outs.size(); i++) cout << outs[i] << " ";
    cout << endl;
    return 0;
}
