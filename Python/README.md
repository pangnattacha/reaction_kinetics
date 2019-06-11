# Reaction kinetics

## Introduction
This project is to create **Python** code for fitting data with a chemical reaction model as shown below:

<img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/reactions.png" width="70%" height="70%">

## Problem setup
Optimizing kinetic rate constant (k) of each reaction that fit the experimental data [here](https://github.com/pangnattacha/reaction_kinetics/blob/master/MATLAB/data_dummy.xlsx) with the prediction from this model.

## Create kinetic rate equations from the model
Assuming the first order reactions, ordinary differential equations (ODEs) are expressed as 

<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdA%7D%7Bdt%7D%20%3D%20-k_%7B1%7DA">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdB%7D%7Bdt%7D%20%3D%20k_1A-%28k_2&plus;k_3%29B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdC%7D%7Bdt%7D%20%3D%20k_2B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdD%7D%7Bdt%7D%20%3D%20k_3B">

## Create class `Optimize_k`
Class [`Optimize_k`](https://github.com/pangnattacha/reaction_kinetics/blob/master/Python/kinetics_python.py) includes some methods to optimize k values that give the best fit to the experimental data. The methods are:
- `ode(x,t,k)` to initialize ode equations following the reaction model
- `model(t,k)` to integrate ode equations with time (t) and input k values
- `errfun(k)` to compute the error when using k in `model`
- `optim(k_guess)` return optimal k values from the initial guess `k_guess`.

## Report the result
The script [`result`](https://github.com/pangnattacha/reaction_kinetics/blob/master/Python/result.py) was written for loading the datafile
It called methods from `Optimize_k` to find optimum k at each temperature.
The plots comparing between model prediction and raw data are shown in the following.

<img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/Python/model_result.png">
