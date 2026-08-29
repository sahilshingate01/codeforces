#include<bits/stdc++.h>
using namespace std;

int R, C;
int A[105][105], B[105][105];

void solveCol(int i, int j) {
    if (j == C) {
        cout << "\n";
        return;
    }
    if (j == 0)
        cout << A[i][j] + B[i][j];
    else
        cout << " " << A[i][j] + B[i][j];
    solveCol(i, j + 1);
}

void solveRow(int i) {
    if (i == R) return;
    solveCol(i, 0);
    solveRow(i + 1);
}

int main(){
    cin >> R >> C;
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            cin >> A[i][j];
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            cin >> B[i][j];
    solveRow(0);
}