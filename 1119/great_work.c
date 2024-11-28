#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = -n + 1; i < n; ++i) {
        int spaces = (i < 0) ? -i : i;
        int index = n - abs(i);

        for (int j = 0; j < spaces; ++j) {
            printf(" ");
        }
        for (int j = 1; j < 2 * index; ++j) {
            int num = (j <= index) ? j : 2 * index - j;
            printf("%d", num);
        }
        printf("\n");
    }
    return 0;
}