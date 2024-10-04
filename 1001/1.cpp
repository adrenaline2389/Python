#include <iostream>
using namespace std;

int plus1(int a, int b)
{
	cout<<"1"<<endl;
	return a + b;
}

double plus1(double a, double b)
{
	cout<<"2"<<endl;
	return a + b;
}

double add(int a, int b)
{
	return a + b;
}

int main()
{
	int a = 3 , b = 4, res;
	double c = 1, d = 2;

	cout<<"1/c + 1/d = "<<add(1/a, 1/d)<<endl;
	cout<<"c + d = "<<plus1(c, d)<<endl;

	return 0;

}
