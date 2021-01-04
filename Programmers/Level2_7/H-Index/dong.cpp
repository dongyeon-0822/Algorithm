#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end());
    int max = citations.back();
    
    int h_index = 0;
    for (int h_index = 0; h_index <= max; h_index++) {
        int count = 0;
        for (int i = 0; i < citations.size(); i++) {
            if (citations[i] >= h_index)
                count++;
        }
        if (count>=h_index) {
            answer = h_index;
        }
    }
    return answer;
}
\