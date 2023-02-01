_B=None
_A='utf-8'
import random as r
from migratorydata.protocol.push_protocol import *
from migratorydata.core.subject import sHL
from migratorydata.migratorydata_message import *
from migratorydata.core.io import eTG as B
class Mbl:
	def __init__(self):self._encoding=aMy.ChH
	def tPH(self,vrD,token,session_type,user_agent,version):
		vrD.extend(bytes(chr(msU.amE(QeI.HZk)),_A))
		if token is not _B:self.Dvd(vrD,msU.ytU(qUd.APr),msU.YCF(token))
		if session_type is not _B:self.Dvd(vrD,msU.ytU(qUd.Eje),msU.fha(session_type))
		if user_agent is not _B:self.Dvd(vrD,msU.ytU(qUd.TUm),msU.YCF(user_agent))
		self.Dvd(vrD,msU.ytU(qUd.nBj),msU.fha(version));self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def eno(self,vrD,qpH,session_id):
		vrD.extend(bytes(chr(msU.amE(QeI.tPQ)),_A));self.Dvd(vrD,msU.ytU(qUd.CMD),msU.YCF(qpH.get_subject()))
		if session_id is not _B and session_id>=0:self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id))
		qCT=qpH.qsb()
		if qCT==sHL.CUr:self.Dvd(vrD,msU.ytU(qUd.JXd),msU.fha(qpH.Ckb()))
		elif qCT==sHL.LPP:self.Dvd(vrD,msU.ytU(qUd.jMx),msU.fha(qpH.Ffz()));self.Dvd(vrD,msU.ytU(qUd.VDH),msU.fha(qpH.get_seq()+1))
		self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def GWM(self,vrD,session_id,qpH):
		vrD.extend(bytes(chr(msU.amE(QeI.piP)),_A));self.Dvd(vrD,msU.ytU(qUd.CMD),msU.YCF(qpH.get_subject()))
		if session_id>=0:self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id))
		self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def Elg(self,vrD,message,session_id):
		vrD.extend(bytes(chr(msU.amE(QeI.zLx)),_A));self.Dvd(vrD,msU.ytU(qUd.CMD),msU.YCF(message.get_subject()));self.Dvd(vrD,msU.ytU(qUd.OWx),msU.kTg(message.get_content()))
		if message.get_reply_to_subject()is not _B:self.Dvd(vrD,msU.ytU(qUd.BmE),msU.YCF(message.get_reply_to_subject()))
		if message.get_closure()is not _B and len(message.get_content())>0:self.Dvd(vrD,msU.ytU(qUd.uFN),msU.YCF(message.get_closure()))
		if session_id>=0:self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id))
		if message.is_retained()is True:self.Dvd(vrD,msU.ytU(qUd.yvW),msU.fha(1))
		else:self.Dvd(vrD,msU.ytU(qUd.yvW),msU.fha(0))
		YaS=message.get_qos()
		if YaS==QoS.GUARANTEED:self.Dvd(vrD,msU.ytU(qUd.QlV),msU.fha(QoS.GUARANTEED))
		elif YaS==QoS.STANDARD:self.Dvd(vrD,msU.ytU(qUd.QlV),msU.fha(QoS.STANDARD))
		if message.is_compressed():self.Dvd(vrD,msU.ytU(qUd.vPj),msU.fha(1))
		self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def GnG(self,vrD,session_id):
		vrD.extend(bytes(chr(msU.amE(QeI.yLo)),_A))
		if session_id>=0:self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id))
		self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def aoa(self,vrD,token,session_id):
		vrD.extend(bytes(chr(msU.amE(QeI.gCa)),_A))
		if session_id>=0:self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id))
		self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding))
		if token is not _B:self.Dvd(vrD,msU.ytU(qUd.APr),msU.YCF(token))
		vrD.extend(bytes(chr(msU.Ydq),_A))
	def FGC(self,vrD,qpH,HxA,epoch,session_id):vrD.extend(bytes(chr(msU.amE(QeI.PUBLISH_ACK)),_A));self.Dvd(vrD,msU.ytU(qUd.CMD),msU.YCF(qpH));self.Dvd(vrD,msU.ytU(qUd.VDH),msU.fha(HxA));self.Dvd(vrD,msU.ytU(qUd.jMx),msU.fha(epoch));self.Dvd(vrD,msU.ytU(qUd.yvl),msU.fha(session_id));self.Dvd(vrD,msU.ytU(qUd.UMK),msU.fha(self._encoding));vrD.extend(bytes(chr(msU.Ydq),_A))
	def Dvd(self,vrD,vDO,PrM):vrD.append(vDO);vrD.extend(PrM);vrD.append(msU.max)
class Crr:
	def __init__(self,_start,_end):self._start=_start;self._end=_end
	def IMd(self):return self._start
	def IGC(self):return self._end
