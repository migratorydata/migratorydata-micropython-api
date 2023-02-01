_A=None
from migratorydata.protocol.push_protocol import *
from migratorydata.protocol.message import vYC
from migratorydata.protocol.codec import gnU,Crr
class NgC:
	@staticmethod
	def Pff(vrD,logger):
		tBo=vrD.Fvx
		if vrD.yKx[tBo]==72:tBo=NgC.FHW(vrD)
		if tBo==-1:return[]
		vrD.vdE(tBo);OFn=[]
		while True:
			if tBo>=len(vrD.yKx):return OFn
			if vrD.yKx[tBo]==msU.uiM:tBo+=1
			else:
				try:HJU=gnU.zsy(vrD,tBo)
				except IndexError:HJU=Crr(-1,-1)
				bWw=HJU.IMd();daR=HJU.IGC()
				if bWw==-1:return OFn
				while True:
					tdG=NgC.jZp(vrD,bWw,daR,msU.Ydq)
					if tdG==-1:break
					axu=NgC.KaF(vrD,bWw+1,tdG,logger)
					if axu is not _A:message=vYC(msU.XJr[vrD.yKx[bWw]],axu);OFn.append(message)
					bWw=tdG+1;vrD.vdE(bWw)
				tBo=vrD.Fvx
	@staticmethod
	def FHW(vrD):
		Ckh='\r\n\r\n'.encode('utf-8');Fvx=vrD.Fvx;tdG=NgC.search(vrD.yKx[Fvx:],len(vrD.yKx),Ckh,len(Ckh))
		if tdG==-1:return-1
		Fvx=tdG+len(Ckh);return Fvx
	@staticmethod
	def jZp(vrD,start,end,value):
		for tdG in range(start,end):
			if vrD.yKx[tdG]==value:return tdG
		return-1
	@staticmethod
	def KaF(vrD,start,end,logger):
		axu=_A
		while True:
			if start>=end:break
			Vhq=vrD.yKx[start];SZk=NgC.jZp(vrD,start+1,end,msU.max)
			if SZk==-1:logger.trace('Received an invalid msg: Hdr end missing - msg ignored, Hdr Position: '+str(start)+', '+str(vrD.yKx[start:end]));return _A
			vDO=msU.vWP(Vhq)
			if vDO is _A:logger.trace('Received an unknown Hdr - Hdr ignored, Hdr Position: '+str(vrD.yKx));start=SZk+1
			start=start+1
			if axu is _A:axu={}
			value=_A;vzm=msU.Ikw(vDO);MDn=vrD.yKx[start:SZk]
			if vzm==xpp.Xkq:value=msU.KEz(MDn)
			elif vzm==xpp.Pfy:Rwq=msU.fLt(MDn);value=Rwq.decode('utf-8')
			elif vzm==xpp.eFH:value=msU.fLt(MDn)
			elif vzm==xpp.ZKD:value=MDn
			hwP=axu.get(vDO)
			if hwP is _A:axu[vDO]=value
			else:values=[hwP,value];axu[vDO]=values
			start=SZk+1
		return axu
	@staticmethod
	def search(PrM,dataLength,pattern,patternLength):
		SoJ=[0]*patternLength;dji=0;len=0;tdG=1
		while tdG<patternLength:
			if pattern[tdG]==pattern[len]:len+=1;SoJ[tdG]=len;tdG+=1
			elif len!=0:len=SoJ[len-1]
			else:SoJ[tdG]=0;tdG+=1
		tdG=0
		while tdG<dataLength:
			if pattern[dji]==PrM[tdG]:tdG+=1;dji+=1
			if dji==patternLength:return tdG-dji
			elif tdG<dataLength and pattern[dji]!=PrM[tdG]:
				if dji!=0:dji=SoJ[dji-1]
				else:tdG+=1
		return-1