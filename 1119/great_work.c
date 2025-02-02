// #include <stdio.h>
// #include <stdlib.h>
// int main() {
//     int n;
//     scanf("%d", &n);
    
//     for (int i = -n + 1; i < n; ++i) {
//         int spaces = (i < 0) ? -i : i;
//         int index = n - abs(i);

//         for (int j = 0; j < spaces; ++j) {
//             printf(" ");
//         }
//         for (int j = 1; j < 2 * index; ++j) {
//             int num = (j <= index) ? j : 2 * index - j;
//             printf("%d", num);
//         }
//         printf("\n");
//     }
//     return 0;
// }









// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     int n;
//     scanf("%d", &n);

//     for (int i = 1 - n; i < n; i++) {
//         int spaces = (i < 0) ? -i : i;
//         for (int j = 0; j < spaces; j++) printf(" ");

//         int index = n - abs(i);
//         for (int j = 1; j < 2 * index; j++) {
//             int num = (j <= index) ? j : 2 * index - j;
//             printf("%d", num);
//         }
//         printf("\n");
//     }
//     return 0;
// }










#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1 - n; i < n; i++) {
        int spaces = (i < 0) ? -i : i;
        for (int j = 0; j < spaces; j++) printf(" ");

        int index = n - abs(i);
        for (int j = 1; j < 2 * index; j++) {
            int num = (j <= index) ? j : 2 * index - j;
            printf("%d", num);
        }
        printf("\n");
    }
    return 0;
}










#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 10;
    int size = 2*n+1;
    for (int y=0;y<size;y++) {
        for (int x=0;x<size;x++) {
            int d = abs(n-x) + abs(n-y);
            // distance to center
            if (n-d >0)
                printf("%d", n-d);
            else
                printf(" ");
        }
        printf("\n");
    }
}