#include <iostream>
#include <vector>

using namespace std;

vector<string> permutations(string str) {
	vector<string> perms;
	for (unsigned int i = 0; i < str.length(); i++)  {
		string part1 = str.substr(0, i);
		string part2 = str.substr(i + 1, str.length() - 1);
		for (string perm : permutations(part1 + part2)) {
			if (std::find(perms.begin(), perms.end(), str.substr(i, i + 1) + perm) != perms.end()) {
				perms.push_back(str.substr(i, i + 1) + perm);
			}
		}
	}
	if (str.length() == 1) {
		perms.push_back(str);
	}
	return perms;
}

int main() {
	for (string str : permutations("123")) {
		cout << 1 << endl;
		cout << str.c_str() << endl;
	}

	cout << "Done :D" << endl;

	cin.get();

	return 0;
}