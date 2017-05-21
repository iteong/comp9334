% Week 7, Q1, Part (a): Transient removal   

% load the traces 
load trace1 
load trace2 
load trace3 
load trace4 
load trace5 

% put the traces in an array
nsim = 5;     % number of simulation
m = 100;  % number of data points in each simulation
T = zeros(nsim,m);
for i = 1:5
    eval(['T(i,:) = trace',num2str(i),';']);
end    

% Compute the mean over the 5 replications
mt = mean(T);

% smooth it out with different values of w
% vary the value of w here 
w = 2;
mt_smooth = zeros(1,m-w);

    for i = 1:(m-w)
        if (i <= w)
            mt_smooth(i) = mean(mt(1:(2*i-1)));
        else
            mt_smooth(i) = mean(mt((i-w):(i+w)));
        end
    end

% plot the smoothed batch mean
xv = 1:(m-w);
plot(mt_smooth','Linewidth',3);
title(['w = ',int2str(w)],'FontSize',16)









