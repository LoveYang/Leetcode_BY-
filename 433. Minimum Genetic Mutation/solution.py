# -*- coding: utf-8 -*-

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        lenbank=len(bank)
        if start in bank:
            bank.remove(start)
        count=self.count_dis(start,end)
        if not lenbank or count>lenbank:
            print('No blank or needt to search..blank:%d, count:%d'%(lenbank,count))
            return -1
       
        bank=sorted(bank,key=lambda x :self.count_dis(x,end))
        print('start: ',start)
        print('end: ',end)
        print('blank: ',bank)

#        bank=probank
        if count==1 and end in bank:
            print('find final')
            return 1

        else:
            for x in bank:
                if self.count_dis(x,start)==1:
                    mid=[y for y in bank]
#                    mid=bank
                    mid.remove(x)
                    count_=self.minMutation(x,end,mid)
                    if count_ :
                        if count_>0:
                            return count_+1
                print('End for')
            return -1
                    
    def count_dis(self,start,end):
        count=0
        for x,y in zip(start,end):
            if x!=y:
                count=count+1
        return count
    
# start="AACCGGTT"
# end="AAACGGTA"
# bank=["AACCGGTA","AACCGCTA","AAACGGTA"]
ans=Solution()
start="AAAACCCC"
end="CCCCCCCC"
bank=["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
print(ans.minMutation( start, end, bank))
        