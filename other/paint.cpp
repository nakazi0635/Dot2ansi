#include <iostream>
#include <string>
using namespace std;

// カービィ制作
// ピンク
void b_pink(){
    printf("\033[48;5;%sm  \033[0m",std::to_string(225).c_str());
}
// //暗めのピンク
// def pink
//     print "\033[48;5;", 218.to_s, "m","  \033[0m"
// end

// //目とか
// def black
//     print "\033[48;5;", 239.to_s, "m","  \033[0m"
// end

// //ほっぺのピンクと足
// def orange
//     print "\033[48;5;", 210.to_s, "m","  \033[0m"
// end

// //暗めの赤色166,167
// def foot
//     print "\033[48;5;", 166.to_s, "m","  \033[0m"
// end



// //空白
// def space
//     print "  "
// end
// //改行
// def new_line
//     print "\n"
// end

int main(int argc, const char * argv[]) {
    // new_line;
    // space;space;space;space;space;  space;pink;pink;space;space;pink;pink;pink;pink;pink;space;space;pink;pink;
    // new_line;
    // space;space;space;space;space;  pink;b_pink;b_pink;pink;pink;b_pink;b_pink;b_pink;b_pink;b_pink;pink;pink;b_pink;b_pink;pink;
    // new_line;
    // space;space;space;space;pink;  b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;pink;
    // new_line;
    // space;space;space;space;pink;  b_pink;b_pink;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;pink;b_pink;pink;
    // new_line;
    // space;space;space;space;pink;  b_pink;pink;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;pink;pink;pink;
    // new_line;
    // space;space;space;space;pink;  pink;pink;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;b_pink;pink;pink;
    // new_line;
    // space;space;space;space;pink;  pink;b_pink;b_pink;orange;orange;b_pink;b_pink;b_pink;b_pink;b_pink;orange;orange;b_pink;b_pink;b_pink;pink;
    // new_line;
    // space;space;space;space;space;  pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;pink;
    // new_line;
    // space;space;space;space;space;  pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;black;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;pink;
    // new_line;
    // space;space;space;space;space;  foot;foot;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;foot;foot;
    // new_line;
    // space;space;space;space;foot;  orange;orange;foot;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;foot;orange;orange;foot;
    // new_line;
    // space;space;space;space;foot;  orange;orange;orange;orange;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;orange;orange;orange;orange;foot;
    // new_line;
    // space;space;space;space;foot;  orange;orange;orange;orange;b_pink;b_pink;b_pink;b_pink;b_pink;b_pink;orange;orange;orange;orange;orange;foot;
    // new_line;
    // space;space;space;space;foot;  foot;orange;orange;orange;foot;b_pink;b_pink;b_pink;b_pink;b_pink;foot;orange;orange;orange;orange;foot;
    // new_line;
    // space;space;space;space;space;  foot;orange;orange;orange;foot;pink;pink;pink;pink;pink;foot;orange;orange;orange;foot;
    // new_line;
    // space;space;space;space;space;  space;foot;foot;foot;space;space;space;space;space;space;space;foot;foot;foot;
    // new_line;
    b_pink();b_pink();b_pink();b_pink();b_pink();

    printf("c++でも動く\n");
    return 0;
}