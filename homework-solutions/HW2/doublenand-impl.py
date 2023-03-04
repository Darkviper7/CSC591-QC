#Name: Sai Krishna Teja Varma Manthena  
#Unity ID: smanthe

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = value + dict_1[key]
   return dict_3

def gen_qubo(n):
  if n <= 0:
    return {}
  Q = {('q1','q1'):-2, ('q2','q2'):-2,('q3','q3'):-3,('q1','q2'):1,('q1','q3'):2,('q2','q3'):2}
  if n == 1:
    return Q
  for i in range(2, n+1):
    k = i*2 - 1
    Q1 = {('q' + str(k),'q' +str(k)):-2, ('q'+str(k+1),'q' + str(k+1)):-2,('q' + str(k+2),'q' + str(k+2)):-3,('q' + str(k),'q' +str(k+1)):1,('q'+str(k),'q'+str(k+2)):2,('q' +str(k+1),'q' +str(k+2)):2}
    Q = mergeDictionary(Q, Q1)
  return Q

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

Q = gen_qubo(4)

response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

print("\nQubo for n = 4:")
print(gen_qubo(4))

#Output
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -6.0 Occurrences:  657
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -6.0 Occurrences:  656
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -6.0 Occurrences:  522
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -6.0 Occurrences:  859
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -6.0 Occurrences:  408
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -6.0 Occurrences:  511
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  -6.0 Occurrences:  466
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -6.0 Occurrences:  920
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -5.0 Occurrences:  1

# Qubo for n = 4:
# {('q1', 'q1'): -2, ('q2', 'q2'): -2, ('q3', 'q3'): -5, ('q1', 'q2'): 1, ('q1', 'q3'): 2, ('q2', 'q3'): 2, ('q4', 'q4'): -2, ('q5', 'q5'): -5, ('q3', 'q4'): 1, ('q3', 'q5'): 2, ('q4', 'q5'): 2, ('q6', 'q6'): -2, ('q7', 'q7'): -5, ('q5', 'q6'): 1, ('q5', 'q7'): 2, ('q6', 'q7'): 2, ('q8', 'q8'): -2, ('q9', 'q9'): -3, ('q7', 'q8'): 1, ('q7', 'q9'): 2, ('q8', 'q9'): 2}