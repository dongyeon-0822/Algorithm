#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> map;
    for (int i = 0; i < clothes.size(); i++) {
        if (map.count(clothes[i][1]) >= 1)
            map[clothes[i][1]]++;
        else
            map.insert(make_pair(clothes[i][1], 1));
    }
    for (auto it =map.begin(); it != map.end(); it++) {
        answer *= (it->second+1);
    }
    answer--;
    return answer;
}