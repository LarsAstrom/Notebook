// Reads in an unknown number of rows with unknown number of words
string line;
string word;

while (getline(cin, line)){
  stringstream ss(line);
  while(getline(ss, word, ' ')){
    cout << word << endl;
  }
  cout << "________________________" << endl;
}


//Reads ints until end of file
int k;

while (cin >> k){
   cout << k << endl;
}
