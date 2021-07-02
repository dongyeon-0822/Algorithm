#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector<vector<char>> buffer;
    vector<vector<char>> _buffer;
    vector<vector<char>> menu(20, vector<char>(0));
    map<string, int> m;
    
    for (int i = 0; i < orders.size(); i++) {
        sort(orders[i].begin(), orders[i].end());
        for (int j = 0; j < orders[i].size(); j++) {
            menu[i].push_back(orders[i][j]);
        }
    }
    
    //나올 수 있는 조합 buffer에 저장
    for (int i = 0; i < orders.size() - 1; i++) {
        for (int j = i + 1; j < orders.size(); j++) {
            vector<char> buff(menu[i].size() + menu[j].size());
            auto iter = set_intersection(menu[i].begin(), menu[i].end(), menu[j].begin(), menu[j].end(), buff.begin());
            buff.erase(iter, buff.end());
            if (buff.size() > 1) {
                buffer.push_back(buff);
            }
        }
    }
    sort(buffer.begin(), buffer.end());
    buffer.erase(unique(buffer.begin(), buffer.end()), buffer.end());

    for (int i = 0; i < buffer.size(); i++) {
        vector<char> c;
        vector<int> flag;
        for (int j = 0; j < buffer[i].size(); j++) {
            c.push_back(buffer[i][j]);
        }
        for (int k = 0; k < course.size() && course[k] < c.size(); k++) {
            for (int j = 0; j < c.size() - course[k]; j++) {
                flag.push_back(0);
            }
            for (int j = 0; j < course[k]; j++) {
                flag.push_back(1);
            }
            do {
                vector<char> buff;
                for (int j = 0; j < flag.size(); j++) {
                    if (flag[j] == 1) {
                        buff.push_back(c[j]);
                    }
                }
                _buffer.push_back(buff);
                buff.clear();
            } while (next_permutation(flag.begin(), flag.end()));
        }
        flag.clear();
        c.clear();
    }
    buffer.insert(buffer.end(), _buffer.begin(), _buffer.end());
    sort(buffer.begin(), buffer.end());
    buffer.erase(unique(buffer.begin(), buffer.end()), buffer.end());

    for (int i = 0; i < buffer.size(); i++) {
        for (int j = 0; j < buffer[i].size(); j++) {
            cout << buffer[i][j];
        }cout << endl;
    }

    //각 조합의 개수를 세고 map에 insert
    for (int i = 0; i < buffer.size(); i++) {
        int count = 0;
        string temp1 = "";
        for (int k = 0; k < buffer[i].size(); k++) {
            temp1 += buffer[i][k];
        }
        for (int j = 0; j < orders.size(); j++) {
            vector<char> buff(buffer[i].size() + menu[j].size());
            auto iter = set_intersection(buffer[i].begin(), buffer[i].end(), menu[j].begin(), menu[j].end(), buff.begin());
            buff.erase(iter, buff.end());

            string temp2 = "";
            for (int k = 0; k < buff.size(); k++) {
                temp2 += buff[k];
            }
            if (temp1 == temp2) {
                count++;
            }
        }
        m.insert({ temp1,count });
    }
    for (auto iter = m.begin(); iter != m.end(); iter++) {
        cout << iter->first << " " << iter->second << endl;
    }

    //course의 시간 별로 가장 많은 것
    vector<pair<string,int>> q;
    for (int i = 0; i < course.size(); i++) {
        for (auto iter = m.begin(); iter != m.end(); iter++) {
            if ((iter->first).size() == course[i]) {
                if (q.empty()) {
                    q.push_back(make_pair(iter->first,iter->second));
                }
                else {
                    if (q.back().second == iter->second) {
                        q.push_back(make_pair(iter->first, iter->second));
                    }
                    else if (q.back().second < iter->second) {
                        q.clear();
                        q.push_back(make_pair(iter->first, iter->second));
                    }
                }
            }
        }
        for (int j = 0; j < q.size(); j++) {
            answer.push_back(q[j].first);
        }
        q.clear();
    }
    sort(answer.begin(), answer.end());
    
    return answer;
}
int main() {
    vector<string> orders = { "ABCFG", "AC", "CDE","ACDE","BCFG", "ACDEH"};
    vector<int> course = { 2,3,4 };
    solution(orders, course);

}