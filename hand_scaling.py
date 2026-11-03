#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:54:55 2026

@author: karelgreen
"""

#%%Modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%Data

df = pd.DataFrame({
    "Chips": [5, 10, 20, 30, 30, 35, 40, 60, 100, 120, 140, 160],
    "Mult": [1, 2, 2, 3, 4, 4, 4, 7, 8, 12, 14, 16],
    "Planet": ["Pluto", "Mercury", "Uranus", "Venus",
               "Saturn", "Jupiter", "Earth", "Mars",
               "Neptune", "Planet X", "Ceres", "Eris"],
    "+Chips": [10, 15, 20, 20, 30, 15, 25, 30, 40, 35, 40, 50],
    "+Mult":  [1, 1, 1, 2, 3, 2, 2, 3, 4, 3, 4, 3]
    }, 
    index=["High Card", "Pair", "Two Pair", "Three of a Kind",
           "Straight", "Flush", "Full House", "Four of a Kind",
           "Straight Flush", "Five of a Kind", "Flush House", "Flush Five"])

df.index.name = "Hand"

#%%Plotting

levels = np.arange(1, 11)

plt.figure(figsize=(12, 7))

# colors = plt.cm.rainbow(np.linspace(0, 1, len(df)))
colors = plt.cm.hsv(np.linspace(0, 1, len(df), endpoint=False))

for i, ((hand, row), color) in enumerate(zip(df.iterrows(), colors)):
    chips = row["Chips"] + (levels - 1) * row["+Chips"]
    mult = row["Mult"] + (levels - 1) * row["+Mult"]
    score = chips * mult

    linestyle = "-" if i % 2 == 0 else "--"

    plt.plot(levels, score, label=hand, color=color,
             linewidth=2, linestyle=linestyle)

plt.xlabel("Level")
plt.ylabel("Score (Chips × Mult)")
plt.title("Balatro Hand Score by Level")
plt.xticks(levels)

handles, labels = plt.gca().get_legend_handles_labels()

plt.legend(handles[::-1], labels[::-1],
           title="Hand",
           loc="upper left")

plt.grid(True, alpha=0.3)
# plt.yscale("log")
plt.tight_layout()
plt.show()