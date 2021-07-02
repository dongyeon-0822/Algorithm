#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int znum = 0;
    int correct = 0;
    for (int i = 0; i < lottos.size(); i++) {
        if (lottos[i] == 0) {
            znum++;
        }
        else {
            for (int j = 0; j < win_nums.size(); j++) {
                if (lottos[i] == win_nums[j]) {
                    correct++;
                }
            }
        }
    }
    int max, min;
    if (znum + correct < 1)
        max = 6;
    else max = 7 - (znum + correct);
    if (correct < 1)
        min = 6;
    else min = 7 - correct;

    answer.push_back(max);
    answer.push_back(min);

    return answer;
}