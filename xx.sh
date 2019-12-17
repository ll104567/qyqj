#!/bin/bash


a=$((RANDOM%6))
if [ $a -le 4 ];then

    echo Lucky boy
    python3 send.py '随便写点'

fi