class gnU:
	@staticmethod
	def zsy(vrD,vdE):
		JCj=Crr(-1,-1)
		if vdE==len(vrD.yKx):return JCj
		Fvx=vdE;kHl=2;MUJ=0;ZUA=0;VkN=len(vrD.yKx)-Fvx
		if VkN<kHl:return JCj
		b=vrD.yKx[Fvx];dXs=b>>7&1;yvu=b&64;xSf=b&32;pnc=b&16
		if dXs!=1 or yvu!=0 or xSf!=0 or pnc!=0:return JCj
		Fvx+=1;b=vrD.yKx[Fvx];fNt=b&127
		if fNt<126:ZUA=0;MUJ=fNt
		elif fNt==126:
			ZUA=2
			if VkN<kHl+ZUA:return JCj
			bbt=bytearray()
			for tdG in range(Fvx+1,Fvx+1+ZUA):bbt.extend(bytes([vrD.yKx[tdG]]))
			MUJ=gnU.peR(bbt);Fvx+=ZUA
		elif fNt==127:
			ZUA=8
			if VkN<kHl+ZUA:return JCj
			bbt=bytearray()
			for tdG in range(Fvx+1,Fvx+1+ZUA):bbt.extend(bytes([vrD.yKx[tdG]]))
			MUJ=gnU.peR(bbt);Fvx+=ZUA
		if VkN<kHl+ZUA+MUJ:return JCj
		Fvx+=1;return Crr(Fvx,Fvx+MUJ)
	@staticmethod
	def peR(PrM):
		if len(PrM)==2:return(PrM[0]&255)<<8|PrM[1]&255
		else:return(PrM[4]&127)<<24|(PrM[5]&255)<<16|(PrM[6]&255)<<8|PrM[7]&255
class MNt:
	cxA='GET /WebSocketConnection HTTP/1.1\r\n';fqs='GET /WebSocketConnection-Secure HTTP/1.1\r\n';jNh='Host: ';bME='Origin: ';jaR='Upgrade: websocket\r\n';WMQ='Sec-WebSocket-Key: 23eds34dfvce4\r\n';xde='Sec-WebSocket-Version: 13\r\n';hRg='Sec-WebSocket-Protocol: pushv1\r\n';KGJ='Connection: Upgrade\r\n';xIh='\r\n';cwg=2;yYY=10;swk=128;buj=128
	def GDg(self):vrD=B();Fvx=MNt.yYY;vrD.extend(bytearray(10));Fvx+=4;vrD.extend(bytes([r.randint(0,255),r.randint(0,255),r.randint(0,255),r.randint(0,255)]));vrD.vdE(Fvx);vrD.body_start_mark=Fvx;return vrD
	def vSZ(self,vrD):
		dXs=MNt.buj;dXs|=MNt.cwg;vrD.body_end_mark=len(vrD.yKx);iEb=vrD.body_end_mark-vrD.body_start_mark;QSR=self.AZp(iEb);bPv=self.igr(iEb,QSR);GFl=0;AVW=0
		if QSR==1:GFl=8;AVW=8;vrD.yKx[AVW]=dXs;vrD.yKx[AVW+1]=bPv[0]|MNt.swk
		elif QSR==2:
			GFl=6;AVW=6;vrD.yKx[AVW]=dXs;vrD.yKx[AVW+1]=126|MNt.swk;AVW+=2
			for tdG in range(0,2):vrD.yKx[AVW+tdG]=bPv[tdG]
		else:
			vrD.yKx[AVW]=dXs;vrD.yKx[AVW+1]=127|MNt.swk;AVW+=2
			for tdG in range(0,8):vrD.yKx[AVW+tdG]=bPv[tdG]
		hnr=bytearray();hnr.extend(bytes([vrD.yKx[vrD.body_start_mark-4]]));hnr.extend(bytes([vrD.yKx[vrD.body_start_mark-3]]));hnr.extend(bytes([vrD.yKx[vrD.body_start_mark-2]]));hnr.extend(bytes([vrD.yKx[vrD.body_start_mark-1]]));dji=0
		for tdG in range(vrD.body_start_mark,vrD.body_end_mark):
			b=vrD.yKx[tdG]^hnr[dji];vrD.yKx[tdG]=b
			if dji==3:dji=0
			else:dji+=1
		vrD.vdE(GFl)
	def fhl(self,host,encrypted):
		vrD=B()
		if encrypted is False:vrD.extend(bytes(MNt.cxA,_A))
		else:vrD.extend(bytes(MNt.fqs,_A))
		vrD.extend(bytes(MNt.bME,_A));vrD.extend(bytes('http://'+str(host),_A));vrD.extend(bytes(MNt.xIh,_A));vrD.extend(bytes(MNt.jNh,_A));vrD.extend(bytes(str(host),_A));vrD.extend(bytes(MNt.xIh,_A));vrD.extend(bytes(MNt.jaR,_A));vrD.extend(bytes(MNt.KGJ,_A));vrD.extend(bytes(MNt.WMQ,_A));vrD.extend(bytes(MNt.xde,_A));vrD.extend(bytes(MNt.hRg,_A));vrD.extend(bytes(MNt.xIh,_A));return vrD
	def AZp(self,size):
		if size<=125:return 1
		elif size<=65535:return 2
		return 8
	def igr(self,value,QSR):
		Ivr=bytearray();Ybw=8*QSR-8
		for tdG in range(0,QSR):hva=self.Rca(value,Ybw-8*tdG);CMM=hva-256*int(hva/256);Ivr.extend(bytes([CMM]))
		return Ivr
	def Rca(self,val,n):return val%4294967296>>n