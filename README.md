# Reaction kinetics

## Introduction
This project is to create **MATLAB** code for fitting data with a chemical reaction model as shown below:

<img src="https://github.com/pangnattacha/reaction_kinetics/blob/master/reactions.png" width="70%" height="70%">

Assuming the first order reactions, ordinary derivative equations (ODEs) are expressed as 

<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7BdA%7D%7Bdt%7D%20%3D%20-k_%7B1%7DA">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20B%7D%7B%5Cmathrm%7Bd%7D%20t%7D%20%3D%20k_1A%20-%20%28k_2&plus;k_3%29B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20C%7D%7B%5Cmathrm%7Bd%7D%20t%7D%20%3D%20k_2B">
<img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%20%3D%20k_3B">
