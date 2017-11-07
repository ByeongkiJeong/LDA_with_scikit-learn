import pandas as pd
import numpy as np

def __init__(self):
    return

def Edgelist2Matrix(self, edgelist):
    source = np.unique(edgelist[edgelist.columns[0]].values)
    target = np.unique(edgelist[edgelist.columns[1]].values)
    matrix = pd.DataFrame(np.zeros([len(source), len(target)]), index=source, columns=target)
    for _, row in edgelist.iterrows():
        Source, Target, Weight = row
        try:
            matrix.loc[Source, Target] = Weight
        except KeyError:
            continue
    return matrix

def Matrix2Edgelist(self, matrix):
    edgelist = [('Source','Target','Weight')]
    for source in matrix.index.values:
        for target in matrix.index.values:
            edgelist.append((target,source,matrix[source][target]))
    return pd.DataFrame(edgelist)

def WriteCSV(self, filename, matrix):
    matrix.to_csv(filename)

def WriteXLSX(self, filename, matrix):
    matrix.to_excel(filename)

def ReadCSV(self, filename, delimiter, ind_col = None):
    return pd.read_csv(filename,delimiter=delimiter) if ind_col == None else pd.read_csv(filename,delimiter=delimiter, index_col=ind_col)

def ReadXLSX(self, filename, ind_col = None):
    return pd.read_excel(filename) if ind_col == None else pd.read_excel(filename, index_col=ind_col)

if __name__ == "__main__":
    m = Edgelist2Matrix("edgelist.csv", ',')
    WriteCSV("test.csv", m)
    WriteXLSX("test.xlsx", m)