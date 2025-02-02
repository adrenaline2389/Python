#include <stdio.h>
#include <string.h>

int main() {
    char a[3][81], sum = 0;
    for (int i = 0; i < 3; i++) {
        gets(a[i]);
        for (int j = 0; j < strlen(a[i]); j++) {
            if (a[i][j] >= 'A' && a[i][j] <= 'Z') sum++;
        }
    }
    printf("%d", sum);

    return 0;
}