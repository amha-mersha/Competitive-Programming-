class Solution(object):
    def subdomainVisits(self, cpdomains):
        resultDic = {}
        for i,doms in enumerate(cpdomains):
            count,domain = doms.split()
            resultDic[domain]= resultDic.setdefault(domain,0) + int(count)
            temp = domain.split(".")
            for j in range(1,len(temp)):
                resultDic[".".join(temp[j:])] = resultDic.setdefault(".".join(temp[j:]),0) + int(count)
        result = []
        m = list(map(str,resultDic.values()))
        n = list(resultDic.keys())
        for i in range(len(resultDic)):
            result.append(m[i]+ ' ' + n[i] )
        return result
