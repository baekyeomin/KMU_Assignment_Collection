#----------------------
# 정보검색과 텍스트마이닝 :: [과제 B1] 한국어 형태소 분석기 개발
# 인공지능학부 20243153 백여민
#----------------------
'''
josaEomi.py에서 !가 제거 되지 않아,
"훔쳤다!" 및 "적이다!" 등이 아래와 같이 분리되지 않는 문제 해결했습니다. 

훔쳤다
        훔쳤 + 다/조사
        훔쳤 + 다/어미
 적이다
        적 + 이다/조사
        적이 + 다/조사
        적이 + 다/어미       
        
또한, 조사 / 어미 분리가 되지 않는 경우,
==> 조사/어미 분리되지 않음 이라고 출력이 되도록 했습니다. 
'''

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent

def load_list(relpath: str):
    path = BASE / relpath
    items = []
    with open(path, 'r', encoding='cp949') as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            items.append(s)
    # 긴 항목부터 우선 매칭하도록 길이 기준 내림차순
    items.sort(key=len, reverse=True)
    return items

def remove_punc(s: str) -> str:
    # 최소한의 문장부호 제거(원 코드와 유사)
    punc = ['\n','\r','\'','"','-','=','/','.', '(', ')', ',', '!', '?', ':', ';']
    for ch in punc:
        s = s.replace(ch, '')
    return s

def find_all_suffixes(word: str, suffixes, tag: str):
    """
    word가 suffix로 끝나면 stem + suffix를 모두 찾아서 출력.
    return값은 발견 여부 (bool)
    """
    found = False
    for suf in suffixes:
        if len(suf) >= len(word):
            continue
        if word.endswith(suf):
            stem = word[:-len(suf)]
            if stem:  # stem이 비어있지 않을 때만
                print(f"\t{stem} + {suf}/{tag}")
                found = True
    return found

def analyze_line(line: str, josa, eomi):
    line = remove_punc(line)
    words = [w for w in line.split() if w]
    for w in words:
        print(w)
        # 조사 먼저 시도 → 실패 시 어미
        j_found = find_all_suffixes(w, josa, "조사")
        e_found = find_all_suffixes(w, eomi, "어미")
        if not (j_found or e_found):
            print("\t==> 조사/어미 분리되지 않음")

def main():
    josa = load_list("josa96.txt")
    eomi = load_list("eomi152.txt")
    test_path = BASE / "test.txt"

    with open(test_path, 'r', encoding='cp949') as f:
        for line in f:
            if len(line.strip()) < 1:
                continue
            analyze_line(line, josa, eomi)

if __name__ == "__main__":
    main()
