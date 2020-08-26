import turtle as t
import math
from random import *
t.degrees(360)
window=t.Screen()
window.setup(600,600)


#     F    T.    H

### Importation of Data from Robot Possible Movements ##
#       T     F     H
#[[0, [4.20, 0.18, 29.90]], 
#[1, [5.22, 2.57, 21.17]], 
#	[2, [5.19, 2.96, 11.68]], 
#	[3, [6.18, 3.05, 6.15]],
#	[4, [5.58, 5.13, 3.79]],
#	[5, [4.36, 7.20, 2.86]], 
#	[6, [3.18, 8.10, 1.94]],
#	[7, [0.78, 9.37, 1.18]],
#	[8, [0.78, 9.37, 1.18]], 
#	[9, [-1.68, 7.69, -1.23]],
#	[10, [-2.75, 7.31, -1.71]],
#	[11, [-4.52, 5.78, -3.42]], 
#	[12, [-4.66, 4.81, -6.26]], 
#	[13, [-4.90, 3.64, -10.48]], 
#	[14, [-5.05, 2.25, -22.47]],
#	[15, [-4.83, 0.04, -29.71]]]

def generate_individual(chromsize):
  chrom = []
  for i in range(chromsize):
    ch = randrange(0,16)
    times= randrange(1,6)
    p = [ch,times]
    chrom.append(p)
  return chrom 
def generate_population(popsize,chromsize ):
    return [generate_individual(chromsize) for i in range(popsize)]

#XorYerr, limit, line, headturn
def fitnessfunc(robotPoss, chrom, times):
  if times == 0: #doing teh first
    #print(robotPoss)
    yerr = 0 # y err
    herr = 0 #heading err
    lerr = 0 # how close are you to 60
    for num in range(len(robotPoss)):
      if isinstance(robotPoss[num], float): #it is heading
        None
      else:
         #cheacks if y is the error then we check how close x is to th target and vis verca
        lerr = robotPoss[-2][0] - 60 #checks how close we are to 60 or 0
        lerr = lerr * 3
        herr = abs(robotPoss[-1]) - 90 #heading err
        herr = herr 
        yerr += abs(robotPoss[num][1]) - 0
         #find the x or y error
    err = abs(yerr) + abs(lerr) + abs(herr)
    fit = 1000/(err+1)

  elif times == 1:
    #print(robotPoss)
    yerr = 0 # y err
    herr = 0 #heading err
    lerr = 0 # how close are you to 60
    for num in range(len(robotPoss)):
      if isinstance(robotPoss[num], float): #it is heading
        None
      else:
         #cheacks if y is the error then we check how close x is to th target and vis verca
        lerr = robotPoss[-2][1] - 60 #checks how close we are to 60 or 0
        lerr = lerr * 3
        herr = abs(robotPoss[-1]) - 180 #heading err
        herr = herr 
        yerr += abs(robotPoss[num][0]) - 60
         #find the x or y error
    err = abs(yerr) + abs(lerr)  + abs(herr)
    fit = 1000/(err+1)

  elif times == 2:
    #print(robotPoss)
    yerr = 0 # y err
    herr = 0 #heading err
    lerr = 0 # how close are you to 60
    for num in range(len(robotPoss)):
      if isinstance(robotPoss[num], float): #it is heading
        None
      else:
         #cheacks if y is the error then we check how close x is to th target and vis verca
        lerr = robotPoss[-2][0] - 0 #checks how close we are to 60 or 0
        lerr = lerr * 3
        herr = abs(robotPoss[-1]) - 275 #heading err
        herr = abs(herr) 
        yerr += abs(robotPoss[num][1]) - 60
         #find the x or y error
    err = abs(yerr) + abs(lerr)  + abs(herr)
    fit = 1000/(err+1)

  elif times == 3:
    #print(robotPoss)
    yerr = 0 # y err
    herr = 0 #heading err
    lerr = 0 # how close are you to 60
    for num in range(len(robotPoss)):
      if isinstance(robotPoss[num], float): #it is heading
        None
      else:
         #cheacks if y is the error then we check how close x is to th target and vis verca
        lerr = robotPoss[-2][1] - 0 #checks how close we are to 60 or 0
        lerr = lerr * 3
        if abs(robotPoss[-1]) > 0 and abs(robotPoss[-1]) < 180:
          ht = 0
        else:
          ht = 360
        herr = abs(robotPoss[-1]) - ht #heading err
        herr = herr 
        yerr += abs(robotPoss[num][0]) - 0
         #find the x or y error
    err = abs(yerr) + abs(lerr)  + abs(herr)
    fit = 1000/(err+1)
  return fit

def select(population, fitness_list):
	## Calculate Sum of Total Fitness of Entire Population 
  total = 0 
  for i in range(len(fitness_list)):
    total += fitness_list[i]
	## Calculate Probability to Select Each Individual ##
  probability_list = []
  for j in range(len(fitness_list)):
    prob = float(fitness_list[j])/total
    probability_list.append(prob)

  parents = []
  parent1=choices(population, probability_list)
  parent2=choices(population, probability_list)

  while parent1 == parent2:
    parent2 = choices(population, probability_list)
  parents.append(parent1[0])
  parents.append(parent2[0])
  return parents


