#!/bin/bash
for f in examples/*; do m=`cat $f | ./ksi`; echo "$m $f"; done | sort 
#for f in examples/*; do m=`cat $f | ./ksi`; echo "$m $f"; done | sort | sed "s/^[0-9\s\.]* //"
