#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());

    for (int i = 0; i < phone_book.size(); i++) {
        for (int j = i + 1; j < phone_book.size(); j++) {
            if (phone_book[i].size() < phone_book[j].size()) {
                int size = phone_book[i].size();
                if (phone_book[i] == phone_book[j].substr(0, size)) {
                    answer = false;
                    return answer;
                }
            }
        }
    }
    return answer;
}
int main() {
    vector<string> phone_book = { "12","123","1235","567","88" };
    cout << solution(phone_book);
}