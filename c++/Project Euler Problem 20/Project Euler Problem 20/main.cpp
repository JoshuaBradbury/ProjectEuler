#include <iostream>

using namespace std;

long long factorial(int n) {
	long long result = 1;
	for (int i = 0; i < n; i++) {
		result *= (i + 1);
	}
	return result;
}

int main() {
	cout << factorial(10) << endl;
	cout << factorial(20) << endl;
	cout << factorial(30) << endl;
	cout << factorial(40) << endl;

	cin.get();
	return 0;
}