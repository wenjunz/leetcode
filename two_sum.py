class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        adict = {};
        for i,n in enumerate(num):
            if n in adict:
                adict[n].append(i+1);
            else:
                adict[n] = [i+1];
        
        for k in adict.keys():
            if k==target-k:
                if len(adict[k])>1: return(adict[k][0],adict[k][1]);
            elif target-k in adict.keys():
                return (sorted([adict[k][0],adict[target-k][0]]))
