class Solution(object):
    def isAlienSorted(self, words, order):
        def isAlienSortedHelper(s1,s2,order_dict):
            for i in range(len(s1)):
                if order_dict[s1[i]]< order_dict[s2[i]]:
                    return True
                elif order_dict[s1[i]] == order_dict[s2[i]]:
                    if i!=len(s1)-1 and i==len(s2)-1:
                        return False
                    continue
                else:
                    return False
        if len(words) == 1:
            return True
        order_dict ={}
        for idx,char in enumerate(order):
            order_dict[char] = idx
        for i in range(len(words)-1):
            if isAlienSortedHelper(words[i],words[i+1],order_dict) == False:
                return False
        return True