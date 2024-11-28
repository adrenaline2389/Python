#include <stdio.h>
int main() {
    int array[3][4];
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 4; ++j) {
            scanf("%d", &array[i][j]);
        }
    }

    int saddlepoint = 0;

    for (int i = 0; i < 3; ++i) {
        int target = array[i][0];
        int index = 0;
        for (int j = 1; j < 4; ++j) {
            if (array[i][j] > target) {
                target = array[i][j];
                index = j;
            }
        }
        int examine = target;
        for (int j = 0; j < 3; ++j) {
            examine = (array[j][index] < examine) ? array[j][index] : examine;
        }

        if (examine == target) {
            printf("%d", target);
            saddlepoint = 1;
            break;
        }
    }

    if (!saddlepoint) printf("NO");
    
    return 0;
}