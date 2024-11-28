// #include <stdio.h>
// #include <string.h>

// #define MAX_LEN 81  // 80位数+1位结尾符

// void bigNumberAdd(char num1[], char num2[], char result[]) {
//     int len1 = strlen(num1);
//     int len2 = strlen(num2);
//     int carry = 0;  // 进位
//     int index = 0;

//     // 从个位开始逐位相加
//     for (int i = 0; i < len1 || i < len2 || carry; i++) {
//         int digit1 = (i < len1) ? num1[len1 - 1 - i] - '0' : 0;
//         int digit2 = (i < len2) ? num2[len2 - 1 - i] - '0' : 0;
//         int sum = digit1 + digit2 + carry;
//         result[index++] = (sum % 10) + '0';  // 当前位的值
//         carry = sum / 10;  // 更新进位
//     }
//     result[index] = '\0';

//     // 反转结果字符串
//     for (int i = 0; i < index / 2; i++) {
//         char temp = result[i];
//         result[i] = result[index - 1 - i];
//         result[index - 1 - i] = temp;
//     }
// }

// int main() {
//     char num1[MAX_LEN], num2[MAX_LEN], result[MAX_LEN + 1];

//     // 输入两个大整数
//     scanf("%s", num1);
//     scanf("%s", num2);

//     // 计算大数相加
//     bigNumberAdd(num1, num2, result);

//     // 输出结果
//     printf("%s", result);

//     return 0;
// }






// #include <stdio.h>
// #include <string.h>
// #define MAXLEN 81
// void BigNumAdd(char num1[], char num2[], char result[]) {
//     int len1 = strlen(num1);
//     int len2 = strlen(num2);
//     int carry = 0;
//     int index = 0;

//     for (int i = 0; i < len1 || i < len2 || carry; i++) {
//         int digit1 = (i < len1) ? num1[len1 - 1 - i] - '0' : 0;
//         int digit2 = (i < len2) ? num2[len2 - 1 - i] - '0' : 0;
//         int sum = digit1 + digit2 + carry;
//         result[index++] = (sum % 10) + '0';
//         carry = sum / 10;
//     }
//     result[index] = '\0';

//     for (int i = 0; i < index / 2; i++) {
//         char temp = result[i];
//         result[i] = result[index - 1 - i];
//         result[index - 1 - i] = temp;
//     }
// }

// int main() {
//     char num1[MAXLEN], num2[MAXLEN], result[MAXLEN + 1];
//     scanf("%s", &num1);
//     scanf("%s", &num2);

//     BigNumAdd(num1, num2, result);

//     printf("%s", result);

//     return 0;
// }














#include <stdio.h>
#include <string.h>

#define MAX_LEN 81

void BigNumAdd(char num1[], char num2[], char result[]) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    int carry = 0;
    int index = 0;

    for (int i = 0;i < len1 || i < len2 || carry; i++) {
        int digit1 = (i < len1) ? num1[len1 - 1 - i] - '0' : 0;
        int digit2 = (i < len2) ? num2[len2 - 1 -i] - '0' : 0;
        int sum = digit1 + digit2 + carry;
        result[index++] = (sum % 10) + '0';
        carry = sum / 10;
    }
    result[index] = '\0';

    for (int i = 0; i < index / 2; i++) {
        char temp = result[i];
        result[i] = result[index - 1 - i];
        result[index - 1 - i] = temp;
    }
}

int main() {
    char num1[MAX_LEN], num2[MAX_LEN], result[MAX_LEN + 1];

    scanf("%s", &num1);
    scanf("%s", &num2);

    BigNumAdd(num1, num2, result);

    printf("%s", result);

    return 0;
}