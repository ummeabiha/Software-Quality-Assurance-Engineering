#include <iostream>
using namespace std;

int main() {
    int i = 1, total_input = 0, total_valid = 1, sum = 0, minimum = 0, maximum = 0;

    do {
        total_input = total_input + 1;
        if (i >= minimum && i <= maximum) {
            total_valid = total_valid + 1;
            sum = sum + i;}
        i++;
    } while (i != -999 && total_input < 100);

    float average;
    if (total_valid > 0) {average = static_cast<float>(sum) / total_valid;} 
    else {average = -999;}

    cout << "Average: " << average << endl;
    cout << "i: " << i << endl;
    cout << "Sum: " << sum << endl;
    cout << "Total input: " << total_input << endl;
    cout << "Total valid: " << total_valid << endl;
    cout << "Minimum: " << minimum << endl;
    cout << "Maximum: " << maximum << endl;
    return 0;}
