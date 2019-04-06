#!/usr/bin/python3
#Use Python 3.
#By Georges Oates Larsen

import json
import sys
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

def Main():
	if (len(sys.argv) != 2):
		print("Usage: python3 AnalyzePoolCountSpectrum.py NameOfResultsFile.json")
	else:
		filename = sys.argv[1]
		with open(filename) as resultsFile:
			resultsData = json.load(resultsFile)
			resultsN = range(1, len(resultsData) + 1)
			resultsTotal = [0] * len(resultsData)
			resultsPerThread = [0] * len(resultsData)
			for datum in resultsData:
				print(datum)
				resultsTotal[datum[0]-1] = datum[1]
				resultsPerThread[datum[0]-1] = datum[1]/datum[0]
			df = pd.DataFrame(data={'Total hops/s': resultsTotal, 'Efficiency (hops/s/thread)':resultsPerThread}, index=resultsN)
			fig, ax = plt.subplots()
			ax2 = ax.twinx()
			df[df.columns[0]].plot(ax=ax, marker='o', linestyle='-', color='blue')
			df[df.columns[1]].plot(ax=ax2, marker='o', linestyle='-', color='orange')
			ax.set_xlabel('Pool Depth')
			ax.set_ylabel('Total hops/s')
			ax2.set_ylabel('Efficiency (hops/s/thread)')
			
			lines1, labels1 = ax.get_legend_handles_labels()
			lines2, labels2 = ax2.get_legend_handles_labels()
			
			ax.legend(lines1 + lines2, labels1 + labels2)
			ax.set_ylim(0, ax.get_ylim()[1] * 1.5)
			ax2.set_ylim(0, ax2.get_ylim()[1] * 1.5)
			mplcursors.cursor(lines1)
			mplcursors.cursor(lines2)
			
			
			plt.show()

if (__name__ == '__main__'):
	Main()
