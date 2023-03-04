#Name: Sai Krishna Teja Varma Manthena  
#Unity ID: smanthe

from dimod import ExactSolver
sampler = ExactSolver()

Q = {('x', 'y'): 1, ('x', 'z'): 2, ('y', 'z'): 2, ('z', 'z'): -3, ('x', 'x'): -2, ('y', 'y'): -2}

response = sampler.sample_qubo(Q)
for datum in response.data(['sample','energy']):
	print(datum.sample, "Energy:", datum.energy)

# Output:
# {'x': 1, 'y': 1, 'z': 0} Energy: -3.0
# {'x': 0, 'y': 1, 'z': 1} Energy: -3.0
# {'x': 1, 'y': 0, 'z': 1} Energy: -3.0
# {'x': 0, 'y': 0, 'z': 1} Energy: -3.0
# {'x': 1, 'y': 0, 'z': 0} Energy: -2.0
# {'x': 0, 'y': 1, 'z': 0} Energy: -2.0
# {'x': 1, 'y': 1, 'z': 1} Energy: -2.0
# {'x': 0, 'y': 0, 'z': 0} Energy: 0.0