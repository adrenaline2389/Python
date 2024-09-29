#include <stdio.h>

int main()
{
    int arr[3]; // Array to store the 3 numbers
    // Input three numbers
    scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

    // Bubble sort algorithm for descending order
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2 - i; j++) {
            if (arr[j] < arr[j + 1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // Print the sorted array in descending order
    printf("%d %d %d", arr[0], arr[1], arr[2]);

    return 0;
}
