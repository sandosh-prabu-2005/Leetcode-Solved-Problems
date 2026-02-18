void decimalToBinaryString(unsigned int n, char *binaryStr) {
    for (int i = 31; i >= 0; i--) {
        binaryStr[i] = (n % 2) + '0';
        n /= 2;
    }
    binaryStr[32] = '\0';
}

void reverseString(char *str) {
    int i = 0, j = strlen(str) - 1;
    while (i < j) {
        char temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }
}

unsigned int binaryStringToDecimal(char *binaryStr) {
    unsigned int decimal = 0;
    for (int i = 0; i < 32; i++) {
        if (binaryStr[i] == '1') {
            decimal += (unsigned int)pow(2, 31 - i);
        }
    }
    return decimal;
}

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (int i = 0; i < 32; i++) {
        result <<= 1;
        if (n & 1) {
            result++;
        }
        n >>= 1;
    }
    
    return result;
}