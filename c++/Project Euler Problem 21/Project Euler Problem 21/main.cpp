#include <iostream>
#include <vector>

using namespace std;

vector<int> factorsOfN(int n) {
	vector<int> factors;
	for (int i = 1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			factors.push_back(i);
		}
	}
	return factors;
}

int main() {
	string factorsString;
	vector<int> factors = factorsOfN(220);
	for (int i : factors) {
		factorsString += i + ", ";
	}
	cout << factorsString.c_str() << endl;
	cin.get();
	return 0;
}