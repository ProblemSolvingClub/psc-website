/*
 Author: Wenli Looi
 This solution was written by the one of the ACPC judges.
 Feel free to discuss it in the CPC discord. (discord.gg/MEXwfze)
 ---------------------------------------------------------------------*/
#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define ALL(a) begin(a),end(a)
typedef vector<int> VI;

int A[100000];
VI sts[300000];

void build(int n, int a, int b) {
	auto& s = sts[n];
	if (a == b) {
		s.push_back(A[a]);
		return;
	}
	int m = (a+b)/2;
	build(n*2+1, a, m);
	build(n*2+2, m+1, b);
	s = sts[n*2+1];
	s.insert(s.end(), ALL(sts[n*2+2]));
	sort(ALL(s));
	s.erase(unique(ALL(s)), s.end());
}

int I;
VI QS;

bool check(int n) {
	for (int a : sts[n]) {
		if (!binary_search(ALL(QS), a)) return false;
	}
	return true;
}

int sv(int n, int a, int b) {
	if (check(n)) return b;
	if (a == b) return a-1;
	int m = (a+b)/2;
	if (I <= m) {
		int res = sv(2*n+1, a, m);
		if (res != m) return res;
	}
	return sv(2*n+2, m+1, b);
}

int main() {
	int N, Q;
	scanf("%d", &N);
	FOR(n,0,N) scanf("%d", A+n);
	build(0, 0, N-1);
	scanf("%d", &Q);
	FOR(q,0,Q) {
		int M;
		scanf("%d%d", &I, &M);
		--I;
		QS.clear();
		FOR(m,0,M) {
			int x;
			scanf("%d", &x);
			QS.push_back(x);
		}
		sort(ALL(QS));
		printf("%d\n", sv(0, 0, N-1) - I + 1);
	}
}
