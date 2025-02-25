#!/usr/bin/env python3
import matplotlib
import numpy as np
import json
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from collections import Counter, defaultdict
from glob import glob

# command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

input_files = glob(args.input_dir + '/*')

for key in args.keys:
    total = defaultdict(lambda: Counter())
    yaxis = []
    
    for path in sorted(input_files):
        with open(path) as f:
            tmp = json.load(f)
            val = 0
            try:
                for k in tmp[key]:
                    val += tmp[key][k]
            except:
                pass
            yaxis.append(val)
    plt.plot(np.arange(len(yaxis)), yaxis, label=key)

plt.xlabel("Date in 2020")
plt.ylabel("# of Tweets")
plt.title("Number of Tweets with hashtag (2020)")
plt.legend()
plt.xticks([0, 60, 121, 182, 244, 305], ["Jan", "Mar", "May", "Jul", "Sept", "Nov"])
plt.savefig("myplot4.png", bbox_inches="tight")
