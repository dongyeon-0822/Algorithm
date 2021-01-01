#include <vector>
#include <iostream>
using namespace std;

bool isPrime(int n) {
    for (int j = 2; j < n; j++) {
        if (n % j == 0)
            return false;
    }return true;
}
int solution(vector<int> nums) {
    int answer = 0;
    vector<int> comb;

    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                comb.push_back(nums[i] + nums[j] + nums[k]);
            }
        }
    }
    for (int i = 0; i < comb.size(); i++) {
        if (isPrime(comb[i]))
            answer++;
    }
    return answer;
}