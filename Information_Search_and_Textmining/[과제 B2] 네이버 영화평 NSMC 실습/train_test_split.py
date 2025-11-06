import csv

input_file = "NSMC_282K(ratings200K+kmuNP82K).txt"
train_file = "train.txt"
test_file = "test.txt"


with open(input_file, 'r', encoding='utf-8') as f_in, \
     open(train_file, 'w', encoding='utf-8') as f_train, \
     open(test_file, 'w', encoding='utf-8') as f_test:

    reader = csv.reader(f_in)
    next(reader)  # 첫 줄 id,review,label있는 부분은 건너뛰기
    
    for i, row in enumerate(reader):
        if len(row) >= 3:
            review = row[1].strip()
            label = row[2].strip()
            
            if label == "0" : label = "-1" # negative label을 0에서 -1로 바꿔줬습니다. 
            
            line = f"{review},{label}\n"
            # 매 10번째 리뷰는 test로, 나머지는 train으로 저장합니다.
            if i % 10 == 0:
                f_test.write(line)
            else:
                f_train.write(line)


#데이터가 9:1로 잘 나뉘어졌는지 확인을 위해 다음을 출력했습니다. 
print(len(open("NSMC_282K(ratings200K+kmuNP82K).txt", 'r', encoding='utf-8').readlines()))
print(len(open("train.txt", 'r', encoding='utf-8').readlines()))
print(len(open("test.txt", 'r', encoding='utf-8').readlines()) ) 
