#include <stdio.h>

int main() {
    int inputNumber, outputNumber;
    int lastTwoDigits, digitsInfront;

    scanf("%d", &inputNumber);

    lastTwoDigits = inputNumber % 100;
    digitsInfront = inputNumber / 100;

    if (inputNumber < 149) {
        outputNumber = 99;
    } else {
        if (lastTwoDigits < 49) {
            outputNumber = (digitsInfront - 1) * 100 + 99;
        } else {
            outputNumber = digitsInfront * 100 + 99;
        }
    }

    printf("%d", outputNumber);

    return 0;
}
