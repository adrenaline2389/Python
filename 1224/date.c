#include <stdio.h>

struct DATE
{
    int day;
    int month;
    int year;
};

int days(struct DATE date)
{
    int ans = date.month * 30 - 30 + date.day;
    if (date.month == 2) ans++;
    if (date.month == 3) ans--;
    if (date.month == 6) ans++;
    if (date.month == 7) ans++;
    if (date.month == 8) ans += 2;
    if (date.month == 9) ans += 3;
    if (date.month == 10) ans += 3;
    if (date.month == 11) ans += 4;
    if (date.month == 12) ans += 4;
    if (date.month > 2 && date.year % 4 == 0) ans++;
    return ans;
}

int main()
{
    struct DATE d;
    scanf("%d-%d-%d", &d.year, &d.month, &d.day);
    printf("%d", days(d));
}