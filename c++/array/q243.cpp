#include <vector>
int shortestDistance(vector<string>& words, string word1, string word2) {
    int pos1 = -1;
    int pos2 = -1;
    int diff = words.size();
    for(int i = 0; i < words.size(); i++){
        if(words[i]==word1)
            pos1 = i;
        else if(words[i]==word2)
            pos2 = i;
        if(pos1 != -1 && pos2 != -1 && abs(pos1-pos2) < diff)
            diff = abs(pos1-pos2);
    }

    return diff;
}
