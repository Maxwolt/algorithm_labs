#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

const int INF = 1e9;
const int V = 8;

// Матриця ваг (варіант 21)
int W[V][V] = {
    {0,   4,   1,   7,   INF, INF, INF, INF},
    {4,   0,   INF, 5,   INF, 9,   INF, INF},
    {1,   INF, 0,   INF, INF, INF, INF, 2  },
    {7,   5,   INF, 0,   3,   INF, INF, INF},
    {INF, INF, INF, 3,   0,   2,   8,   INF},
    {INF, 9,   INF, INF, 2,   0,   7,   1  },
    {INF, INF, INF, INF, 8,   7,   0,   6  },
    {INF, INF, 2,   INF, INF, 1,   6,   0  }
};

// Рекурсивний вивід шляху за масивом попередників
void printPath(const vector<int>& pred, int v) {
    if (pred[v] == -1) {
        cout << v + 1;
        return;
    }
    printPath(pred, pred[v]);
    cout << " -> " << v + 1;
}

void dijkstra(int start) {
    vector<int> dist(V, INF);
    vector<int> pred(V, -1);
    vector<bool> visited(V, false);
    dist[start] = 0;

    for (int i = 0; i < V; ++i) {
        int u = -1;
        for (int j = 0; j < V; ++j) {
            if (!visited[j] && (u == -1 || dist[j] < dist[u])) {
                u = j;
            }
        }
        if (u == -1 || dist[u] == INF) break;
        visited[u] = true;

        for (int v = 0; v < V; ++v) {
            if (W[u][v] != INF && dist[u] + W[u][v] < dist[v]) {
                dist[v] = dist[u] + W[u][v];
                pred[v] = u;
            }
        }
    }

    cout << "--- Результати алгоритму Дейкстри від вершини " << start + 1 << " ---" << endl;
    for (int i = 0; i < V; ++i) {
        cout << "До вершини " << i + 1 << ": відстань = " << dist[i] << ", шлях: ";
        printPath(pred, i);
        cout << endl;
    }
}

void floyd() {
    int D[V][V];
    for (int i = 0; i < V; ++i)
        for (int j = 0; j < V; ++j)
            D[i][j] = W[i][j];

    for (int k = 0; k < V; ++k) {
        for (int i = 0; i < V; ++i) {
            for (int j = 0; j < V; ++j) {
                if (D[i][k] != INF && D[k][j] != INF && D[i][k] + D[k][j] < D[i][j]) {
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }

    cout << "\n--- Фінальна матриця найкоротших відстаней (Алгоритм Флойда D^8) ---" << endl;
    for (int i = 0; i < V; ++i) {
        for (int j = 0; j < V; ++j) {
            if (D[i][j] == INF) cout << setw(5) << "INF";
            else cout << setw(5) << D[i][j];
        }
        cout << endl;
    }
}

int main() {
    dijkstra(0);   // від вершини 1 (індекс 0)
    floyd();
    return 0;
}
