function  cout=curv(c1,c2,x1,x2,x3,de)

cout=(c1+c2/(1.+((de-x2)/x3)^2))*((de/x1)^2)/(1.+((de/x1)^2));