class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = defaultdict(list)
        
        for i in range(len(emails)):
            temp = [] 
            plus = False
            squid = False
            for j in emails[i]:
                if j == "+":
                    plus = True
                    
                if j == "@":
                    squid = True 
                    
                if j != "." and squid == False and plus == False:
                    temp.append(j)
                    
                if squid == True:
                    temp.append(j)
            email_list["".join(temp)] = True
        
        return len(email_list)
    
    # O(N) time
    # O(N) space
