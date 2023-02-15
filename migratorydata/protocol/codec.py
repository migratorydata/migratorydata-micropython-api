_B=None
_A='utf-8'
import random as r
from .push_protocol import *
from ..core.subject import FLh
from ..migratorydata_client import QoS
from ..core.io import NPQ as B
class AKi:
	def __init__(self):self._encoding=sIx.fUk
	def tWU(self,tzo,token,session_type,user_agent,version):
		tzo.extend(bytes(chr(rCj.wKa(Eid.MSM)),_A))
		if token is not _B:self.cUl(tzo,rCj.KRN(LuJ.meQ),rCj.aGX(token))
		if session_type is not _B:self.cUl(tzo,rCj.KRN(LuJ.kQl),rCj.rSl(session_type))
		if user_agent is not _B:self.cUl(tzo,rCj.KRN(LuJ.FLQ),rCj.aGX(user_agent))
		self.cUl(tzo,rCj.KRN(LuJ.lEu),rCj.rSl(version));self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def bXi(self,tzo,sRv,session_id):
		tzo.extend(bytes(chr(rCj.wKa(Eid.eEO)),_A));self.cUl(tzo,rCj.KRN(LuJ.Piu),rCj.aGX(sRv.get_subject()))
		if session_id is not _B and session_id>=0:self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id))
		LWu=sRv.NFG()
		if LWu==FLh.MjB:self.cUl(tzo,rCj.KRN(LuJ.mAm),rCj.rSl(sRv.uZy()))
		elif LWu==FLh.RaK:self.cUl(tzo,rCj.KRN(LuJ.vbm),rCj.rSl(sRv.pEN()));self.cUl(tzo,rCj.KRN(LuJ.NEo),rCj.rSl(sRv.get_seq()+1))
		self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def diW(self,tzo,session_id,sRv):
		tzo.extend(bytes(chr(rCj.wKa(Eid.Nab)),_A));self.cUl(tzo,rCj.KRN(LuJ.Piu),rCj.aGX(sRv.get_subject()))
		if session_id>=0:self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id))
		self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def Ouz(self,tzo,message,session_id):
		tzo.extend(bytes(chr(rCj.wKa(Eid.mav)),_A));self.cUl(tzo,rCj.KRN(LuJ.Piu),rCj.aGX(message.get_subject()));self.cUl(tzo,rCj.KRN(LuJ.rLN),rCj.UJO(message.get_content()))
		if message.get_reply_to_subject()is not _B:self.cUl(tzo,rCj.KRN(LuJ.ijN),rCj.aGX(message.get_reply_to_subject()))
		if message.get_closure()is not _B and len(message.get_content())>0:self.cUl(tzo,rCj.KRN(LuJ.vDS),rCj.aGX(message.get_closure()))
		if session_id>=0:self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id))
		if message.is_retained()is True:self.cUl(tzo,rCj.KRN(LuJ.sBx),rCj.rSl(1))
		else:self.cUl(tzo,rCj.KRN(LuJ.sBx),rCj.rSl(0))
		jsb=message.get_qos()
		if jsb==QoS.GUARANTEED:self.cUl(tzo,rCj.KRN(LuJ.qHM),rCj.rSl(QoS.GUARANTEED))
		elif jsb==QoS.STANDARD:self.cUl(tzo,rCj.KRN(LuJ.qHM),rCj.rSl(QoS.STANDARD))
		if message.is_compressed():self.cUl(tzo,rCj.KRN(LuJ.vGY),rCj.rSl(1))
		self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def UgJ(self,tzo,session_id):
		tzo.extend(bytes(chr(rCj.wKa(Eid.RXp)),_A))
		if session_id>=0:self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id))
		self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def LMB(self,tzo,token,session_id):
		tzo.extend(bytes(chr(rCj.wKa(Eid.sAy)),_A))
		if session_id>=0:self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id))
		self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding))
		if token is not _B:self.cUl(tzo,rCj.KRN(LuJ.meQ),rCj.aGX(token))
		tzo.extend(bytes(chr(rCj.czT),_A))
	def Ftt(self,tzo,sRv,OmT,epoch,session_id):tzo.extend(bytes(chr(rCj.wKa(Eid.PUBLISH_ACK)),_A));self.cUl(tzo,rCj.KRN(LuJ.Piu),rCj.aGX(sRv));self.cUl(tzo,rCj.KRN(LuJ.NEo),rCj.rSl(OmT));self.cUl(tzo,rCj.KRN(LuJ.vbm),rCj.rSl(epoch));self.cUl(tzo,rCj.KRN(LuJ.kFg),rCj.rSl(session_id));self.cUl(tzo,rCj.KRN(LuJ.ukk),rCj.rSl(self._encoding));tzo.extend(bytes(chr(rCj.czT),_A))
	def cUl(self,tzo,raH,bDQ):tzo.append(raH);tzo.extend(bDQ);tzo.append(rCj.CUW)
class AVP:
	def __init__(self,_start,_end):self._start=_start;self._end=_end
	def DUb(self):return self._start
	def zsL(self):return self._end
