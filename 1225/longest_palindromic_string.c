#include <stdio.h>
#include <string.h>

// 函数定义

// 辅助函数，用于中心扩展
void findLongestPalindromeHelper(char *s, int left, int right, int *start, int *maxLen) {
    while (left >= 0 && right < strlen(s) && s[left] == s[right]) {
        left--;
        right++;
    }
    // 检查当前回文子串长度是否大于已知的最大长度
    int len = right - left - 1;
    if (len > *maxLen) {
        *maxLen = len;
        *start = left + 1;
    }
}

void findLongestPalindrome(char *s, int len, int *start, int *maxLen) {
    for (int i = 0; i < len; i++) {
        // 以s[i]为中心的回文串
        findLongestPalindromeHelper(s, i, i, start, maxLen);
        // 以s[i]和s[i+1]为中心的回文串
        findLongestPalindromeHelper(s, i, i + 1, start, maxLen);
    }
}


int main() {
    char s[81]; // 假设字符串不超过80个字符
    scanf("%s", s); // 读取输入的字符串

    int len = strlen(s); // 获取字符串长度
    int start = 0; // 回文子串的起始位置
    int maxLen = 1; // 最长回文子串的长度

    // 寻找最长回文子串
    findLongestPalindrome(s, len, &start, &maxLen);

    // 输出最长回文子串
    for (int i = 0; i < maxLen; i++) {
        printf("%c", s[start + i]);
    }
    printf("\n");

    return 0;
}