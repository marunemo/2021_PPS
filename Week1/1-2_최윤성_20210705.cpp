#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    
    for(string tree : skill_trees) {
        bool able = true;
        for(int i = skill.length(); i >= 0; i--) {
            int index = tree.find(skill[i]);
            if(index != string::npos && i > 0)
                if(tree.substr(0, index).find(skill[i - 1]) == string::npos)
                    able = false;
        }
        if(able) answer++;
    }
    
    return answer;
}