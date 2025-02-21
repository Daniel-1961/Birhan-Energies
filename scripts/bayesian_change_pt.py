# bayesian_change_point_detection.py

import pymc3 as pm
import matplotlib.pyplot as plt

def setup_model(data):
    """Set up the Bayesian model for change point detection."""
    mean_price = data['Price'].mean()
    
    with pm.Model() as model:
        # Priors
        mean_prior = pm.Normal('mean_prior', mu=mean_price, sigma=10)
        change_point = pm.DiscreteUniform('change_point', lower=0, upper=len(data)-1)

        # Likelihood
        likelihood = pm.Normal('likelihood', mu=mean_prior, sigma=10, observed=data['Price'])
        
    return model

def perform_inference(model):
    """Perform Bayesian inference using MCMC sampling."""
    with model:
        trace = pm.sample(1000, tune=1000, cores=2)
    return trace

def plot_results(trace):
    """Plot the posterior distributions."""
    pm.plot_posterior(trace)
    plt.show()
