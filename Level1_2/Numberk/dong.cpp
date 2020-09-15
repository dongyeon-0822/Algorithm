#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> arr;
    
    for (int i = 0; i < commands.size(); i++) {
        int a = commands[i][0];
        int b = commands[i][1];
        int k = commands[i][2];

        arr.clear();
        arr.assign(array.begin() + a - 1, array.begin() + b);
        sort(arr.begin(), arr.end());
        answer.push_back(arr[k-1]);
    }

    return answer;
}
