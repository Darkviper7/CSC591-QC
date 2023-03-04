#Name: Sai Krishna Teja Varma Manthena  
#Unity ID: smanthe

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

Q = {('x','y'):1, ('x','z'):2, ('y','zz'):2, ('z','zz'):-2, ('z','z'):-0.5, ('zz','zz'):-0.5, ('x','x'):-2, ('y','y'):-2}

response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

#Output
# {'x': 1, 'y': 0, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  1305
# {'x': 1, 'y': 1, 'z': 0, 'zz': 0} Energy:  -3.0 Occurrences:  1374
# {'x': 0, 'y': 1, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  994
# {'x': 0, 'y': 0, 'z': 1, 'zz': 1} Energy:  -3.0 Occurrences:  1295
# {'x': 1, 'y': 0, 'z': 0, 'zz': 1} Energy:  -2.5 Occurrences:  12
# {'x': 0, 'y': 1, 'z': 1, 'zz': 0} Energy:  -2.5 Occurrences:  18
# {'x': 1, 'y': 1, 'z': 1, 'zz': 1} Energy:  -2.0 Occurrences:  2