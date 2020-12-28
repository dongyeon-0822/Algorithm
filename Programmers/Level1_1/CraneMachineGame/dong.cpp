#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> get;

    for (int k = 0; k < moves.size(); k++) {
        int i = moves[k]-1;
        int j = 0;
        while (board[j][i] == 0) {
            j++;
            if (j == board.size()) break;
        }
        if (j==board.size()) continue;

        //우선 넣기
        get.push_back(board[j][i]);
        
        int l = get.size();
        if (l >= 2) {
            if (board[j][i] == get[l - 2]) {
                answer += 2;
                get.pop_back();
                get.pop_back();
            }
        }
        board[j][i] = 0;
    }
    return answer;
}
int main() {
    vector<vector<int>> board(
        {
            vector<int>({0,0,0,0,0}),
            vector<int>({0,0,1,0,3}),
            vector<int>({0,2,5,0,1}),
            vector<int>({4,2,4,4,2}),
            vector<int>({3,5,1,3,1})
        }
    );
    vector<int> moves({ 1,5,3,5,1,2,1,4 });

    int sol = solution(board, moves);
    cout << sol;
}