class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for(String tree : skill_trees) {
            boolean able = true;
            for(int i = skill.length() - 1; i >= 0; i--) {
                int index = tree.indexOf(skill.charAt(i));
                if(index != -1 && i > 0)
                    if(tree.substring(0, index).indexOf(skill.charAt(i - 1)) == -1)
                        able = false;
            }
            if(able) answer++;
        }
        
        return answer;
    }
}