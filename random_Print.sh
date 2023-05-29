#!/bin/sh
# ３つのドット絵をランダムに生成するスプリクト
paint_terminal_dot() {
    TEXTDIR=~/development/ANSI_image #テキストファイルがあるパスを指定
    AA1="sed -e 's/^/\t/g' $TEXTDIR/kirby.txt" #　変数に格納

    AA2_1="sed -e 's/^/\t/g' $TEXTDIR/kirby.txt"

    AA2_2="sed -e 's/^/\t/g' $TEXTDIR/gura_red.txt"

    AA2_3="sed -e 's/^/\t/g' $TEXTDIR/siroko.txt"

    COUNT=10
    trap '' 1 2 3 4 5 15
    LINE=35
    TEXTDIR=~/development/ANSI_image #テキストファイルがあるパスを指定


        RAND=$(($RANDOM % 100))
    if [ $RAND -lt 33 ]; then
        eval $AA2_1 #　実行
    elif [ $RAND -lt 66 ]; then
        eval $AA2_2
    elif [ $RAND -lt 99 ]; then      
        eval $AA2_3
    fi


}

#関数を呼び出し
paint_terminal_dot