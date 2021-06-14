#!/bin/bash

for i in {0..99}
do 
  ampl lp${i}.file > lp_log/lp${i}.txt &
done
 
