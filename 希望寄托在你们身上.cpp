#include <synchapi.h>
#include <utilapiset.h>
#include <cstdio>
#include <cstdlib>
#define p(a,b) Beep(a,b);
#define s(b) Sleep(b);
#define w(q) printf("%s\n",q);
#define ting 128
#define st s(ting);
using namespace std;

// _在前表示低音, 在后表示高音
// o表示升
const int _oC = 277, _oD = 311,_oE = 659, _oF = 370, _oG = 415, _oA = 466,_oB = 988;
const int _C = 262, _D = 294, _E = 330, _F = 349, _G = 392, _A = 440, _B = 494;
const int oC = 554, oD = 622, oF = 740, oG = 831, oA = 932,oB = 988;
const int C = 523, D = 578, E = 659, F = 698, G = 784, A = 880, B = 988;
const int C_ = 1047, D_ = 1175, E_ = 1319, F_ = 1397, G_ = 1568, A_ = 1760, B_ = 1976;
const int oC_ = 1109, oD_ = 1245, oF_ = 1480, oG_ = 1661, oA_ = 1865,oB_ = 1976;
const int C__ = C_*2-C, D__ = D_*2-D, E__ = E_*2-E, F__ = F_*2-F, G__ = G_*2-G, A__ = A_*2-A, B__ = B_*2-B;
const int oC__ = C__+oC_-C_, oD__ = D__+oD_-D_, oF__ = F__+oF_-F_, oG__ = G__+oG_-G_, oA__ = A__+oA_-A_, oB__ = B__+oB_-B_;

const int T = 400; //一拍的长度
const int Stop = 800; //一拍休止符的长度

int main(){
    s(500);
    
	p(E_,T*2);
	
	p(C_,T*3/2);
	p(C_,T/2);
	
	p(D_,T/2);
	p(E_,T/2);
	p(C_,T/2);
	p(A,T/2);

	p(G,T);
	p(0,T);

	p(C,T*3/2);
	p(A,T/2);
	
	p(E,T);
	p(A,T);
	
	p(G,T*4);
	
	
	p(C_,T*3/4);
	p(C_,T/4);
	p(C_,T/2);
	p(C_,T/2);

	p(D_,T);
	p(C_,T/2);
	p(A,T/2);
	
	p(G,T);
	p(A,T/2);
	p(C_,T/2);
	
	p(G,T);
	p(E,T/2);
	p(D,T/2);

	p(C,T*3/4);
	p(D,T/4);
	p(E,T/2);
	p(G,T/2);

	p(A,T);
	p(G,T/2);
	p(E,T/2);

	
	p(D,T);
	p(E,T);

	p(C,T);
	p(0,T);
	
	p(G,T*3/4);
	p(G,T/4);
	p(E_,T/2);
	p(E_,T/2);

	p(E_,T*2);
	
	p(E_,T*3/2);
	p(E_,T/2);
	p(D_,T/2);
	p(C_,T/2);
	
	p(D_,T*2);
	

	p(C_,T);
	p(C_,T);
	
	p(D_,T);
	p(C_,T/2);
	p(A,T/2);
	
	p(G,T*3/2);
	p(E,T/2);
	
	p(A,T);
	p(0,T);
	
	p(C,T);
	p(D,T);

	p(E,T);
	p(G,T);

	p(C_,T/2);
	p(C_,T/2);
	p(A,T/2);
	p(G,T/4);
	p(G,T/4);
	

	p(C_,T);
	p(D_,T);

	p(E_,T*2);
	
	p(D_,T);
	p(0,T);
	
	p(E_,T/2);
	p(D_,T);
	p(C_,T/2);
	
	p(A,T);
	p(G,T);

	p(A,T);
	p(D_,T);
	
	p(C_,T*4);
	
	
    return 0;
}