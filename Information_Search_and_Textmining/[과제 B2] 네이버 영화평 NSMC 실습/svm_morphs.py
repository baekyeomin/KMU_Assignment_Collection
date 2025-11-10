import numpy as np
from scipy.sparse import coo_matrix
from sklearn.svm import LinearSVC
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
            rows.append(int(i)); cols.append(int(j)); data.append(float(v))
    if n_rows is None or n_cols is None:
        n_rows = max(rows) + 1
        n_cols = max(cols) + 1
    return coo_matrix((data, (rows, cols)), shape=(n_rows, n_cols)).tocsr()

X_train = load_coo_from_txt("train_tfidf_coo_morphs.txt")
X_test  = load_coo_from_txt("test_tfidf_coo_morphs.txt")

with open("train_labels_morphs.txt","r",encoding="utf-8") as f:
    y_train = np.array([int(x.strip()) for x in f])
with open("test_labels_morphs.txt","r",encoding="utf-8") as f:
    y_test  = np.array([int(x.strip()) for x in f])

clf = LinearSVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
