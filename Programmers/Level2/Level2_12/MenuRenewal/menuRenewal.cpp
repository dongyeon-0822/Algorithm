#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector<vector<char>> menu(20, vector<char>(0));
    map<string, int> map;
    

    //교집합 구하고 그 길이가 course에 속하면 result하고 중복제거
    for (int i = 0; i < orders.size(); i++) {
        for (int j = 0; j < orders[i].size(); j++) {
            menu[i].push_back(orders[i][j]);
        }
        for (int j = 0; j < orders[i].size(); j++) {
            cout << menu[i][j];
        }
        cout << endl;
    }

    for (int i = 0; i < orders.size() - 1; i++) {
        for (int j = i + 1; j < orders.size(); j++) {
            vector<char> buff(menu[i].size() + menu[j].size());
            auto iter = set_intersection(menu[i].begin(), menu[i].end(), menu[j].begin(), menu[j].end(), buff.begin());
            buff.erase(iter, buff.end());
            for (int k = 0; k < buff.size(); k++) {
                cout << buff[k];
            }
            cout << endl;
            if (find(course.begin(), course.end(), buff.size()) != course.end()) {
                string temp = "";
                for (int j = 0; j < buff.size(); j++) {
                    temp += buff[j];
                }
                auto it = map.find(temp);
                if (it != map.end()) {
                    (it->second)++;
                }
                else {
                    map.insert({ temp,1 });
                }
            }
        }
    }
    for (int i = 0; i < map.size(); i++) {

    }
    
    sort(answer.begin(), answer.end());
    /*for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << " ";
    }*/
    //answer.erase(unique(answer.begin(), answer.end()), answer.end());
    
    return answer;
}
int main() {
    vector<string> orders = { "ABCFG", "AC", "CDE","ACDE","BCFG","ACDEH" };
    vector<int> course = { 2,3,4 };
    solution(orders, course);

}