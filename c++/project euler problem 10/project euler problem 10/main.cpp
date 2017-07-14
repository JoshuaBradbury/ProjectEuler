#include <iostream>

using namespace std;

bool isPrime(int n) {
	if (n <= 1)
		return false;
	else if (n == 2)
		return true;
	else if (n % 2 == 0)
		return false;
	else
	{
		bool prime = true;
		int divisor = 3;
		double num_d = static_cast<double>(n);
		int upperLimit = static_cast<int>(sqrt(num_d) + 1);

		while (divisor <= upperLimit)
		{
			if (n % divisor == 0)
				prime = false;
			divisor += 2;
		}
		return prime;
	}
}

int main() {
	long long result = 0;

	for (int j = 1; j < 10000000; j++) {
		if (j % 10000 == 0) {
			cout << j << endl;
		}
		if (isPrime(j)) {
			result += j;
		}
	}

	cout << "The total is: " << result << "!" << endl;

	cin.get();
	return 0;
}