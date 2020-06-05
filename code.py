from random import randint

N=100000
def simulate(N):
  K = 0
  for i in range(N):
    truth = randint(1,3)
    guess1 = randint(1,3)
    if truth == guess1:
      monty = randint(1,3)
      while monty ==  truth:
        monty = randint(1,3)
        
    else :
      monty = 6 - truth - guess1
    guess2 = 6 - guess1 - monty
    
    if guess2 == truth:
      K = K + 1
  return float(K) / float(N)

print("Probability of winning a car by switching is",simulate(N))           
