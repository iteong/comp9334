% COMP9334 
% Assignment
% After working out the balance equation, we need to solve
% the set of linear equations
% 
% I have chosen to use the first 9 equations together
% with sum( probabilities ) = 1 
% 
% In principle, you can choose any of the 10 equations together
% with sum( probabilities ) = 1 
%
% We put the linear equations in standard form A x = b
% where x is the unknown vector  
% 
A = [ 20  0   0   0   0   0   0   0   0   0
      0  10   0   0   0   0   0   0   0   0
     -20  0  40 -10   0   0   0   0 -20   0
      0   0 -20  30   0 -20   0   0   0   0
      0 -10   0   0  30   0 -20   0   0   0
      0   0   0 -20   0  50 -10 -20 -10   0
      0   0   0   0 -20   0  30   0   0   0
      0   0   0   0 -10 -20   0  30   0   0
      0   0 -20   0   0 -10   0   0  50 -20
      1   1   1   1   1   1   1   1   1   1];
b = [0 0 0 0 0 0 0 0 0 1]';
x = A\b