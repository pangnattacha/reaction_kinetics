clear
% calculate k_optim
    [k_optim,RMSE] = fun1(100);    
    n = length(k_optim);
    k = zeros(3,n);
    RMSE_all = zeros(3,4);
    k(1,:) = k_optim';
    RMSE_all(1,:) = RMSE;
    for i = 2:3
        [k_optim,RMSE] = (fun1(100*i));
        k(i,:) = k_optim';
        RMSE_all(i,:) = RMSE;
    end

%Compute Ea, A from Arrhenius eq.
    lnk = log(k);
    temp = [100;200;300];
    T_inv = 1./(temp+273.15);
    
    %preallocation
    lnk_fit = zeros(3,n);
    p = zeros(n,2);
    
    for i= 1:n
        idx1 = k(:,i)>(10e-10); % remove too low k
        p(i,:) = polyfit(T_inv(idx1),lnk(idx1,i),1);
        lnk_fit(:,i) = polyval(p(i,:),T_inv);
        lnk_res(idx1,i) = lnk(idx1,i) - lnk_fit(idx1,i);
            
    end
    
    %calculat r^2
    R2_AC = zeros(1,n);
    R2_MC = zeros(1,n);
    for i= 1:n
        SS_resAC = sum(lnk_res(:,i).^2);
        SS_totalAC = (length(lnk)-1) * var(lnk(:,i));
        R2_AC(i) = 1-SS_resAC/SS_totalAC;
    end
    
    Ea =  -p(:,1).*8.314 %calc from slope
    A = exp(p(:,2)) %calc from intercept
