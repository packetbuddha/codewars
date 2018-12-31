#include <stdio.h>

int multiply(int a, char *b)
{
    return a * (int) b;
}

int main ()
{
    int a = 2;
    char *b_p = "4"; 

    printf("%d", multiply(a, b_p));

    return 1;
}
