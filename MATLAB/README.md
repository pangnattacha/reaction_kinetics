# Reaction kinetics

## Introduction
This project is to create **MATLAB** code for fitting data with a chemical reaction model as shown below:

<img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/reactions.png" width="70%" height="70%">

## Problem setup
Optimizing kinetic rate constant (k) of each reaction that fit the experimental data [here](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/data_dummy.xlsx) with the prediction from this model.

## Create kinetic rate equations from the model
Assuming the first order reactions, ordinary differential equations (ODEs) are expressed as 

<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdA%7D%7Bdt%7D%20%3D%20-k_%7B1%7DA">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdB%7D%7Bdt%7D%20%3D%20k_1A-%28k_2&plus;k_3%29B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdC%7D%7Bdt%7D%20%3D%20k_2B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdD%7D%7Bdt%7D%20%3D%20k_3B">

The ODEs are stored as a function called [`ode`](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/ode.m).

## Find optimum k
To integrate ODEs and predict yields of each product in the reaction chains, a local function called `pred` using MATLAB function called [`ode45`](https://uk.mathworks.com/help/matlab/ref/ode45.html?requestedDomain=) was created. Then k values were optimized by data fitting that minimize the least square error using MATLAB function called [`lsqnonlin`](https://uk.mathworks.com/help/optim/ug/lsqnonlin.html). These codes are stored inside the function [`fun1`](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/fun1.m). This function returns `k_optim` and `RMSE`(root mean squared error).

## Report the result
A script [`result`](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/result.m) was written for loading the datafile, calling the functions to optimize k values to fit the reaction model and plotting the results. The plots comparing between model prediction and raw data for three different temperatures are shown in the following.

<img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/result100.jpg" width="30%" height="30%"><img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/result200.jpg" width="30%" height="30%"><img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/.jpg" width="30%" height="30%">

In addition, activation energy(Ea) and pre-exponential factor(A) can be calculated from the Ahrrenius equation:

<img src="https://latex.codecogs.com/gif.latex?k%3DAe%5E%7B%5Cfrac%7B-E_a%7D%7BRT%7D%7D">

where R is a gas constant and T is an absolute temperature. By running [`result`](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/result.m), Ea and A were also obtained.
