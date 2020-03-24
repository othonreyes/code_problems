from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        class DomainCount:
            def __init__(self, values):
            #def __init__(self, values:string): # typing with strings
                self.count = int(values[:values.index(" ")])
                domains = values[values.index(" ") + 1:] # more practices splicing
                domains_list = domains.split('.')
                
                self.subdomain = None
                self.site = None
                self.top_level = None
                
                if len(domains_list) == 3:
                    self.subdomain = domains
                    self.site = domains_list[1] + "." + domains_list[2]
                    self.top_level = domains_list[2]
                else:
                    self.site = domains_list[0] + "." + domains_list[1] 
                    self.top_level = domains_list[1]
        
        domains = {} # more idiomatic way to initialize the values
        
        for i in range(len(cpdomains)):
            dc = DomainCount(cpdomains[i])
            
            if dc.subdomain:
               domains[dc.subdomain] = domains.get(dc.subdomain, 0) + dc.count # more idiomatic way to sum values
            domains[dc.top_level] = domains.get(dc.top_level, 0) + dc.count
            domains[dc.site] = domains.get(dc.site, 0) + dc.count
        
        results = []
        for (k, v) in domains.items():
            result.append(str(v) + " " + k)
        
        return result

    def subdomainVisits_2(self, cpdomains: List[str]) -> List[str]:
      class DomainCount:
          def __init__(self, values):
          #def __init__(self, values:string): # typing with strings
              self.count = int(values[:values.index(" ")])
              domains = values[values.index(" ") + 1:] # more practices splicing
              domains_list = domains.split('.')
              
              self.subdomain = None
              self.site = None
              self.top_level = None
              
              if len(domains_list) == 3:
                  self.subdomain = domains
                  self.site = domains_list[1] + "." + domains_list[2]
                  self.top_level = domains_list[2]
              else:
                  self.site = domains_list[0] + "." + domains_list[1] 
                  self.top_level = domains_list[1]
      
      # domains = {}
      # domains.setdefault(0) # doesn't help when trying to sum a value
      from collections import defaultdict
      domains = defaultdict(lambda : 0) # Pass a collable
      
      for i in range(len(cpdomains)):
          dc = DomainCount(cpdomains[i])
          
          if dc.subdomain:
              domains[dc.subdomain] += dc.count # more idiomatic way to sum values
          domains[dc.top_level] += dc.count
          domains[dc.site] += dc.count
      
      return [str(domains[k]) + " " + k  for k in domains.keys() ]



if __name__ == "__main__":
  s = Solution()
  print(s.subdomainVisits_2(["9001 discuss.leetcode.com"]))
