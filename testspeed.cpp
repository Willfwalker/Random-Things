#include <iostream>
#include <chrono>

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    for (int i = 1; i <= 100; i++) {
        // std::cout << i << std::endl; // Uncomment this line to print numbers
    }

    auto end_time = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time);

    std::cout << "Time taken: " << duration.count() << " seconds" << std::endl;

    return 0;
}