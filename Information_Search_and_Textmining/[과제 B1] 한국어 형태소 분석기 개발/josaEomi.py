#이 소스파일은 '정근시'님이 작성한 것을 수정한 것입니다.
#국민대학교 소프트웨어학부 강승식 2020/12/12
#<추가작업> 조사/어미가 분리되지 않은 어절에 대해 "\t==> 조사/어미 분리되지 않음"이라고 출력되도록 수정!
import re

# 조사 또는 어미 파일을 읽어와서 dlist로 return
def load_josaEomi(filename):
	dlist = []
	f = open(filename, 'r')
	while True:
		line = f.readline()
		if not line:
			break
		dlist.append(line.rstrip())
	f.close()
	return dlist

#한글 어절에서 마침표, 콤마, 따옴표, 괄호 등 문장 부호를 제거
def removePunc(line):
	#한글 어절에서 마침표, 콤마, 따옴표, 괄호 등 문장 부호를 제거를 위한 List
	puncList = ['\n','\r\n','\'', '\"', '-', '-','=','/', '.', '(', ')']
	for _rm in puncList:
		if _rm in line:
			line = line.replace(_rm, '')
	return line

def sepJosaEomi(word, jeList, josaEomiTag):
	for _j in jeList:	#check Josa/Eomi
		pattern = ".+" + _j + "$"
		p = re.compile(pattern)
		m = p.match(word.rstrip())
		if m != None: #separate Josa/Eomi
			sep = word.split(_j)
			print('\t' + sep[0] + " + " + _j + josaEomiTag)

josaList = load_josaEomi("./josa96.txt")
print("Josa list =", josaList)

eomiList = load_josaEomi("./eomi152.txt")
print("Eomi list =", eomiList)

f = open("./test.txt", 'r')
while True:
	line = f.readline()
	if not line:
		break
	if len(line) < 2:
		continue

	line = removePunc(line)	#문장 부호를 제거
	wordList = line.split(' ')	#sentence --> word-list

	for _w in wordList:
		print(_w)
		sepJosaEomi(_w, josaList, "/조사")	# separate Josa
		sepJosaEomi(_w, eomiList, "/어미")	# separate Eomi
f.close()