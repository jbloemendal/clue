#!/bin/bash
#for f in examples/set1/*; do m=`cat $f | ./clue`; echo "$m $f"; done | sort 
#for f in examples/set2/*; do m=`cat $f | ./clue`; echo "$m $f"; done | sort 
#for f in examples/set3/*; do c=`cat $f`; m=`cat $f | ./clue`; echo "$m $f $c"; done | sort 
#for f in examples/*; do m=`cat $f | ./clue`; echo "$m $f"; done | sort | sed "s/^[0-9\s\.]* //"
while read line; do c=`echo $line`; k=`echo $c | ./clue`; echo "$k, $c"; done < examples/set5/set5.c 
