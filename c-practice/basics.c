#include <stdio.h>

// Returns the larger of two integers
int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

// Returns 1 if n is even, 0 if odd
int is_even(int n) {
    return n % 2 == 0;
}

// Returns the sum of all integers from 1 to n
int sum_to_n(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

int main() {
    printf("max(4, 9) = %d\n", max(4, 9));
    printf("is_even(7) = %d\n", is_even(7));
    printf("is_even(8) = %d\n", is_even(8));
    printf("sum_to_n(5) = %d\n", sum_to_n(5));
    return 0;
}
