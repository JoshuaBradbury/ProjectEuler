#include <iostream>
#include <math.h>

using namespace std;

int numOfFactors(int n) {
	int numOfFactors = 0;
	for (int i = 1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			numOfFactors += 1;
		}
	}
	return numOfFactors * 2;
}

int main() {
	
	long long i = 1;
	long long triangleNo = 0;
	int numFacts = 0;
	while (numFacts <= 500) {
		triangleNo += i;
		i++;
		if (i % 100 == 0) {
			cout << i << " " << numFacts << endl;
		}
		int n = numOfFactors(triangleNo);
		if (n > numFacts) {
			numFacts = n;
		}
	}

	cout << "The Final Answer is " << triangleNo << " With " << numFacts << " Factors" << endl;

	cin.get();

	return 0;
}