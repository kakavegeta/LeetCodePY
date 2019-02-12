class Solution:
    def subdomainVisits(self, cpdomains):
        dic = {}
        for dom in cpdomains:
            count = int(dom.split(' ')[0])
            subdoms = dom.split(' ')[1]
            for i in range(len(subdoms)):
                

