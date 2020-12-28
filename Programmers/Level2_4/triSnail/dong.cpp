#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;

    int** array = new int* [n];
    for (int i = 0; i < n; i++) 
        array[i] = new int[i+1];

    int num = 1, x = -1, y = 0;
    for (int i = 0; i < n; i++) {
        switch (i%3) {
        case 0:
            for (int j = 0; j < n - i; j++)
                array[++x][y] = num++; 
            break;
        case 1:
            for (int j = 0; j < n - i; j++)
                array[x][++y] = num++;
            break;
        case 2:
            for (int j = 0; j < n - i; j++)
                array[--x][--y] = num++; 
            break;
        default: break;
        }
        
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i+1; j++) {
            answer.push_back(array[i][j]);
        }
    }

    for (int i = 0; i < n; i++) 
        delete[] array[i]; 
    delete[] array;

    return answer;
}

int main() {
    solution(4);
}