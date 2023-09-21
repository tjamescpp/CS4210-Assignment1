# -------------------------------------------------------------------------
# AUTHOR: Tommy
# FILENAME: decision_tree.py
# SPECIFICATION: read the file contact_lens.py and output a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features into numbers and add to the 4D array X.
# For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# --> add your Python code here

# feature_vals = {
#     'Young': 1,
#     'Prepresbyopic': 2,
#     'Presbyopic': 3,
#     'Myope': 1,
#     'Hypermetrope': 2,
#     'No': 2,
#     'Yes': 1,
#     'Reduced': 1,
#     'Normal': 2,
# }

# rows, cols = (10, 4)
# X = [[0]*cols]*rows

# for i in range(0, 10):
#     for j in range(0, 4):
#         X[i][j] = feature_vals[db[i][j]]


X = [[1, 1, 2, 1], [3, 1, 2, 2], [2, 1, 2, 1], [2, 1, 2, 2], [3, 1, 1, 2],
     [1, 1, 1, 2], [1, 2, 2, 1], [2, 1, 1, 1], [3, 2, 2, 1], [1, 1, 1, 1]]


# transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> addd your Python code here


Y = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1]

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=[
               'Yes', 'No'], filled=True, rounded=True)
plt.show()