class JqV:
	@staticmethod
	def Ksz(tzo,xgh):
		skU=AVP(-1,-1)
		if xgh==len(tzo.Htg):return skU
		PKd=xgh;pit=2;lWP=0;iVJ=0;Yza=len(tzo.Htg)-PKd
		if Yza<pit:return skU
		b=tzo.Htg[PKd];seZ=b>>7&1;Nxk=b&64;uhG=b&32;Euh=b&16
		if seZ!=1 or Nxk!=0 or uhG!=0 or Euh!=0:return skU
		PKd+=1;b=tzo.Htg[PKd];ccz=b&127
		if ccz<126:iVJ=0;lWP=ccz
		elif ccz==126:
			iVJ=2
			if Yza<pit+iVJ:return skU
			tss=bytearray()
			for sEb in range(PKd+1,PKd+1+iVJ):tss.extend(bytes([tzo.Htg[sEb]]))
			lWP=JqV.QjR(tss);PKd+=iVJ
		elif ccz==127:
			iVJ=8
			if Yza<pit+iVJ:return skU
			tss=bytearray()
			for sEb in range(PKd+1,PKd+1+iVJ):tss.extend(bytes([tzo.Htg[sEb]]))
			lWP=JqV.QjR(tss);PKd+=iVJ
		if Yza<pit+iVJ+lWP:return skU
		PKd+=1;return AVP(PKd,PKd+lWP)
	@staticmethod
	def QjR(bDQ):
		if len(bDQ)==2:return(bDQ[0]&255)<<8|bDQ[1]&255
		else:return(bDQ[4]&127)<<24|(bDQ[5]&255)<<16|(bDQ[6]&255)<<8|bDQ[7]&255
class tIS:
	dHy='GET /WebSocketConnection HTTP/1.1\r\n';GBR='GET /WebSocketConnection-Secure HTTP/1.1\r\n';PbS='Host: ';YxI='Origin: ';DdZ='Upgrade: websocket\r\n';QzD='Sec-WebSocket-Key: 23eds34dfvce4\r\n';kPL='Sec-WebSocket-Version: 13\r\n';pBq='Sec-WebSocket-Protocol: pushv1\r\n';cHl='Connection: Upgrade\r\n';WZt='\r\n';wEg=2;yZC=10;trO=128;QSu=128
	def ofp(self):tzo=B();PKd=tIS.yZC;tzo.extend(bytearray(10));PKd+=4;tzo.extend(bytes([r.randint(0,255),r.randint(0,255),r.randint(0,255),r.randint(0,255)]));tzo.xgh(PKd);tzo.body_start_mark=PKd;return tzo
	def fdj(self,tzo):
		seZ=tIS.QSu;seZ|=tIS.wEg;tzo.body_end_mark=len(tzo.Htg);ahn=tzo.body_end_mark-tzo.body_start_mark;iFw=self.Kja(ahn);WBL=self.REh(ahn,iFw);nAA=0;Zua=0
		if iFw==1:nAA=8;Zua=8;tzo.Htg[Zua]=seZ;tzo.Htg[Zua+1]=WBL[0]|tIS.trO
		elif iFw==2:
			nAA=6;Zua=6;tzo.Htg[Zua]=seZ;tzo.Htg[Zua+1]=126|tIS.trO;Zua+=2
			for sEb in range(0,2):tzo.Htg[Zua+sEb]=WBL[sEb]
		else:
			tzo.Htg[Zua]=seZ;tzo.Htg[Zua+1]=127|tIS.trO;Zua+=2
			for sEb in range(0,8):tzo.Htg[Zua+sEb]=WBL[sEb]
		oyq=bytearray();oyq.extend(bytes([tzo.Htg[tzo.body_start_mark-4]]));oyq.extend(bytes([tzo.Htg[tzo.body_start_mark-3]]));oyq.extend(bytes([tzo.Htg[tzo.body_start_mark-2]]));oyq.extend(bytes([tzo.Htg[tzo.body_start_mark-1]]));qny=0
		for sEb in range(tzo.body_start_mark,tzo.body_end_mark):
			b=tzo.Htg[sEb]^oyq[qny];tzo.Htg[sEb]=b
			if qny==3:qny=0
			else:qny+=1
		tzo.xgh(nAA)
	def ojs(self,host,encrypted):
		tzo=B()
		if encrypted is False:tzo.extend(bytes(tIS.dHy,_A))
		else:tzo.extend(bytes(tIS.GBR,_A))
		tzo.extend(bytes(tIS.YxI,_A));tzo.extend(bytes('http://'+str(host),_A));tzo.extend(bytes(tIS.WZt,_A));tzo.extend(bytes(tIS.PbS,_A));tzo.extend(bytes(str(host),_A));tzo.extend(bytes(tIS.WZt,_A));tzo.extend(bytes(tIS.DdZ,_A));tzo.extend(bytes(tIS.cHl,_A));tzo.extend(bytes(tIS.QzD,_A));tzo.extend(bytes(tIS.kPL,_A));tzo.extend(bytes(tIS.pBq,_A));tzo.extend(bytes(tIS.WZt,_A));return tzo
	def Kja(self,size):
		if size<=125:return 1
		elif size<=65535:return 2
		return 8
	def REh(self,value,iFw):
		WPJ=bytearray();mju=8*iFw-8
		for sEb in range(0,iFw):hZO=self.xnd(value,mju-8*sEb);IAn=hZO-256*int(hZO/256);WPJ.extend(bytes([IAn]))
		return WPJ
	def xnd(self,val,n):return val%4294967296>>n