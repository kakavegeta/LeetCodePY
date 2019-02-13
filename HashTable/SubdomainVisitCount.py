class Solution:
    def subdomainVisits(self, cpdomains):
        dic = {}
        for dom in cpdomains:
            count = int(dom.split(' ')[0])
            subdoms = dom.split(' ')[1].split('.')
            for i in range(len(subdoms)):
                item = ".".join(subdoms[i:])
                if item in dic:
                    dic[item] += count
                else:
                    dic[item] = count
        return ["{} {}".format(num, item) for item, num in dic.items()]

