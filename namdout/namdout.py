import os

import numpy as np
import pandas as pd


def read_headers(fin):
    for line in fin:
        if line.startswith("ETITLE:"):
            return [s.lower() for s in line.split()[1:]]


def read_values(fin):
    values = []
    for line in fin:
        if line.startswith("ENERGY:"):
            v = [float(s) for s in line.split()[1:]]
            values.append(v)
    return np.array(values)


def read(filename):
    with open(filename, "r") as fin:
        headers = read_headers(fin)
        values = read_values(fin)
        df = pd.DataFrame({h: v for h, v in zip(headers, values.T)})

        df["filename"] = os.path.splitext(filename)[0]
        df["filename"] = df["filename"].astype("category")

        return df
