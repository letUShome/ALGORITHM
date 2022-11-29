#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

bool compare(pair<string, int>& a, pair<string, int>& b){
    return a.second > b.second;
}

bool compare_songs(pair<int, int>& a, pair<int, int>& b){
    return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    // 장르 개수 저장
    map<string, int> cnt;
    
    // 장르 별 플레이 회수 저장
    map<string, map<int, int>> songs;
    
    for(int i = 0; i < genres.size(); i++){
        cnt[genres[i]] += plays[i]; // 속한 노래가 많이 재생됨
        songs[genres[i]][i] = plays[i];// 장르 내에서 많이 재생됨
        cout << genres[i] << " " << i << " " << songs[genres[i]][i] << "\n";
    }
    
    
    // cout << songs["classic"].begin()->first;
    
    for(auto iter = cnt.begin(); iter != cnt.end(); iter++){
        string name = iter->first;
        int idx = 0;
        for(auto iter2 = songs[name].begin(); iter2 != songs[name].end(); iter2++){
            if(idx != 2){
                answer.push_back(iter2->first);
                idx++;
            }
        }
    }
    
    return answer;
}
