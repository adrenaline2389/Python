#include <stdio.h>
#include <math.h>
int main() {
    float a1, a2;
    scanf ("%f %f", &a1, &a2);
    float q = a2 / a1;
    float a0 = a1 / q, a3 = a2 * q, a4 = sqrt(a1 * a2);
    int a0_ = a0, a3_ = a3, a4_ = a4;
    int exam = 0;
    if (a0 - a0_ == 0.) {
        exam++;
        printf("%d %.0f %.0f\n", a0_, a1, a2);
    }
    if (a4 - a4_ == 0. && a4 != a0) {
        exam++;
        printf("%.0f %d %.0f\n", a1, a4_, a2);
    }
    if (a3 - a3_ == 0. && a3 != a0) {
        exam++;
        printf("%.0f %.0f %d", a1, a2, a3_);
    }
    
    if (exam == 0) printf("error");

    return 0;
}