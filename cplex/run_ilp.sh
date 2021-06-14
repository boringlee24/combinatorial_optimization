#!/bin/bash

for i in {0..99}
do 
  ampl ilp${i}.file > ilp_log/ilp${i}.txt &
done
 
