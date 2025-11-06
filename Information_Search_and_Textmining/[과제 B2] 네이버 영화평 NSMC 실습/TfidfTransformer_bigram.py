import sklearn
import re
import nltk
import unicodedata
import numpy as np
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#처음 1회 다운로드를 위해 적은 부분
'''
nltk.download('punkt')
nltk.download('punkt_tab')
'''

#전처리
def clean_text(s):
    s = unicodedata.normalize('NFKC', s)              # 전각/호환 문자 표준화
    s = s.replace('�', ' ')                            # 깨진 글자 제거
    s = re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', s)       # 제어문자 제거
    s = re.sub(r'[^가-힣A-Za-z\s]', ' ', s)          # 한글·영문 외 숫자 및 기호 제거
    s = re.sub(r'\s+', ' ', s).strip()                 # 공백 정리
    return s

#데이터 로드
rows = []
with open("train.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line or ',' not in line: 
            continue
        # 맨 마지막 쉼표는 label 앞이므로, 오른쪽 쉼표 한 개 기준으로 split해서 label 제거합니다
        review, label = line.rsplit(",", 1)
        label = label.strip().strip('"').strip("'")  # 따옴표가 있으면 제거

        # 라벨이 0/1 숫자인지 검사. 아니면 스킵
        if label not in {"-1", "1"}:
            continue
        rows.append((clean_text(review), label))

corpus = [r for r, _ in rows]
labels = [l for _, l in rows]

cv = CountVectorizer(preprocessor=clean_text, analyzer='word', ngram_range=(2, 2))    # word bigram 
X = cv.fit_transform(corpus)
tfidf_trans = TfidfTransformer()
X2 = tfidf_trans.fit_transform(X)

words =  cv.get_feature_names_out()

# 결과 희소 행렬로 텍스트 파일로 저장
def save_sparse_as_coo_txt(path, spmat, float_fmt="%.6f"):
    coo = spmat.tocoo(copy=False)
    n_rows, n_cols = coo.shape
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# shape={n_rows},{n_cols} nnz={coo.nnz} format=coo\n")
        is_int = str(coo.data.dtype).startswith(("int", "uint"))
        if is_int:
            for i, j, v in zip(coo.row, coo.col, coo.data):
                f.write(f"{int(i)} {int(j)} {int(v)}\n")
        else:
            for i, j, v in zip(coo.row, coo.col, coo.data):
                f.write(f"{int(i)} {int(j)} {float_fmt % float(v)}\n")

save_sparse_as_coo_txt("train_count_coo_bigram.txt", X)          # Count (정수)
save_sparse_as_coo_txt("train_tfidf_coo_bigram.txt", X2)         # TF-IDF (실수)

#CountVectorizer가 전체 코퍼스(리뷰들)에서 어떤 단어를 몇 번째 열(column)에 매핑했는지에 대한 정보
with open("train_vocab_bigram.tsv", "w", encoding="utf-8") as f:
    f.write("# col_index\ttoken\n")
    for idx, tok in enumerate(words):
        f.write(f"{idx}\t{tok}\n")

#라벨을 영화평 순서대로 저장
with open("train_labels_bigram.txt", "w", encoding="utf-8") as f:
    for y in labels:
        f.write(str(y).strip() + "\n")

# CountVectorizer, TF-IDF 모델 저장
joblib.dump(cv, "countvectorizer_bigram.pkl")
joblib.dump(tfidf_trans, "tfidf_transformer_bigram.pkl")

#test 데이터에 대해서도 파일 만들기
cv = joblib.load("countvectorizer_bigram.pkl")
tfidf_trans = joblib.load("tfidf_transformer_bigram.pkl")

rows = []
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line or ',' not in line:
            continue
        review, label = line.rsplit(",", 1)
        rows.append((clean_text(review), label))

test_corpus = [r for r, _ in rows]
test_labels = [l for _, l in rows]

X_test = cv.transform(test_corpus)
X_test_tfidf = tfidf_trans.transform(X_test)

# 저장
save_sparse_as_coo_txt("test_count_coo_bigram.txt", X_test)
save_sparse_as_coo_txt("test_tfidf_coo_bigram.txt", X_test_tfidf)

# vocab은 train과 동일하게 유지
words = cv.get_feature_names_out()
with open("test_vocab_bigram.tsv", "w", encoding="utf-8") as f:
    f.write("# col_index\ttoken\n")
    for idx, tok in enumerate(words):
        f.write(f"{idx}\t{tok}\n")

# 라벨 저장
with open("test_labels_bigram.txt", "w", encoding="utf-8") as f:
    for y in test_labels:
        f.write(str(y).strip() + "\n")