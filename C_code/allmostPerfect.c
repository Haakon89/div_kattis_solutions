#include <stdio.h>

int main() {
    /*FILE *file;
    int numbers[500];*/
    int count = 3;
    int sumOfDivisors;
    
    /*file = fopen("sample.in", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (fscanf(file, "%d", &numbers[count]) == 1) {
        count++;
    }

    fclose(file);*/
    int numbers[3]
    numbers[0] = 6;
    numbers[1] = 65;
    numbers[2] = 650;
    for (int i = 0; i < count; i++) {
        sumOfDivisors = 0;
        for (int j = 1; j < numbers[i]; j++) {
            if (j % numbers[i] == 0) {
                sumOfDivisors += j;
            }
        }
        if (sumOfDivisors == numbers[i]) {
            printf("%d perfect\n", numbers[i]);
        } else if (abs(sumOfDivisors - numbers[i]) <= 2) {
            printf("%d almost perfect\n", numbers[i]);
        } else {
            printf("%d not perfect\n", numbers[i]);
        }
        
    }

    return 0;
}
