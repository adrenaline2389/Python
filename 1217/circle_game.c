#include <stdio.h>
 
int lastRemaining(int n) 
{
    int i, last = 0; // 最后剩下的人的初始编号为0
 
    // 对于每一轮，i 从 2 开始，每次循环只剩下一个人时结束
    for (i = 2; i <= n; i++)
        last = (last + 3) % i; // 根据规则计算下一个要被删除的人的编号
 
    return last + 1; // 返回最后剩下的人的编号
}
 
int main() 
{
    int n;
    scanf("%d", &n);
    printf("%d\n", lastRemaining(n));
    return 0;
}