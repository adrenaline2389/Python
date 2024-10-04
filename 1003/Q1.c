#include <stdio.h>

// 求最大公约数（GCD）的欧几里得算法
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// 求最小公倍数（LCM）
int lcm(int a, int b) {
    return a * (b / gcd(a, b));
}

int main() {
    int n, a, b;
    int results[3][100];  // 三行分别存储三批数据的结果，每批最多 100 个结果
    int counts[3] = {0};  // 用来记录每批数据的结果个数
    int idx = 0;  // 用于记录当前批次

    // 第一批数据，已知 case 数量
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d %d", &a, &b);
        results[0][counts[0]++] = lcm(a, b);
    }

    // 第二批数据，以两个 0 结束
    while (1) {
        scanf("%d %d", &a, &b);
        if (a == 0 && b == 0) break;
        results[1][counts[1]++] = lcm(a, b);
    }

    // 第三批数据，处理到输入结束(ctrl + z)
    while (scanf("%d %d", &a, &b) == 2) {
        results[2][counts[2]++] = lcm(a, b);
    }

    // 输出第一批数据结果
    for (int i = 0; i < counts[0]; ++i) {
        printf("%d\n", results[0][i]);
    }
    printf("group 1 done\n");

    // 输出第二批数据结果
    for (int i = 0; i < counts[1]; ++i) {
        printf("%d\n", results[1][i]);
    }
    printf("group 2 done\n");

    // 输出第三批数据结果
    for (int i = 0; i < counts[2]; ++i) {
        printf("%d\n", results[2][i]);
    }
    printf("group 3 done\n");

    return 0;
}