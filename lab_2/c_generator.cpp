#include <iostream>
#include <ctime>

const int SIZE = 128;

/**
 * This function initializes the random number generator using the current time and generates
 * a 128-bit binary sequence, printing it to the standard output.
 * 
 * @return None
 */
void binary_generate() {

    std::srand(static_cast<unsigned>(std::time(0)));

    for (int i = 0; i < SIZE; ++i) {
        int random_bit = std::rand() % 2;
        std::cout << random_bit;
    }
}

/**
 * The main function calls binary_generate to generate a random binary sequence
 * and print it to the standard output.
 *
 * @return The program exit code.
 */
int main() {
    binary_generate();
    return 0;
}