#!/bin/sh

paint_terminal_dot() {
    AA1="sed -e 's/^/\t/g' ~/dot2ansi/kirby.txt" #テキストファイルがあるパスを指定
    eval $AA1 #　実行
}

#関数を呼び出し
paint_terminal_dot