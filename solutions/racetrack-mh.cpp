/*
 Author: Modan Han
 This solution was written by the one of the ACPC judges.
 Feel free to discuss it in the CPC discord. (discord.gg/MEXwfze)
 ---------------------------------------------------------------------*/
#include <bits/stdc++.h>
using namespace std;

const double EP = 1e-9; // do not use for angles
typedef complex<double> PX;
const PX BAD(1e100,1e100);

double cp(PX a, PX b) {return (conj(a)*b).imag();}
double dp(PX a, PX b) {return (conj(a)*b).real();}
bool ss(PX a, PX b) {return fabs(cp(a,b)) < EP;}
struct arc{
	PX p,b,e;double r;
};

typedef pair<PX,PX> ls;
typedef vector<ls> vls;

int n,q;
vls lss;
vector<arc> arcs;

// Can be used to check if a point is on a line (0)
int ccw(PX a, PX b, PX c) {
double r = cp(b-a, c-a);
if (fabs(r) < EP) return 0;
return r > 0 ? 1 : -1;
}

PX lineIntersect(PX p1, PX v1, PX p2, PX v2) {
// If exact same line, pick random point (p1)
if (ss(v1, v2)) return ss(v1, p2-p1) ? p1 : BAD;
return p1 + (cp(p2-p1,v2)/cp(v1,v2))*v1;
}

double p2ls(PX p, ls l){
	double l2=norm(l.second-l.first);
	if(l2<EP)return abs(p-l.first);
	double t=max(0.0,min(1.0,dp(p-l.first,l.second-l.first)/l2));
	PX pr=l.first+t*(l.second-l.first);
	return abs(p-pr);
}

double p2a(PX p, arc a){
	if(ccw(a.p,a.b,a.e)==ccw(a.p,a.b,p) && ccw(a.p,a.b,a.e)==ccw(a.p,p,a.e)){
		return abs(abs(p-a.p)-abs(a.b-a.p));
	}
	return min(abs(p-a.b),abs(p-a.e));
}

int main(){
	cin>>n>>q;
	vector<PX> polygon;
	polygon.assign(n,PX(0,0));
	vector<double> smooth;
	smooth.assign(n,0);
	for(int i=0;i<n;i++){
		double x,y;cin>>x>>y;
		polygon[i]=PX(x,y);
	}
	lss.resize(n);
	for(int i=0;i<n;i++){
		lss[i].first=polygon[i];
		lss[i].second=polygon[(i+1)%n];
	}
	for(int i=0;i<n;i++)cin>>smooth[i];
	for(int i=0;i<n;i++){
		if(smooth[i]<EP)continue;
		auto pp=polygon[(i+n-1)%n];
		auto pc=polygon[i];
		auto pn=polygon[(i+1)%n];
		double theta=acos(dp(pn-pc,pp-pc)/(abs(pn-pc)*abs(pp-pc)));
		double r=tan(theta/2)*smooth[i];
		auto d=pp-pc;
		d/=abs(d);
		auto pm=pc+d*smooth[i];
		auto rd=PX(-d.imag(),d.real());
		if(ccw(pp,pc,pn)>0)rd*=-1;
		auto rp=pm+rd*r;
		arc a;a.p=rp;a.r=r;a.b=pm;
		{
			auto d1=pn-pc;
			d1/=abs(d1);
			auto pm1=pc+d1*smooth[i];
			a.e=pm1;
		}
		arcs.push_back(a);
	}
//	for(auto a:arcs)cout<<a.p<<'\t'<<a.r<<'\t'<<a.b<<'\t'<<a.e<<endl;
//	for(auto a:lss)cout<<a.first<<'\t'<<a.second<<endl;
	for(int i=0;i<n;i++){
		double l0=smooth[i], l1=smooth[(i+1)%n];
		auto d=lss[i].second-lss[i].first;
		d/=abs(d);
		lss[i].first+=d*l0;
		lss[i].second-=d*l1;
	}
//	for(auto a:lss)cout<<a.first<<'\t'<<a.second<<endl;
	for(int i=0;i<q;i++){
		double x,y;cin>>x>>y;
		PX p(x,y);
		double ans=1e100;
		for(auto a:lss)ans=min(ans,p2ls(p,a));
		for(auto a:arcs)ans=min(ans,p2a(p,a));
		printf("%.6f\n",ans);
	}
	
}
