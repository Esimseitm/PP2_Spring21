#include<iostream>
using namespace std;
int main()
{
    string s = "!/.6;;0041^_^ 1337EVOL228 33HTIW77 ,44NAHKILA55 55MORF13 ! 25TSEB44 667EHT777 322LLA244432 UOY 2HSIW3 ,4YADHTRIB 56YPPAH7";
    int n = s.size() - 1;
    for(int i=n; i >= 0; i--) {
        if(!('0' <= s[i] && s[i] <= '9')) {
            if('A' <= s[i] && s[i] <= 'Z' || s[i] == 32 || s[i] == 44 || s[i] == 33) {
                cout << s[i];
            }
        }
    }
    cout << endl;
    cout << "Made by Alikhan Gubayev, FIT 25'BD" << endl;

    return 0;
}