# stochastic_optimization
- Although Particle swarm optimization (PSO) is a simple algorithm to implement, it produces good results. PSO was developed by Eberhart and Kennedy in early 90, it is a biologically inspired optimization following to ant/bee colonies, or fish schooling. PSO is being used in a wide range of applications from antenna design, electromagnetic  applications, to a machine learning problems. Like many others stochastic optimization, PSO is not ensured to provide the global minimum, but it does a excellent and challenging tasks on such problems as high dimensional, non-convex problems. In this very short tutorial, I’ll show PSO in its simple form and implement it using numpy in matrix form.

- The basis PSO routine can be described as follows:

    I. Initialize
        1. Randomly initialize particle positions. 
        2. Randomly initialize particle velocities.
    II. Optimize
        LOOP
            1. Evaluate cost function at each particle position.
            2. Update all particle velocities.
            3. Update all particle positions.
            4. Update local best.
            5. Update global best.
        UNTIL Terminate condition is met.
- Test functions:
\begin{equation}
Cost = \sum_{i=1}^6 x_{i}^2,
\end{equation}
with the minimum value is 0 with all variables are zero.