#include <stdio.h>

int main() {
    int n1 = 0, n2 = 1, next;  // 初始化前两个数
    int count = 20;  // 打印前20个数

    printf("斐波那契数列的前20个数: \n");
    printf("%d, %d", n1, n2);  // 打印前两个数

    for (int i = 2; i < count; i++) {
        next = n1 + n2;  // 计算下一个数
        printf(", %d", next);  // 打印当前数
        n1 = n2;  // 更新n1为下一个位置的值
        n2 = next;  // 更新n2为下一个位置的值
    }

    printf("\n");  // 换行
    return 0;
}
