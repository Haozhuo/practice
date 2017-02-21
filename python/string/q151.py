def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    return " ".join(s.strip().split()[::-1])


#O(n) and in-place
    void reverseWords(string &s) {
        if(s.size() == 0)
            return;
        int i = 0; int j = 0; int l = 0; int word = 0;
        int len = s.size();
        reverse_string(s,0,s.size());
        while(i < len){
            while(i < len && s[i] != ' ')
                i++;
            if(i==len)
                break;
            if(word){
                s[j] = ' ';
                j++;
            }

            l = j;

            while(i < len && s[i] != ' '){
                s[j] = s[i];
                i++; j++;
            }

            reverse_string(s,l,j);
            word++;
        }

        s.resize(j);
        return;
    }
private:
    void reverse_string(string &s,int start,int end){
        int i = start; int j = end - 1;
        while(i < j){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++; j--;
        }

        return;
    }
