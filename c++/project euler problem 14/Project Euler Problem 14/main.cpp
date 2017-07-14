#include <iostream>

using namespace std;

int collatzLength(long long n) {
	int lengthSeq = 0;
	while (n > 1) {
		if (n % 2 == 0)  {
			n /= 2;
		} else {
			n = 3 * n + 1;
		}
		lengthSeq++;
	}
	return lengthSeq;
}

int main() {

	int longestTerm = 0;
	int longestLength = 0;

	for (int i = 0; i < 1000000; i++) {
		int temp = collatzLength(i);
		if (temp > longestLength) {
			longestLength = temp;
			longestTerm = i;
		}
	}

	cout << "The longest term is " << longestTerm << " With a length of " << longestLength << endl;

	cin.get();

	return 0;
}