#!/bin/bash
# make exacutable: chmod +x run.sh
# run: ./run.sh A pypy A.py
# or
# ./run.sh A ./a.out
folder=$1;shift
for f in $folder/*.in; do
    echo $f
    pre=${f%.in}
    out=$pre.out
    ans=$pre.ans
    $* < $f > $out
    diff $out $ans
done
