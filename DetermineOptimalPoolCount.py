#!/usr/bin/python3
#Use Python 3.
#By Georges Oates Larsen

import multiprocessing
import random
import time
import json

def Main():
	threadCount = multiprocessing.cpu_count()
	results = []
	maxDepth = threadCount * 3
	print("You have %i available threads. We will perform 10-second tests at every pool depth from 1 up to %i and determine the optimal pool depth." % (threadCount, maxDepth))
	print("This test will take approximately %0.1f minutes" % (maxDepth * 10/60))
	maxn = 0
	maxResult = 0
	for n in range(1, maxDepth + 1):
		print("Performing round at pool depth %i. %i tests remaining." % (n, maxDepth - n + 1))
		result = TestNProc(n)
		print("At this pool depth you achieve %0.1f hops/s (that's %0.1f hops/(s * worker)" % (result, (result/n)))
		if (result > maxResult):
			maxResult = result
			maxn = n
		results.append((n, result))
	print("Maximal hops/s was %0.1f, and as achieved with pool depth %i" %(maxResult, maxn))
	if (input("Save results? (y/n): ") == 'y'):
		name = input("Enter filename (include .json): ")
		with open(name, 'w') as resultsFile:
			json.dump(results, resultsFile)


def TestNProc(n):
	p = multiprocessing.Pool(n)
	return sum(p.map(WorkHard, range(n)))

def WorkHard(dummyVar):
	startTime = time.time()
	totalChallenges = 0
	while (time.time() - startTime) < 10:
		DoStandardChallenge()
		totalChallenges += 1
	return float(totalChallenges) / (time.time() - startTime) #In case someone is silly enough to try to make this work in python2, I have fixed a bug in advance for them by casting to float.

def DoStandardChallenge():
	#Purposefully do not use numpy here, soas to keep the dependencies bare bones, and the workload explicitly understood.
	#Construct (not very efficiently) a couple of 10 x 10 matrices:
	matrix = []
	matrixResult = []
	for x in range(0, 10):
		matrix.append([])
		matrixResult.append([])
		for y in range(0, 10):
			matrix[x].append(random.uniform(-1000, 1000))
			matrixResult[x].append(0)
	
	#Multiply this matrix by itself (not very efficiently)
	for x in range(0, 10):
		for y in range(0, 10):
			total = 0
			for z in range(0, 10):
				total += matrix[x][z] * matrix[z][y]
			matrixResult[x][y]
if (__name__ == '__main__'):
	Main()
