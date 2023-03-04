#Name: Sai Krishna Teja Varma Manthena  
#Unity ID: smanthe

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = value + dict_1[key]
   return dict_3

def gen_qubo(t):
  i,j,k = t[0],t[1],t[2]
  Q1 = {('q' + i,'q' +i):-2, ('q'+j,'q' + j):-2,('q' + k,'q' + k):-3,('q' + i,'q' +j):1,('q'+i,'q'+k):2,('q' +j,'q' +k):2}
  return Q1

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

Q = {}
chain = [("1","2","3"), ("1","3","4"),("2","3","5"),("4","5","6")]
for i in chain:
  Q = mergeDictionary(Q, gen_qubo(i))

# Q = {('q1','q1'):-4, ('q2','q2'):-4,('q3','q3'):-7,('q4','q4'):-5, ('q5','q5'):-5,('q6','q6'):-3,('q1','q2'):1,('q1','q3'):3,('q1','q4'):2,('q2','q3'):3,('q2','q5'):2,('q3','q4'):2,('q3','q5'):2,('q4','q5'):1,('q4','q6'):2,('q5','q6'):2}

response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

# Output:
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 1} Energy:  -12.0 Occurrences:  725
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -12.0 Occurrences:  1193
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 1} Energy:  -12.0 Occurrences:  1372
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -12.0 Occurrences:  1152
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1} Energy:  -11.0 Occurrences:  36
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 0} Energy:  -11.0 Occurrences:  38
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 1} Energy:  -11.0 Occurrences:  55
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 0} Energy:  -11.0 Occurrences:  24
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 1} Energy:  -11.0 Occurrences:  55
# {'q1': 1, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1} Energy:  -11.0 Occurrences:  23
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1} Energy:  -11.0 Occurrences:  27
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -11.0 Occurrences:  35
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 1} Energy:  -11.0 Occurrences:  49
# {'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -11.0 Occurrences:  34
# {'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -11.0 Occurrences:  35
# {'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 0} Energy:  -11.0 Occurrences:  28
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 1} Energy:  -11.0 Occurrences:  28
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 1} Energy:  -11.0 Occurrences:  28
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 1} Energy:  -11.0 Occurrences:  42
# {'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 1} Energy:  -10.0 Occurrences:  1
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0} Energy:  -10.0 Occurrences:  3
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 0} Energy:  -10.0 Occurrences:  2
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1} Energy:  -10.0 Occurrences:  1
# {'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 1} Energy:  -10.0 Occurrences:  5
# {'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 0} Energy:  -10.0 Occurrences:  3
# {'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 1} Energy:  -10.0 Occurrences:  1
# {'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 1} Energy:  -10.0 Occurrences:  2
# {'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 1} Energy:  -10.0 Occurrences:  3


