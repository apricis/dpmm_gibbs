# -*- coding: utf-8 -*-
# @Author: dmytro
# @Date:   2017-01-02 10:33:56
# @Last Modified by:   Dmytro Kalpakchi
# @Last Modified time: 2017-01-04 22:25:35

import numpy as np
import matplotlib.pyplot as plt
from dpm import DPM


# data generation params
D = 2
K_genuine = 3
colors = np.array(['b', 'r', 'g', 'm', 'y', 'k', 'c'])
N = 100
mu = np.array([0, 0.5])
tau_sq = 9
sigma_sq = 0.5

# data construction
true_z = np.arange(N) % K_genuine # clusters
c = colors[true_z]
theta_k = np.array([np.random.multivariate_normal(mu, tau_sq * np.eye(D)) for _ in xrange(K_genuine)])
x = np.array([np.random.multivariate_normal(th, sigma_sq * np.eye(D)) for th in theta_k[true_z]])

plt.scatter(x[:,0], x[:,1], c=c)
plt.savefig("gibbs_genuine.png")

# hyperparameters
alpha = 1.0
K = 1

z = np.arange(N) % K

dpm = DPM(x, z, K, mu, sigma_sq, tau_sq, alpha)
dpm.gibbs_sample()
