import turtle as t
import math
from random import *
from ga import *
t.speed(10)

t.degrees(360)
window = t.Screen()
window.setup(600, 600)

goalPoss = []
goal = [
    goalPoss.append(t.pos()),
    goalPoss.append(t.heading()),
    t.forward(60),
    goalPoss.append(t.pos()),
    t.left(90),
    goalPoss.append(t.heading()),
    t.forward(60),
    goalPoss.append(t.pos()),
    t.left(90),
    goalPoss.append(t.heading()),
    t.forward(60),
    goalPoss.append(t.pos()),
    t.left(90),
    goalPoss.append(t.heading()),
    t.forward(60),
    goalPoss.append(t.pos()),
    t.left(90),
    goalPoss.append(t.heading())
]


def make_next_chrom(previous_population, fitness_list):
  slected = select(previous_population, fitness_list)
    #roullete wheel return the two selcted parent
  child = crossover(slected)  # gets the parents returns the child
  individual = mutate(child)  #mutation
  return individual


def make_next_generation(previous_population, times, idealChrom, stx, sty,  sth):
  next_generation = []
  fitness_list = []
  for chrom in previous_population:

    value = fitnessfunc(robotgo(chrom, stx, sty, sth), chrom, times)
    t.clear()
 
    fitness_list.append(value)
# print("fitness list", fitness_list)
  bestScore = 0
  for i in fitness_list:
    if i > bestScore:
      bestScore = i
  best_overall_score.append(bestScore)
  print("best score", bestScore)
  print("best chrom", previous_population[fitness_list.index(bestScore)])

  next_generation.append(previous_population[fitness_list.index(bestScore)])

  for i in range(len(previous_population)-1):
    ind = make_next_chrom(previous_population, fitness_list)
    while ind == next_generation[i]:
      ind = make_next_chrom(previous_population, fitness_list)
    next_generation.append(ind)
     
  if times == 4:
    print(idealChrom)
  else:
    if bestScore > 15:
      times += 1
      print("times", times)
      bestCh = previous_population[fitness_list.index(bestScore)]
      idealChrom.append(bestCh)
      t.clear()
      robotgo(bestCh, stx, sty, sth)
      stx = t.xcor()
      sty = t.ycor()
      sth = t.heading()
      chromsize = 2
      popsize = 5
      populationtwo = generate_population(popsize, chromsize)
      make_next_generation(populationtwo, times, idealChrom, stx, sty, sth)
    else:
      print("times", times)
      make_next_generation(next_generation, times, idealChrom, stx, sty, sth)

chromsize = 2
popsize = 5
generations = 10
best_overall_score = []
times = 0
idealChrom = []
stx = 0.0
sty = 0.0
sth = 0.0
fitSide = 1 #which side of teh sqyare or teh fitness function
population = generate_population(popsize, chromsize)

make_next_generation(population, times, idealChrom, stx, sty, sth)
#  return next_generation

#while True:
 # print(f" GENERATION {i}")
    #for individual in population:
    #print(individual, fitnessFunc(individual))
 # if i == generations:
  #  break
 # i += 1
 # population = make_next_generation(population)

#best_individual = sort_population_by_fitness(population)[-1]
print(" FINAL RESULT")


#print(best_individual, fitnessfunc(best_individual))
