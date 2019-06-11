function dxdt = ode(t,x,k)

    dxdt = zeros(4,1);
    dxdt(1) = -k(1)*x(1); %A
    dxdt(2) = k(1)*x(1)-(k(2)+k(3))*x(2); %B
    dxdt(3) = k(2)*x(2); %C
    dxdt(4) = k(3)*x(2); %D

  
end