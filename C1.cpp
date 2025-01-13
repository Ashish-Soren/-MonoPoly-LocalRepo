#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
template <typename T>

T add(T num1, T num2){
    return(num1+num2);
}

int main(int argc, char const *argv[])
{
    double result;
    result = add<float>(6.82,3.5);
    cout << result;
    return 0;

    std::vector<int> vec1 = {1,2,3,4,5};
}
