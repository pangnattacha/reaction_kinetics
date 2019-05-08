function [k_optim,RMSE] = fun1(Temp)

    tableAC = readtable('data_dummy.xlsx');
    idx = tableAC.Temp == Temp;
    t = tableAC{idx,'time'};
    comp = {'A', 'B', 'C', 'D'};
    y = tableAC{idx,comp};
    x0 = y(1,:);
    
    %assume parameters as initial guess
    k0 = zeros(3,1); %k1~k3
    
    %find k_optim to fit kinetic model
    err = @(k) pred(k,t,x0)-y;
    lb = [0 0 0];
    ub = [];
    k_optim = lsqnonlin(err,k0,lb,ub);
    
    %compute RMSE
    RMSE = sum(sqrt((pred(k_optim,t,x0)-y).^2/length(t)));
    
    %plot
    t_plot = linspace(0,t(end));
    x_plot = pred(k_optim,t_plot,x0);
    legendName = {'A', 'B', 'C', 'D',...
        'predicted A', 'predicted B', 'predicted C','predicted D'};
    
    figure()
    plot(t,y(:,1),'ro',t,y(:,2),'bs',t,y(:,3),'m*',t,y(:,4),'g^',...
        t_plot,x_plot(:,1),'r-',t_plot,x_plot(:,2),'b-',t_plot,x_plot(:,3),'m-',...
        t_plot,x_plot(:,4),'g-','MarkerSize',14,'LineWidth',2)
    legend(legendName,'Location','bestoutside')
    xlabel('time (min)')
    ylabel('concentration [mol.L^{-1}]')
    set(gca,'FontSize',18);
    
    function xsol = pred(k,t,x0)
        [~,xsol] = ode45(@(t,x) ode(t,x,k),t,x0);
    end

end
