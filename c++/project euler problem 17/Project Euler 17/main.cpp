#include <iostream>

using namespace std;

string getDigit(int n) {
	string digits[10] = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
	return digits[n % 10];
}

string getNumberString(int n) {
	string number = "";
	if (n == 1000) {
		number = "onethousand";
	} else {
		if (n > 99) {
			int hundreds = n - (n % 100);
			number += getDigit(hundreds / 100) + "hundred";
			if (n % 100 != 0) {
				number += "and";
			}
		}
		if (n > 9) {
			int other = n % 1000;
			int other2 = n % 100;
			other -= other2;
			int tens = n - other;
			tens -= (tens % 10);
			if (tens == 10) {
				string teens[10] = { "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };
				number += teens[n % 10];
			}
			else if (tens == 20) {
				number += "twenty";
			}
			else if (tens == 30) {
				number += "thirty";
			}
			else if (tens == 40) {
				number += "forty";
			}
			else if (tens == 50) {
				number += "fifty";
			}
			else if (tens == 80) {
				number += "eighty";
			}
			else {
				number += getDigit(tens / 10);
				if (getDigit(tens / 10) != "") {
					number += "ty";
				}
			}
		}
		if (n % 100 < 10 || n % 100 > 20) {
			number += getDigit(n % 10);
		}
	}
	return number;
}

int main() {

	int size = 0;

	for (int i = 0; i < 1000; i++) {
		size += getNumberString(i + 1).length();
		cout << getNumberString(i + 1).c_str() << endl;
	}

	cout << size << endl;

	cin.get();

	return 0;
}