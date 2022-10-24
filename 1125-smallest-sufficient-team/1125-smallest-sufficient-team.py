class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        
        idxs = {skill: i  for i, skill in enumerate(req_skills)}
        
        dp = {0:[]}
        
        for i, p in enumerate(people):
            currSkills = 0 
            for s in p:
                currSkills |= (1 << idxs[s])
            for  preSkills , team in list(dp.items()):
                
                updated = preSkills | currSkills
                if updated not in dp or len(dp[updated]) > len(team) + 1:
                    dp[updated] = team + [i]
        return dp[(1 << len(req_skills)) -1]
        