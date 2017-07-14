#include <iostream>
using namespace std;

int main() {
	long long result = 1;
	for (int i = 0; i < 50; i++) {
		result *= 2;
	}
	cout << result << endl;
	cin.get();
	return 0;
}