#include <stdio.h>

int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};  // 相邻格子的x方向位移
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};  // 相邻格子的y方向位移

int main() {
    int n, m;
    scanf("%d %d", &n, &m);  // 输入行数和列数
    char grid[n][m + 1];  // 定义雷区矩阵

    // 输入雷区的每一行
    for (int i = 0; i < n; ++i) {
        scanf("%s", &grid[i]);
    }

    // 遍历每个格子
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '?') {
                int count = 0;  // 初始化雷数为0
                
                // 遍历九宫格中的8个相邻格子
                for (int k = 0; k < 8; ++k) {
                    int x = i + dx[k];  // 相邻格子的x坐标
                    int y = j + dy[k];  // 相邻格子的y坐标
                    
                    // 确保相邻格子在边界范围内，且是地雷
                    if (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == '*') {
                        count++;  // 如果是地雷，雷数+1
                    }
                }
                
                // 用雷数填充当前的 `?` 格子
                grid[i][j] = count + '0';
            }
        }
    }

    // 输出完整的雷区
    for (int i = 0; i < n; ++i) {
        printf("%s\n", grid[i]);
    }

    return 0;
}
