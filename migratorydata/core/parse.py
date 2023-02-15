_A=None
from ..protocol.push_protocol import *
from ..protocol.message import hbd
from ..protocol.codec import JqV,AVP
class zSm:
	@staticmethod
	def LZV(tzo,logger):
		PsX=tzo.PKd
		if tzo.Htg[PsX]==72:PsX=zSm.rtR(tzo)
		if PsX==-1:return[]
		tzo.xgh(PsX);GCd=[]
		while True:
			if PsX>=len(tzo.Htg):return GCd
			if tzo.Htg[PsX]==rCj.ibi:PsX+=1
			else:
				try:vRh=JqV.Ksz(tzo,PsX)
				except IndexError:vRh=AVP(-1,-1)
				XCi=vRh.DUb();kCh=vRh.zsL()
				if XCi==-1:return GCd
				while True:
					sEb=zSm.IrL(tzo,XCi,kCh,rCj.czT)
					if sEb==-1:break
					wst=zSm.JEm(tzo,XCi+1,sEb,logger)
					if wst is not _A:message=hbd(rCj.HhG[tzo.Htg[XCi]],wst);GCd.append(message)
					XCi=sEb+1;tzo.xgh(XCi)
				PsX=tzo.PKd
	@staticmethod
	def rtR(tzo):
		NCA='\r\n\r\n'.encode('utf-8');PKd=tzo.PKd;sEb=zSm.search(tzo.Htg[PKd:],len(tzo.Htg),NCA,len(NCA))
		if sEb==-1:return-1
		PKd=sEb+len(NCA);return PKd
	@staticmethod
	def IrL(tzo,start,end,value):
		for sEb in range(start,end):
			if tzo.Htg[sEb]==value:return sEb
		return-1
	@staticmethod
	def JEm(tzo,start,end,logger):
		wst=_A
		while True:
			if start>=end:break
			YOy=tzo.Htg[start];jmc=zSm.IrL(tzo,start+1,end,rCj.CUW)
			if jmc==-1:logger.trace('Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: '+str(start)+', '+str(tzo.Htg[start:end]));return _A
			raH=rCj.Jyr(YOy)
			if raH is _A:logger.trace('Received an unknown Hdr - Hdr ignored, Hdr Position: '+str(tzo.Htg));start=jmc+1
			start=start+1
			if wst is _A:wst={}
			value=_A;HXJ=rCj.nND(raH);ptV=tzo.Htg[start:jmc]
			if HXJ==UxH.UOC:value=rCj.vzf(ptV)
			elif HXJ==UxH.gBo:bVu=rCj.VhM(ptV);value=bVu.decode('utf-8')
			elif HXJ==UxH.Rld:value=rCj.VhM(ptV)
			elif HXJ==UxH.shb:value=ptV
			VmB=wst.get(raH)
			if VmB is _A:wst[raH]=value
			else:values=[VmB,value];wst[raH]=values
			start=jmc+1
		return wst
	@staticmethod
	def search(bDQ,dataLength,pattern,patternLength):
		ngV=[0]*patternLength;qny=0;len=0;sEb=1
		while sEb<patternLength:
			if pattern[sEb]==pattern[len]:len+=1;ngV[sEb]=len;sEb+=1
			elif len!=0:len=ngV[len-1]
			else:ngV[sEb]=0;sEb+=1
		sEb=0
		while sEb<dataLength:
			if pattern[qny]==bDQ[sEb]:sEb+=1;qny+=1
			if qny==patternLength:return sEb-qny
			elif sEb<dataLength and pattern[qny]!=bDQ[sEb]:
				if qny!=0:qny=ngV[qny-1]
				else:sEb+=1
		return-1