function Z = tabe(x)
x1 = x(: , 1)
x2 = x(: , 2)
Z = -(3*x1^2 + 5*x2^2) 
xt=zeros(1,72);
if 3*x1 + 2*x2 >= 18
    Z = 10^5

 end