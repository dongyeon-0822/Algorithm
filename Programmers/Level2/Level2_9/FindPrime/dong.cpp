#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

bool IsPrime(int n){
    if (n <= 1) 
        return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if ((n % i) == 0) 
            return false;
    }
    return 1;
}
int solution(string numbers) {
    int answer = 0;
    
    vector<int> number;
    for (int i = 0; i < numbers.size(); i++) {
        number.push_back(numbers[i]);
    }
    sort(number.begin(), number.end());

    set<int> num;
    do {
        string s = "";
        for (int i = 0; i < number.size(); i++) {
            s += number[i];
            num.insert(stoi(s));
        }
    } while (next_permutation(number.begin(), number.end()));
    
    for (auto it = num.begin(); it != num.end(); it++) {
        if (IsPrime(*it))
            answer++;
    }
    return answer;
}
int main() {
    string s = "011";
    solution(s);
}