//실행 전 동일한 파일 경로에 필요한 텍스트파일들이 존재하는지 확인하세요!

#include <bits/stdc++.h>
using namespace std;

vector<string> load_list(const string& filename) {
    vector<string> items;
    ifstream fin(filename);
    if (!fin.is_open()) {
        cerr << "파일 열기 실패: " << filename << "\n";
        return items;
    }
    string line;
    while (getline(fin, line)) {
        // 끝 공백 제거
        while (!line.empty() && (line.back() == '\r' || line.back() == '\n'))
            line.pop_back();
        if (!line.empty()) items.push_back(line);
    }
    fin.close();
    // 긴 항목부터 매칭되게 정렬
    sort(items.begin(), items.end(), [](const string& a, const string& b) {
        return a.size() > b.size();
        });
    return items;
}

string remove_punc(const string& s) {
    static const string punc = "\n\r'\"-=/.,()!?:;";
    string out = s;
    for (char c : punc) {
        out.erase(remove(out.begin(), out.end(), c), out.end());
    }
    return out;
}

bool find_all_suffixes(const string& word, const vector<string>& suffixes, const string& tag) {
    bool found = false;
    for (const auto& suf : suffixes) {
        if (suf.size() >= word.size()) continue;
        if (word.size() >= suf.size() &&
            equal(suf.rbegin(), suf.rend(), word.rbegin())) { // ends_with
            string stem = word.substr(0, word.size() - suf.size());
            if (!stem.empty()) {
                cout << "\t" << stem << " + " << suf << "/" << tag << "\n";
                found = true;
            }
        }
    }
    return found;
}

void analyze_line(const string& line, const vector<string>& josa, const vector<string>& eomi) {
    string cleaned = remove_punc(line);
    istringstream iss(cleaned);
    string word;
    while (iss >> word) {
        cout << word << "\n";
        bool j_found = find_all_suffixes(word, josa, "조사");
        bool e_found = find_all_suffixes(word, eomi, "어미");
        if (!j_found && !e_found) {
            cout << "\t==> 조사/어미 분리되지 않음\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 실행 경로에 txt 파일이 있다고 가정
    vector<string> josa = load_list("josa96.txt");
    vector<string> eomi = load_list("eomi152.txt");

    ifstream fin("test.txt");
    if (!fin.is_open()) {
        cerr << "test.txt 파일을 열 수 없습니다.\n";
        return 1;
    }

    string line;
    while (getline(fin, line)) {
        if (line.find_first_not_of(" \t\r\n") == string::npos) continue; // 빈 줄 스킵
        analyze_line(line, josa, eomi);
    }
    fin.close();
    return 0;
}
