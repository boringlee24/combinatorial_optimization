set WEIGHTS;

param cost {WEIGHTS} > 0;
param f_min := 0;
param f_max := 1;
param cap;

var SELECT {j in WEIGHTS} >= f_min, <= f_max;

maximize objective:  sum {j in WEIGHTS} cost[j] * SELECT[j];

subject to constraint:
   sum {j in WEIGHTS} cost[j] * SELECT[j] <= cap;
