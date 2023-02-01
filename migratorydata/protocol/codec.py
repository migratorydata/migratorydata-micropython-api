_B=None
_A='utf-8'
import random as r
from .push_protocol import *
from ..core.subject import CKs
from ..migratorydata_client import QoS
from ..core.io import lBF as B
class Qlb:
	def __init__(self):self._encoding=XAE.vKL
	def lyy(self,lCc,token,session_type,user_agent,version):
		lCc.extend(bytes(chr(VWl.kNt(yZW.wFt)),_A))
		if token is not _B:self.ffh(lCc,VWl.gCJ(ssB.eAm),VWl.mSp(token))
		if session_type is not _B:self.ffh(lCc,VWl.gCJ(ssB.cxQ),VWl.auC(session_type))
		if user_agent is not _B:self.ffh(lCc,VWl.gCJ(ssB.Vxz),VWl.mSp(user_agent))
		self.ffh(lCc,VWl.gCJ(ssB.DoJ),VWl.auC(version));self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def ijw(self,lCc,Owg,session_id):
		lCc.extend(bytes(chr(VWl.kNt(yZW.aoD)),_A));self.ffh(lCc,VWl.gCJ(ssB.inO),VWl.mSp(Owg.get_subject()))
		if session_id is not _B and session_id>=0:self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id))
		skb=Owg.DKe()
		if skb==CKs.GiL:self.ffh(lCc,VWl.gCJ(ssB.fmO),VWl.auC(Owg.FlP()))
		elif skb==CKs.aEp:self.ffh(lCc,VWl.gCJ(ssB.mmS),VWl.auC(Owg.GjX()));self.ffh(lCc,VWl.gCJ(ssB.Xdm),VWl.auC(Owg.get_seq()+1))
		self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def UGm(self,lCc,session_id,Owg):
		lCc.extend(bytes(chr(VWl.kNt(yZW.Apn)),_A));self.ffh(lCc,VWl.gCJ(ssB.inO),VWl.mSp(Owg.get_subject()))
		if session_id>=0:self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id))
		self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def HqW(self,lCc,message,session_id):
		lCc.extend(bytes(chr(VWl.kNt(yZW.beJ)),_A));self.ffh(lCc,VWl.gCJ(ssB.inO),VWl.mSp(message.get_subject()));self.ffh(lCc,VWl.gCJ(ssB.OMZ),VWl.GXg(message.get_content()))
		if message.get_reply_to_subject()is not _B:self.ffh(lCc,VWl.gCJ(ssB.AKb),VWl.mSp(message.get_reply_to_subject()))
		if message.get_closure()is not _B and len(message.get_content())>0:self.ffh(lCc,VWl.gCJ(ssB.ulT),VWl.mSp(message.get_closure()))
		if session_id>=0:self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id))
		if message.is_retained()is True:self.ffh(lCc,VWl.gCJ(ssB.wsX),VWl.auC(1))
		else:self.ffh(lCc,VWl.gCJ(ssB.wsX),VWl.auC(0))
		PBz=message.get_qos()
		if PBz==QoS.GUARANTEED:self.ffh(lCc,VWl.gCJ(ssB.lWK),VWl.auC(QoS.GUARANTEED))
		elif PBz==QoS.STANDARD:self.ffh(lCc,VWl.gCJ(ssB.lWK),VWl.auC(QoS.STANDARD))
		if message.is_compressed():self.ffh(lCc,VWl.gCJ(ssB.PTc),VWl.auC(1))
		self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def TLD(self,lCc,session_id):
		lCc.extend(bytes(chr(VWl.kNt(yZW.EOC)),_A))
		if session_id>=0:self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id))
		self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def jZk(self,lCc,token,session_id):
		lCc.extend(bytes(chr(VWl.kNt(yZW.KZZ)),_A))
		if session_id>=0:self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id))
		self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding))
		if token is not _B:self.ffh(lCc,VWl.gCJ(ssB.eAm),VWl.mSp(token))
		lCc.extend(bytes(chr(VWl.ciG),_A))
	def waQ(self,lCc,Owg,VUx,epoch,session_id):lCc.extend(bytes(chr(VWl.kNt(yZW.PUBLISH_ACK)),_A));self.ffh(lCc,VWl.gCJ(ssB.inO),VWl.mSp(Owg));self.ffh(lCc,VWl.gCJ(ssB.Xdm),VWl.auC(VUx));self.ffh(lCc,VWl.gCJ(ssB.mmS),VWl.auC(epoch));self.ffh(lCc,VWl.gCJ(ssB.VdX),VWl.auC(session_id));self.ffh(lCc,VWl.gCJ(ssB.vli),VWl.auC(self._encoding));lCc.extend(bytes(chr(VWl.ciG),_A))
	def ffh(self,lCc,KRs,yvg):lCc.append(KRs);lCc.extend(yvg);lCc.append(VWl.FAa)
class Kxp:
	def __init__(self,_start,_end):self._start=_start;self._end=_end
	def DPA(self):return self._start
	def Cls(self):return self._end
