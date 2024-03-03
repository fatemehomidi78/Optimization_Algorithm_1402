clc;
clear;
close all;

%% Problem Definition
tic;
problem.CostFunction = @(x)tabe(x);
problem.nVar = 2;
problem.VarMin = [0,0];
problem.VarMax = [4,6];


%% GA Parameters
params.MaxIt = 100;
params.nPop = 10;

params.beta = 1;
params.pC = 1;
params.gamma = 0.1;
params.mu = 0.01;
params.sigma = 0.1;

%% Run GA

out = RunGA(problem, params);

%% Results
toc;
figure;
plot(out.bestcost, 'lineWidth', 2);
% semilogy(out.bestcost, 'lineWidth', 2);
xlabel('Iterations');
ylabel('Best Cost');
grid on;
