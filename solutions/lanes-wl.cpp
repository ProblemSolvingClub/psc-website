/*
 Author: Wenli Looi
 This solution was written by the one of the ACPC judges.
 Feel free to discuss it in the CPC discord. (discord.gg/MEXwfze)
 ---------------------------------------------------------------------*/
#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a),end(a)
typedef pair<int,int> PT;
typedef pair<int,PT> IPT;
typedef vector<PT> VPT;
typedef vector<VPT> VVPT;

int N, M, R;
PT mycar;
VVPT cars;

struct Edge {
	int n, i, d;
};

struct Gap {
	int s, f, maxd;
	vector<Edge> adj;
};
vector<vector<Gap>> gaps;

int startN, startI, maxAns;
void addGap(int n, int s, int f) {
	if (s < f) {
		gaps[n].push_back(Gap{s, f, 0, vector<Edge>()});
		if (n == 0 && s <= mycar.first && mycar.second <= f) {
			startN = n;
			startI = SZ(gaps[n])-1;
			maxAns = min(mycar.first-s, f-mycar.second);
			//printf("Got start %d %d\n", startN, startI);
		}
	}
}

int main() {
	scanf("%d%d%d", &N, &M, &R);
	cars.resize(N);
	FOR(m,0,M) {
		int lane, length, dist;
		scanf("%d%d%d", &lane, &length, &dist);
		PT car(dist, dist+length);
		if (m == 0) mycar = car; else cars[lane].push_back(car);
	}
	gaps.resize(N);
	FOR(n,0,N) {
		sort(ALL(cars[n]));
		int ls = 0;
		for (auto const& car : cars[n]) {
			addGap(n, ls, car.first);
			ls = car.second;
		}
		addGap(n, ls, R);
	}
	FOR(n,0,N-1) {
		FOR(i,0,gaps[n].size())
		FOR(j,0,gaps[n+1].size()) {
			Gap& gap = gaps[n][i];
			Gap& gap2 = gaps[n+1][j];
			int sz = min(gap.f, gap2.f) - max(gap.s, gap2.s);
			if (sz >= mycar.second-mycar.first) {
				//printf("Got edge (%d %d) <-> (%d %d)\n", n, i, n+1, j);
				gap.adj.push_back(Edge{n+1, j, sz});
				gap2.adj.push_back(Edge{n, i, sz});
			}
		}
	}
	priority_queue<IPT> pq;
	pq.emplace(INT_MAX, PT(startN, startI));
	gaps[startN][startI].maxd = INT_MAX;
	int ansd = 0;
	while (!pq.empty()) {
		IPT ipt = pq.top();
		pq.pop();
		//cout << "Popped " << ipt << endl;
		int n = ipt.second.first, i = ipt.second.second, d = ipt.first;
		if (gaps[n][i].maxd != d) continue;
		if (n == N-1) ansd = max(ansd, d);
		for (Edge const& e : gaps[n][i].adj) {
			//printf("Got edge %d %d %d\n", e.n, e.i, e.d);
			int newd = min(d, e.d);
			if (newd > gaps[e.n][e.i].maxd) {
				gaps[e.n][e.i].maxd = newd;
				pq.emplace(newd, PT(e.n, e.i));
			}
		}
	}
	if (ansd > 0) {
		printf("%.10f\n", fmin(double(maxAns), 0.5*double(ansd - (mycar.second-mycar.first))));
	} else {
		puts("Impossible");
	}
}
