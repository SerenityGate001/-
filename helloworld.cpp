#include <iostream>
using namespace std;
int main() {
    int a, summ, mult;
    summ = 0; mult = 1;
    cin >> a;
    int sot = a / 100;
    int des = (a / 10) % 10;
    int ed = a % 10;
    if (sot % 2 == 0){
        summ = summ + sot;
        mult = mult * sot;
    }
    if (des % 2==0){
        summ = summ + des;
        mult = mult * des;
    }
    if (ed % 2 == 0){
        summ = summ + ed;
        mult = mult * ed;
    }
    cout << "Сумма: " <<summ << endl;
    cout << "Произведение: " << mult;
    return 0;
}