#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    bool available;
    int index;
    
    for (int i = 0; i < skill_trees.size(); i++) {
        available = true;
        int count = 0; 
        for (int j = 0; j < skill_trees[i].size(); j++) {
            index = skill.find(skill_trees[i][j]);
            if (index == -1) continue;
            else if (count < index) {
                available = false;
                break;
            }
            else if (count == index)
                count++;
        }
        if (available) answer++;
    }

    return answer;
}