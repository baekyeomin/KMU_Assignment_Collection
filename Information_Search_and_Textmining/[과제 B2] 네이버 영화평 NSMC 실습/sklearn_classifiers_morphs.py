import numpy as np
from scipy.sparse import coo_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


def load_coo_from_txt(path):
    rows, cols, data = [], [], []
    n_rows = n_cols = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                try:
                    meta = line.strip().split()
                    shape = meta[1].split("=")[1]  
                    n_rows, n_cols = map(int, shape.split(","))
                except:
                    pass
                continue
            i, j, v = line.strip().split()
            rows.append(int(i))
            cols.append(int(j))
            data.append(float(v))
    if n_rows is None or n_cols is None:
        n_rows = max(rows) + 1
        n_cols = max(cols) + 1
    return coo_matrix((data, (rows, cols)), shape=(n_rows, n_cols)).tocsr()


X_train = load_coo_from_txt("train_tfidf_coo_morphs.txt")
X_test  = load_coo_from_txt("test_tfidf_coo_morphs.txt")

with open("train_labels_morphs.txt", "r", encoding="utf-8") as f:
    y_train = np.array([int(x.strip()) for x in f])

with open("test_labels_morphs.txt", "r", encoding="utf-8") as f:
    y_test = np.array([int(x.strip()) for x in f])


def train_and_eval(name, clf):
    print(f"{name}")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    return clf


# 1. Logistic Regression 
lr = LogisticRegression(max_iter=500, random_state=0)
train_and_eval("Logistic Regression", lr)

# 2. Decision Tree 
dt = DecisionTreeClassifier(criterion="gini", max_depth=None, random_state=0)
train_and_eval("Decision Tree", dt)

# 4. Naive Bayes (MultinomialNB)
nb = MultinomialNB()
train_and_eval("Multinomial Naive Bayes", nb)

# 5. Random Forest 
rf = RandomForestClassifier(n_estimators=100,max_depth=None, n_jobs=-1,random_state=0)
train_and_eval("Random Forest", rf)
