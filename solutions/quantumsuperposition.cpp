/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca
 Feel free to send any questions about this problem to the email above
 or ask in the CPC discord. (discord.gg/MEXwfze)
 ---------------------------------------------------------------------*/
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int n1, n2, m1, m2;
unordered_map<int, unordered_set<int>> u1, u2, memo1, memo2;


unordered_set<int> solve1(int node) {
  if (memo1.find(node) != memo1.end())
    return memo1[node];

  if (node == n1)
    return unordered_set<int>({0});

  unordered_set<int> aset;
  for (auto iter = u1[node].begin(); iter != u1[node].end(); ++iter) {
    unordered_set<int> bset = solve1(*iter);
    for (auto iter2 = bset.begin(); iter2 != bset.end(); ++iter2)
      aset.insert(*iter2 + 1);
  }
  memo1[node].insert(aset.begin(), aset.end());
  return aset;
}

unordered_set<int> solve2(int node) {
  if (memo2.find(node) != memo2.end())
    return memo2[node];

  if (node == n2)
    return unordered_set<int>({0});

  unordered_set<int> aset;
  for (auto iter = u2[node].begin(); iter != u2[node].end(); ++iter) {
    unordered_set<int> bset = solve2(*iter);
    for (auto iter2 = bset.begin(); iter2 != bset.end(); ++iter2)
      aset.insert(*iter2 + 1);
  }
  memo2[node].insert(aset.begin(), aset.end());
  return aset;
}


int main() {
  int i, u, v, Q, q, found;
  scanf("%d %d %d %d", &n1, &n2, &m1, &m2);

  for (i = 0; i < m1; i++) {
    scanf("%d %d", &u, &v);
    u1[u].insert(v);
  }

  for (i = 0; i< m2; i++) {
    scanf("%d %d", &u, &v);
    u2[u].insert(v);
  }

  unordered_set<int> paths1 = solve1(1);
  unordered_set<int> paths2 = solve2(1);
  
  scanf("%d", &Q);
  for (i = 0; i < Q; i++) {
    scanf("%d", &q);
    found = 0;
    for (auto iter = paths1.begin(); iter != paths1.end(); ++iter) {
      if (paths2.find(q - *iter) != paths2.end()) {
	found = 1;
	printf("Yes\n");
	break;
      }
    }
    if (found == 0)
      printf("No\n");
      
  }  
  return 0;
}
