#include <stdio.h>
int main() {
    int n, v1, v2, ac = 1;
    scanf("%d %d", &n, &v1);
    while (--n) {
        scanf("%d", &v2);
        if (v2 - v1) {
            ac++;
            v1 = v2;
        }
    }
    printf("%d\n", ac);
    return 0;
}
