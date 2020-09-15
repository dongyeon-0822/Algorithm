#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    vector<int>::iterator p;
    int sum = 0;

    for (int i = 0; i < numbers.size()-1; i++) {
        for (int j = i+1; j < numbers.size(); j++) {
            sum = numbers[i] + numbers[j];
            p = find(answer.begin(), answer.end(), sum);
            if (p == answer.end())
                answer.push_back(sum);
        }
    }
    sort(answer.begin(), answer.end());

    return answer;
}
int main() {
    vector<int> numbers = { 2,1,3,4,1 };

    cout << solution(numbers);
}