#!/bin/bash

ALGORITHMS_PATH='code/algorithms'

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a)
    ALGO="$2"
    shift
    ;;
    -e)
    EX_PATH="$2"
    shift
    ;;
    -p|-t)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

#./points -e $EX_PATH -a $ALGO $OPTIONS

python3 ./${ALGORITHMS_PATH}/tp1.py -e $EX_PATH -a $ALGO $OPTIONS
