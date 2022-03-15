#include<iostream>
#include<string>
using namespace std;
int main(){

    string str = "he is@ a@ good boy";
    cout << str << endl;
    str = str.replace(str.find("a"),2,"#");  //从第一个a位置开始的两个字符替换成#
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(str.begin(),str.begin() + 5,"#"); //用#替换从begin位置开始的5个字符
    cout << str << endl;

    str = "he is@ a@ good boy";
    string sub = "12345";
    str=str.replace(0,5,sub,sub.find("1"),4); //用substr的指定字符串替换str指定字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(0,5, sub);   //用str替换从指定位置开始长度为5的字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(str.begin(),str.begin()+6, sub);   //用str替换从指定迭代器位置的字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(0,6,&sub[0],4);   //用str1的前4个字符串替换从位置0~6的字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(str.begin(),str.begin()+6,&sub[0],4);   //用str1的前4个字符串替换从位置0~6的字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    char str1 = '#';
    str = str.replace(0,6,3, str1);   //用重复3次的str1字符替换的替换从位置0~6的字符串
    cout << str << endl;

    str = "he is@ a@ good boy";
    str = str.replace(str.begin(),str.begin()+6,3, str1);   //用重复3次的str1字符替换的替换从指定迭代器位置的内容
    cout << str << endl;

    return 0;
}