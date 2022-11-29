#include <unordered_map>
#include <vector>

using namespace std;

bool cmp(pair<string, int>& a, pair<string, int>& b)
{
    return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;

    unordered_map<string, int> genre_count;

    for(int i=0; i<genres.size(); i++) {
        if(genre_count.find(genres[i]) != genre_count.end()) {
            genre_count[genres[i]] += plays[i];
        }
        else {
            genre_count.insert(make_pair(genres[i], plays[i]));
        }
    }

    vector<pair<string, int>> vec(genre_count.begin(), genre_count.end());
    sort(vec.begin(), vec.end(), cmp);



    return answer;
}

//가장 많이 재생된 노래 2개씩 모으기
//재생된수sum이 젤 큰 장르부터
//장르안에서는 재생된 수가 많은순으로
//재생된 수가 같으면 고유번호 낮은순으로

