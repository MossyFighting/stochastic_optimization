import random
import numpy as np
import matplotlib.pyplot as plt

# set search-space boundary
b_lo = -5.0
b_up = 5.0
# Set swamp parameters 
n_particle = 200
n_dimension = 10
# position parameters
lr = 0.5
phi_local = 2
phi_global = 2
omega = 0.5

# compute all particles
def compute_cost(position_particle):
  cost = np.sum(position_particle**2, axis = 1)
  return cost

def update_local_best(x_particle, x_local_best):
  immediate_cost = compute_cost(x_particle)
  local_cost = compute_cost(x_local_best)
  mask = immediate_cost < local_cost
  x_local_best[mask,:] = x_particle[mask, :]
  return x_local_best

def select_best_among_local_best(x_local_best):
  cost = compute_cost(x_local_best)
  return  x_particle[np.argmin(cost)], np.min(cost)

# update velocity
def update_velocity(omega, 
                    v_particle, x_particle,
                    r_local, r_global, 
                    phi_local, phi_global, 
                    x_local_best, x_global_best):
  # scale velocity 
  _velocity_term = omega*v_particle
  # local interaction
  _local_term = phi_local*r_local*(x_local_best - x_particle)
  # global interaction
  _global_term = phi_global*r_global*(x_global_best - x_particle)
  new_velocity = _velocity_term + _local_term + _global_term
  return new_velocity
def update_pisition(x_particle, new_velocity, lr):
  return x_particle + lr*new_velocity

# run the PSO
n_iteration = 50
global_cost = []
np.random.seed(11111111)
r_local = np.random.uniform(low = 0, high = 1, size=(n_particle, n_dimension))
r_global = np.random.uniform(low = 0, high = 1, size=(n_particle, n_dimension))
# 1. generate position, local_best, global best in matrix form
x_particle = np.random.uniform(low = b_lo, high = b_up, size=(n_particle, n_dimension))
x_local_best = x_particle.copy()
x_global_best = np.random.uniform(low = b_lo, high = b_up, size=(1, n_dimension))
# 2. update local best, and update global best
x_local_best = update_local_best(x_particle, x_local_best)
entity_best, entity_cost = select_best_among_local_best(x_local_best)
if compute_cost(x_global_best)[0] > entity_cost:
  x_global_best = entity_best.reshape(1,n_dimension)
# 3. generate velocity
v_particle = np.random.uniform(low = b_lo , high = b_up, size = (n_particle, n_dimension))
# 4. start the PSO
for iter in range(n_iteration):
  # 4.1 ----- update velocity
  v_particle = update_velocity(omega, 
                                v_particle, x_particle,
                                r_local, r_global, 
                                phi_local, phi_global, 
                                x_local_best, x_global_best)
  # 4.2 ----- update position
  x_particle = update_pisition(x_particle, v_particle, lr)
  x_particle = np.clip(x_particle, b_lo, b_up)
  # 4.3 ----- update local best
  x_local_best = update_local_best(x_particle, x_local_best)
  x_local_best = np.clip(x_local_best, b_lo, b_up)
  # 4.4 ----- update global best
  x_entity_best, entity_cost = select_best_among_local_best(x_local_best)
  if compute_cost(x_global_best)[0] > entity_cost:
    x_global_best = x_entity_best.reshape(1,n_dimension)
  global_cost.append(compute_cost(x_global_best)[0])
  print("Iter: {}, cost: {}".format(iter, compute_cost(x_global_best)[0]))
print(x_global_best)
