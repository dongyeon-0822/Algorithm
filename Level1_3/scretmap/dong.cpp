#include <iostream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<string> map1, map2;

    for (int i = 0; i < n; i++) {
        map1.push_back(bitset<16>(arr1[i]).to_string());
        map2.push_back(bitset<16>(arr2[i]).to_string());
    }
    for (int i = 0; i < n; i++) {
        string str = "";
        for (int j = 16 - n; j < 16; j++) {
            if (map1[i][j] == '1' || map2[i][j] == '1')
                str += "#";
            else str += " ";
        }
        answer.push_back(str);
    }
    return answer;
}