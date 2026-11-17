#include <iostream>
#include <cstring>
using namespace std;

#define INF 9999999
#define V 8 

// Матриця суміжності графа
int G[V][V] = {
    {0, 4, 1, 7, INF, INF, INF, INF},
    {4, 0, INF, 5, INF, 9, INF, INF},
    {1, INF, 0, INF, INF, INF, INF, 2},
    {7, 5, INF, 0, 3, INF, INF, INF},
    {INF, INF, INF, 3, 0, 2, 8, INF},
    {INF, 9, INF, INF, 2, 0, 7, 1},
    {INF, INF, INF, INF, 8, 7, 0, 6},
    {INF, INF, 2, INF, INF, 1, 6, 0}
};

int main() {
    int selected[V];
    memset(selected, false, sizeof(selected));
    int no_edge = 0;

    
    selected[0] = true;

    cout << "Edge" << " : " << "Weight" << endl;

    while (no_edge < V - 1) {
        int min = INF;
        int x = 0;
        int y = 0;

        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    if (!selected[j] && G[i][j] != INF && G[i][j] != 0) {
                        if (min > G[i][j]) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }
        
        cout << (x + 1) << " - " << (y + 1) << " : " << G[x][y] << endl;
        selected[y] = true;
        no_edge++;
    }
    return 0;
}