class GyL:
	@staticmethod
	def jxp(lCc,DOX):
		VWs=Kxp(-1,-1)
		if DOX==len(lCc.zpO):return VWs
		KeQ=DOX;BcL=2;QzO=0;jMG=0;DcH=len(lCc.zpO)-KeQ
		if DcH<BcL:return VWs
		b=lCc.zpO[KeQ];qWg=b>>7&1;jjt=b&64;ZTP=b&32;CUn=b&16
		if qWg!=1 or jjt!=0 or ZTP!=0 or CUn!=0:return VWs
		KeQ+=1;b=lCc.zpO[KeQ];Hcu=b&127
		if Hcu<126:jMG=0;QzO=Hcu
		elif Hcu==126:
			jMG=2
			if DcH<BcL+jMG:return VWs
			smE=bytearray()
			for ocg in range(KeQ+1,KeQ+1+jMG):smE.extend(bytes([lCc.zpO[ocg]]))
			QzO=GyL.MMz(smE);KeQ+=jMG
		elif Hcu==127:
			jMG=8
			if DcH<BcL+jMG:return VWs
			smE=bytearray()
			for ocg in range(KeQ+1,KeQ+1+jMG):smE.extend(bytes([lCc.zpO[ocg]]))
			QzO=GyL.MMz(smE);KeQ+=jMG
		if DcH<BcL+jMG+QzO:return VWs
		KeQ+=1;return Kxp(KeQ,KeQ+QzO)
	@staticmethod
	def MMz(yvg):
		if len(yvg)==2:return(yvg[0]&255)<<8|yvg[1]&255
		else:return(yvg[4]&127)<<24|(yvg[5]&255)<<16|(yvg[6]&255)<<8|yvg[7]&255
class FYt:
	qUh='GET /WebSocketConnection HTTP/1.1\r\n';Dct='GET /WebSocketConnection-Secure HTTP/1.1\r\n';WaP='Host: ';hVg='Origin: ';zIs='Upgrade: websocket\r\n';vah='Sec-WebSocket-Key: 23eds34dfvce4\r\n';jJZ='Sec-WebSocket-Version: 13\r\n';Nqp='Sec-WebSocket-Protocol: pushv1\r\n';zQO='Connection: Upgrade\r\n';WHc='\r\n';IUG=2;Pyz=10;tMQ=128;vms=128
	def oMZ(self):lCc=B();KeQ=FYt.Pyz;lCc.extend(bytearray(10));KeQ+=4;lCc.extend(bytes([r.randint(0,255),r.randint(0,255),r.randint(0,255),r.randint(0,255)]));lCc.DOX(KeQ);lCc.body_start_mark=KeQ;return lCc
	def cEJ(self,lCc):
		qWg=FYt.vms;qWg|=FYt.IUG;lCc.body_end_mark=len(lCc.zpO);zJp=lCc.body_end_mark-lCc.body_start_mark;zdK=self.JtE(zJp);ZxM=self.OrI(zJp,zdK);NMz=0;cRA=0
		if zdK==1:NMz=8;cRA=8;lCc.zpO[cRA]=qWg;lCc.zpO[cRA+1]=ZxM[0]|FYt.tMQ
		elif zdK==2:
			NMz=6;cRA=6;lCc.zpO[cRA]=qWg;lCc.zpO[cRA+1]=126|FYt.tMQ;cRA+=2
			for ocg in range(0,2):lCc.zpO[cRA+ocg]=ZxM[ocg]
		else:
			lCc.zpO[cRA]=qWg;lCc.zpO[cRA+1]=127|FYt.tMQ;cRA+=2
			for ocg in range(0,8):lCc.zpO[cRA+ocg]=ZxM[ocg]
		aWG=bytearray();aWG.extend(bytes([lCc.zpO[lCc.body_start_mark-4]]));aWG.extend(bytes([lCc.zpO[lCc.body_start_mark-3]]));aWG.extend(bytes([lCc.zpO[lCc.body_start_mark-2]]));aWG.extend(bytes([lCc.zpO[lCc.body_start_mark-1]]));DeY=0
		for ocg in range(lCc.body_start_mark,lCc.body_end_mark):
			b=lCc.zpO[ocg]^aWG[DeY];lCc.zpO[ocg]=b
			if DeY==3:DeY=0
			else:DeY+=1
		lCc.DOX(NMz)
	def HDk(self,host,encrypted):
		lCc=B()
		if encrypted is False:lCc.extend(bytes(FYt.qUh,_A))
		else:lCc.extend(bytes(FYt.Dct,_A))
		lCc.extend(bytes(FYt.hVg,_A));lCc.extend(bytes('http://'+str(host),_A));lCc.extend(bytes(FYt.WHc,_A));lCc.extend(bytes(FYt.WaP,_A));lCc.extend(bytes(str(host),_A));lCc.extend(bytes(FYt.WHc,_A));lCc.extend(bytes(FYt.zIs,_A));lCc.extend(bytes(FYt.zQO,_A));lCc.extend(bytes(FYt.vah,_A));lCc.extend(bytes(FYt.jJZ,_A));lCc.extend(bytes(FYt.Nqp,_A));lCc.extend(bytes(FYt.WHc,_A));return lCc
	def JtE(self,size):
		if size<=125:return 1
		elif size<=65535:return 2
		return 8
	def OrI(self,value,zdK):
		IUO=bytearray();Buh=8*zdK-8
		for ocg in range(0,zdK):nER=self.QGY(value,Buh-8*ocg);auQ=nER-256*int(nER/256);IUO.extend(bytes([auQ]))
		return IUO
	def QGY(self,val,n):return val%4294967296>>n