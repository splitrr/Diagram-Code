import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

Sankey(flows=[30, 30, 30, 10, 10, 10, 10, 10, 10, 10, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10, 10, 10],
       labels=['Generative AI', 'Robotics', 'Computer vision', 'Deep learning', 'Reinforcement learning', 'Probabilistic methods', 'Evolutionary algorithms', 'ANI Narrow general Intelligence', 'ANI Narrow general Intelligence', 'ML', 'AGI Artificial general Intelligence', 'ASI Super Intelligence', 'Generative AI', 'Robotics', 'Computer vision', 'Deep learning', 'Reinforcement learning', 'Probabilistic methods', 'Evolutionary algorithms', 'ANI Narrow general Intelligence', 'ANI Narrow general Intelligence', 'Symbolic AI (traditional automation', 'Symbolic AI (traditional automation'],
       orientations=[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
       facecolor='lightblue').finish()

plt.title('Sankey Diagram')
plt.show()