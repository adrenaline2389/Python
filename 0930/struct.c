#include <stdio.h>

struct car
{
    char brand[20];
    int price;
    int speed;
};      //记得加 分号 !!!

int main()
{
    struct car my_car;

    scanf("%s", my_car.brand);
    scanf("%d", &my_car.price);
    scanf("%d", &my_car.speed);

    printf("%s\n", my_car.brand);
    printf("%d\n", my_car.price);
    printf("%d\n", my_car.speed);

    return 0;
}