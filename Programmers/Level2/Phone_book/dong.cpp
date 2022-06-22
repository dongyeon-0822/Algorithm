#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());

    for (int i = 0; i < phone_book.size() - 1; i++) {
        if (phone_book[i] == phone_book[i+1].substr(0, phone_book[i].size())) {
            answer = false;
            return answer;
        }
    }
    return answer;
}
int main() {
    vector<string> phone_book = { "12","123","1235","567","88" };
    cout << solution(phone_book);
}