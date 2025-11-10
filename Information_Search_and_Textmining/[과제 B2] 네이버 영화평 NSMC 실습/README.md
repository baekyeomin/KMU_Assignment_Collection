# [과제 B2] 네이버 영화평 NSMC 실습

### 과제 개요
네이버 영화평 데이터셋(NSMC, 약 28만개 리뷰)을 이용하여 형태소분석/음절ngram(bigram)으로 텍스트 데이터를 벡터화하고, <br>
SVM 및 로지스틱 회귀(Logistic Regression) 모델로 문서 분류 실습을 수행했습니다.


### 실습 과정
- 원본 파일 NSMC_282K(ratings200K+kmuNP82K).txt을 train:test = 9:1 비율로 분리
- ID 열 제거 후 review와 label 부분만 저장하고, label=0 → -1로 변환
- **형태소 분석(nltk.word_tokenize)** 을 이용해 텍스트를 토큰화  
- 텍스트 문서 전처리 : 깨진 글자, 특수문자, 제어문자 등 제거
- **CountVectorizer**와 **TfidfTransformer**를 사용해 **TF-IDF 벡터**를 생성하고 희소행렬(COO format)로 저장 
단어 인덱스(train_vocab.tsv), 라벨(train_labels.txt)도 별도로 저장.
- Bigram 실습 ngram_range=(2,2) 설정으로 **음절 bigram 벡터** 생성해서 형태소 분석과 동일한 과정 수행
- scikit-learn의 SVM과 Logistic Regression 이용하여 분류 및 평가


### 실습 결과

| 모델                       | 형태소 분석 (Accuracy) | 음절 ngram (bigram) (Accuracy) |
|-----------------------------|------------------------|--------------------------------|
| SVM (LinearSVC)             | 0.8613 (86.1%)         | 0.8632 (86.3%)                 |
| Logistic Regression         | 0.8599 (85.9%)         | 0.8624 (86.2%)                 |
| Decision Tree               | 0.7581 (75.8%)         | 0.7674 (76.7%)                 |
| Multinomial Naive Bayes     | 0.8581 (85.8%)         | 0.8528 (85.2%)                 |
| Random Forest               | 0.8365 (83.6%)         | 0.8406 (84.0%)                 |


>전반적으로 SVM과 Logistic Regression이 가장 높은 정확도를 보임
>형태소 분석과 Bigram 간 정확도 차이는 크지 않지만, 형태소 분석이 약간 더 안정적인 성능을 보임
>불필요한 조사·어미 제거로 데이터 노이즈가 줄어 일반화 성능이 향상된 것으로 추정됨

<table align="right">
  <tr>
    <td><b>2025년도 2학기 수강</b></td>
    <td><b>강승식 교수님</b></td>
  </tr>
</table>