def crossover(parents):
  parent1 = parents[0]
  parent2 = parents[1]
  child = []
  chrom = randrange(0,2)
  spot = randrange(0,len(parent1))
  if chrom == 0:
    chromosome1_part1 = parent1[:spot]
    chromosome1_part2 = parent2[spot:]
    chromosome2_part1 = parent2[:spot]
    chromosome2_part2 = parent1[spot:]
  else:
    chromosome1_part1 = parent2[:spot]
    chromosome1_part2 = parent1[spot:]
    chromosome2_part1 = parent1[:spot]
    chromosome2_part2 = parent2[spot:]
  chromosome1 = chromosome1_part1 + chromosome1_part2
  chromosome2 = chromosome2_part1 + chromosome2_part2
  child.append(chromosome1)
  child.append(chromosome2)
  which = randrange(0,2)
  return child[which]

def mutate(individual):
  for i in range(len(individual)):
    rand1 = randrange(100)
    rand2 = randrange(100)
    if rand1 == 5:
      ch = randrange(0,16)
      times= randrange(1,5)
      p = [ch,times]
      individual[i] = p
    if rand2 == 4:
      ch = randrange(0,16)
      times= randrange(1,6)
      individual[i][0] = ch
    elif rand2 == 3:
      times= randrange(1,11)
      individual[i][1] = times
  return individual

  
def robotgo(chrom, stx, sty, sth):
  t.setx(stx)
  t.sety(sty)
  t.seth(sth)
  robotPoss = []
  robotPoss.append(t.pos())
  robotPoss.append(t.heading())
  for sets in chrom:
    #       T     F     H
  #[[0, [4.20, 0.18, 29.90]], 
    if sets[0] == 0:
      for n in range(sets[1]):
        t.forward(0.18)
        t.left(90)
        t.forward(4.20)
        t.right(90)
        t.right(29.90)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #[1, [5.22, 2.57, 21.17]], 
    if sets[0] == 1:
      for n in range(sets[1]):
        t.forward(2.57)
        t.left(90)
        t.forward(5.22)
        t.right(90)
        t.right(21.17)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[2, [5.19, 2.96, 11.68]], 

    if sets[0] == 2:
      for n in range(sets[1]):
        t.forward(2.96)
        t.left(90)
        t.forward(5.19)
        t.right(90)
        t.right(11.68)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[3, [6.18, 3.05, 6.15]],
    if sets[0] == 3:
      for n in range(sets[1]):
        t.forward(3.05)
        t.left(90)
        t.forward(6.18)
        t.right(90)
        t.right(6.15)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[4, [5.58, 5.13, 3.79]],
    if sets[0] == 4:
      for n in range(sets[1]):
        t.forward(5.13)
        t.left(90)
        t.forward(5.58)
        t.right(90)
        t.right(3.79)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[5, [4.36, 7.20, 2.86]], 
    if sets[0] == 5:
      for n in range(sets[1]):
        t.forward(7.20)
        t.left(90)
        t.forward(4.36)
        t.right(90)
        t.right(2.86)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
      
    
    #	[6, [3.18, 8.10, 1.94]],
    if sets[0] == 6:
      for n in range(sets[1]):
        t.forward(8.10)
        t.left(90)
        t.forward(3.18)
        t.right(90)
        t.right(1.94)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
      
    #	[7, [0.78, 9.37, 1.18]],
    if sets[0] == 7:
      for n in range(sets[1]):
        t.forward(9.37)
        t.left(90)
        t.forward(0.78)
        t.right(90)
        t.right(1.18)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[8, [0.78, 9.37, 1.18]], 
    if sets[0] == 8:
      for n in range(sets[1]):
        t.forward(9.37)
        t.left(90)
        t.forward(0.78)
        t.right(90)
        t.right(1.18)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
        
  #	[9, [-1.68, 7.69, -1.23]],
    if sets[0] == 9:
      for n in range(sets[1]):
        t.forward(7.69)
        t.left(90)
        t.forward(-1.68)
        t.right(90)
        t.right(-1.23)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[10, [-2.75, 7.31, -1.71]], 
    if sets[0] == 10:
      for n in range(sets[1]):
        t.forward(7.31)
        t.left(90)
        t.forward(-2.75)
        t.right(90)
        t.right(-1.71)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
        
  #	[11, [-4.52, 5.78, -3.42]], 
    if sets[0] == 11:
      for n in range(sets[1]):
        t.forward(5.78)
        t.left(90)
        t.forward(-4.52)
        t.right(90)
        t.right(-3.42)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[12, [-4.66, 4.81, -6.26]],   
    if sets[0] == 12:
      for n in range(sets[1]):
        t.forward(4.81)
        t.left(90)
        t.forward(-4.66)
        t.right(90)
        t.right(-6.26)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[13, [-4.90, 3.64, -10.48]], 
    if sets[0] == 13:
      for n in range(sets[1]):
        t.forward(3.64)
        t.left(90)
        t.forward(-4.90)
        t.right(90)
        t.right(-10.48)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
        
  #	[14, [-5.05, 2.25, -22.47]],
    if sets[0] == 14:
      for n in range(sets[1]):
        t.forward(2.25)
        t.left(90)
        t.forward(-5.05)
        t.right(90)
        t.right(-22.47)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())

  #	[15, [-4.83, 0.04, -29.71]]] 
    if sets[0] == 15:
      for n in range(sets[1]):
        t.forward(0.04)
        t.left(90)
        t.forward(-4.83)
        t.right(90)
        t.right(-29.71)
        robotPoss.append(t.pos())
        robotPoss.append(t.heading())
  return robotPoss
