package othon.org.leetcode.medium.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

/**
 * Link: https://leetcode.com/problems/accounts-merge
 * <p>
 * TODO:
 */

@Slf4j
public class AccountsMerge {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = "";
    }

    static class Solution {
        /**
         * 25 / 49 test cases passed. https://leetcode.com/submissions/detail/331616899/?from=/explore/interview/card/facebook/52/trees-and-graphs/3027/
         * @param accounts
         * @return
         */
        public List<List<String>> accountsMerge(List<List<String>> accounts) {
            Map<String, List<Set<String>>> map = new HashMap<>();
            for (List<String> account: accounts) {
                if (!map.containsKey(account.get(0))) {
                    // add it
                    Set<String> accountSet = new TreeSet();
                    accountSet.addAll(account.subList(1, account.size()));
                    List<Set<String>> accountList = new ArrayList<>();
                    accountList.add(accountSet);
                    map.put(account.get(0), accountList);
                } else {
                    List<Set<String>> accountList = map.get(account.get(0));
                    boolean found = false;
                    for (int x = 0; x < accountList.size() && !found; x++) {
                        Set<String> accountSet = accountList.get(0);
                        for (int i = 1; i<account.size() && !found;i++) {
                            if (accountSet.contains(account.get(i))) {
                                // add it to the set and leave.
                                accountSet.addAll(account.subList(1, account.size()));
                                found = true;
                                break;
                            }
                        }
                    }
                    if (!found) {
                        Set<String> accountSet = new TreeSet();
                        accountSet.addAll(account.subList(1, account.size()));
                        accountList.add(accountSet);
                    }
                }
            }
            List<List<String>> results = new ArrayList<>();
            for (Map.Entry<String, List<Set<String>>> entry:  map.entrySet()) {
                String name = entry.getKey();
                for (Set<String> emails: entry.getValue()) {
                    List<String> account = new ArrayList<>(emails.size() + 1);
                    account.add(name);
                    account.addAll(emails);
                    results.add(account);
                }
            }
            return results;
        }
    }
}
