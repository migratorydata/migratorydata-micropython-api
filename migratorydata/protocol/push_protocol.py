import struct
class VWl:
	zHz=[];OdB=[];zXe=[];kFC=[];ZAf=25;ciG=127;FAa=30;DHr=31;OiN=[];xZU=[];ZNi=[]
	@staticmethod
	def oIC():
		for B in range(0,128):VWl.zHz.append(-1)
		VWl.zHz[yZW.aoD]=1;VWl.zHz[yZW.Apn]=2;VWl.zHz[yZW.TTE]=3;VWl.zHz[yZW.EOC]=4;VWl.zHz[yZW.XZj]=5;VWl.zHz[yZW.ClT]=6;VWl.zHz[yZW.Qlz]=8;VWl.zHz[yZW.oWs]=9;VWl.zHz[yZW.FRc]=12;VWl.zHz[yZW.beJ]=16;VWl.zHz[yZW.CLIENT_PUBLISH_RESPONSE]=19;VWl.zHz[yZW.wFt]=26;VWl.zHz[yZW.BCa]=7;VWl.zHz[yZW.KZZ]=11
		for B in range(0,128):VWl.OiN.append(-1)
		for A in range(0,yZW.KZZ+1):VWl.OiN[VWl.kNt(A)]=A
		for B in range(0,128):VWl.OdB.append(-1)
		VWl.OdB[ssB.inO]=1;VWl.OdB[ssB.OMZ]=2;VWl.OdB[ssB.Xdm]=3;VWl.OdB[ssB.mmS]=4;VWl.OdB[ssB.vli]=5;VWl.OdB[ssB.VdX]=6;VWl.OdB[ssB.UFY]=7;VWl.OdB[ssB.WHO]=8;VWl.OdB[ssB.QUT]=9;VWl.OdB[ssB.ERROR]=11;VWl.OdB[ssB.DXs]=12;VWl.OdB[ssB.RiS]=15;VWl.OdB[ssB.ulT]=16;VWl.OdB[ssB.aOE]=17;VWl.OdB[ssB.VTl]=18;VWl.OdB[ssB.eAm]=19;VWl.OdB[ssB.zXS]=20;VWl.OdB[ssB.zSb]=21;VWl.OdB[ssB.ykt]=22;VWl.OdB[ssB.wsX]=23;VWl.OdB[ssB.lWK]=24;VWl.OdB[ssB.XBf]=26;VWl.OdB[ssB.LSA]=32;VWl.OdB[ssB.GzR]=39;VWl.OdB[ssB.fmO]=40;VWl.OdB[ssB.Vxz]=35;VWl.OdB[ssB.cxQ]=36;VWl.OdB[ssB.yQX]=37;VWl.OdB[ssB.AKb]=44;VWl.OdB[ssB.DoJ]=45;VWl.OdB[ssB.obh]=46;VWl.OdB[ssB.UQb]=47;VWl.OdB[ssB.abu]=48;VWl.OdB[ssB.aMX]=29;VWl.OdB[ssB.PTc]=38
		for B in range(0,128):VWl.xZU.append(-1)
		for A in range(0,ssB.PTc+1):VWl.xZU[VWl.gCJ(A)]=A
		for B in range(0,128):VWl.ZNi.append(-1)
		VWl.Sod(ssB.inO,Xiz.JnR);VWl.Sod(ssB.OMZ,Xiz.Lwg);VWl.Sod(ssB.Xdm,Xiz.dHF);VWl.Sod(ssB.mmS,Xiz.dHF);VWl.Sod(ssB.vli,Xiz.dHF);VWl.Sod(ssB.VdX,Xiz.dHF);VWl.Sod(ssB.UFY,Xiz.Lwg);VWl.Sod(ssB.WHO,Xiz.Lwg);VWl.Sod(ssB.QUT,Xiz.Lwg);VWl.Sod(ssB.ERROR,Xiz.dHF);VWl.Sod(ssB.DXs,Xiz.Lwg);VWl.Sod(ssB.RiS,Xiz.dHF);VWl.Sod(ssB.VTl,Xiz.JnR);VWl.Sod(ssB.eAm,Xiz.JnR);VWl.Sod(ssB.zXS,Xiz.JnR);VWl.Sod(ssB.zSb,Xiz.dHF);VWl.Sod(ssB.ykt,Xiz.dHF);VWl.Sod(ssB.wsX,Xiz.dHF);VWl.Sod(ssB.lWK,Xiz.dHF);VWl.Sod(ssB.XBf,Xiz.JnR);VWl.Sod(ssB.LSA,Xiz.JnR);VWl.Sod(ssB.GzR,Xiz.JnR);VWl.Sod(ssB.Vxz,Xiz.JnR);VWl.Sod(ssB.cxQ,Xiz.dHF);VWl.Sod(ssB.yQX,Xiz.dHF);VWl.Sod(ssB.ulT,Xiz.JnR);VWl.Sod(ssB.aOE,Xiz.dHF);VWl.Sod(ssB.fmO,Xiz.dHF);VWl.Sod(ssB.AKb,Xiz.JnR);VWl.Sod(ssB.DoJ,Xiz.dHF);VWl.Sod(ssB.obh,Xiz.dHF);VWl.Sod(ssB.UQb,Xiz.dHF);VWl.Sod(ssB.abu,Xiz.JnR);VWl.Sod(ssB.aMX,Xiz.dHF);VWl.Sod(ssB.PTc,Xiz.dHF)
		for B in range(0,255):VWl.kFC.append(-1)
		VWl.kFC[VWl.ciG]=1;VWl.kFC[VWl.FAa]=2;VWl.kFC[VWl.DHr]=3;VWl.kFC[Xyu.hsL]=4;VWl.kFC[Xyu.Ene]=5;VWl.kFC[Xyu.aUI]=6;VWl.kFC[Xyu.Uyd]=7;VWl.kFC[Xyu.Flr]=8;VWl.kFC[33]=9;VWl.kFC[VWl.ZAf]=11
		for B in range(0,255):VWl.zXe.append(-1)
		for A in range(0,128):
			C=VWl.doN(A)
			if C!=-1:VWl.zXe[C]=A
	@staticmethod
	def Sod(Mlk,hdr_type):VWl.ZNi[VWl.gCJ(Mlk)]=hdr_type
	@staticmethod
	def mSp(LDT):
		A=VWl.wpV(LDT);G=0
		for B in range(0,len(A)):
			F=VWl.doN(A[B])
			if F!=-1:G+=1
		if G==0:C=bytearray();C.extend(bytes(A));return C
		D=[]
		for H in range(0,len(A)+G):D.append(0)
		B=0;E=0
		while B<len(A):
			F=VWl.doN(A[B])
			if F!=-1:D[E]=VWl.DHr;D[E+1]=F;E+=1
			else:D[E]=A[B]
			B+=1;E+=1
		C=bytearray();C.extend(bytes(D));return C
	@staticmethod
	def GXg(PcK):
		A=PcK;F=0
		for B in range(0,len(A)):
			E=VWl.doN(A[B])
			if E!=-1:F+=1
		if F==0:return A
		C=[]
		for H in range(0,len(A)+F):C.append(0)
		B=0;D=0
		while B<len(A):
			E=VWl.doN(A[B])
			if E!=-1:C[D]=VWl.DHr;C[D+1]=E;D+=1
			else:C[D]=A[B]
			B+=1;D+=1
		G=bytearray();G.extend(bytes(C));return G
	@staticmethod
	def TFM(LDT):
		E=LDT;A=list(struct.unpack(len(E)*'B',E));F=0
		if len(A)==0:return E
		for B in range(0,len(A)):
			if A[B]==VWl.DHr:F+=1
		C=[]
		for I in range(0,len(A)-F):C.append(0)
		B=0;D=0
		while B<len(A):
			G=A[B]
			if G==VWl.DHr:
				if B+1<len(A):
					C[D]=VWl.nyn(A[B+1])
					if C[D]==-1:raise ValueError()
					B+=1
				else:raise ValueError()
			else:C[D]=G
			B+=1;D+=1
		H=bytearray();H.extend(bytes(C));return H
	@staticmethod
	def Dqp(LDT,_headerId,_headerType):
		D=LDT;B=_headerType;A=None;E=D.find(chr(VWl.gCJ(_headerId)));F=D.find(chr(VWl.FAa),E)
		if E!=-1 and F!=-1:
			C=D[E+1:F]
			if B==Xiz.gLu:A=C
			elif B==Xiz.Lwg:A=C
			elif B==Xiz.JnR:A=C
			elif B==Xiz.dHF:A=VWl.kfG(C)
		return A
	@staticmethod
	def kfG(_dataString):
		I=_dataString;B=list(struct.unpack(len(I)*'B',I));H=0;C=-1;D=0;E=len(B);F=0
		if E==1:return B[0]
		elif E==2 and B[F]==VWl.DHr:
			A=VWl.nyn(B[F+1])
			if A!=-1:return A
			else:raise ValueError()
		while E>0:
			A=B[F];F+=1
			if A==VWl.DHr:
				if E-1<0:raise ValueError()
				E-=1;A=B[F];F+=1;G=VWl.nyn(A)
				if G==-1:raise ValueError()
			else:G=A
			if C>0:D|=G>>C;H=H<<8|(D if D>=0 else D+256);D=G<<8-C
			else:D=G<<-C
			C=(C+7)%8;E-=1
		return H
	@staticmethod
	def auC(_val):
		C=_val
		if int(C)&4294967168==0:
			G=VWl.doN(C)
			if G==-1:return struct.pack('B',C)
			else:return struct.pack('BB',VWl.DHr,G)
		D=0
		if int(C)&4278190080!=0:D=24
		elif int(C)&16711680!=0:D=16
		else:D=8
		B=[]
		for G in range(0,10):B.append(0)
		A=0;H=0
		while D>=0:
			F=int(C)>>D&255;H+=1;B[A]|=(F if F>=0 else F+256)>>H;E=VWl.doN(B[A])
			if E!=-1:B[A]=VWl.DHr;B[A+1]=E;A+=1
			A+=1;B[A]|=F<<7-H&127;D-=8
		E=VWl.doN(B[A])
		if E!=-1:B[A]=VWl.DHr;B[A+1]=E;A+=1
		A+=1
		if A<len(B):B=B[0:A]
		I=bytearray();I.extend(bytes(B));return I
	@staticmethod
	def nyn(b):
		if b>=0:return VWl.zXe[int(b)]
		else:return-1
	@staticmethod
	def doN(b):
		if b>=0:return VWl.kFC[int(b)]
		else:return-1
	@staticmethod
	def gCJ(h):return VWl.OdB[int(h)]
	@staticmethod
	def kNt(o):return VWl.zHz[int(o)]
	@staticmethod
	def Paj(Mlk):A=VWl.gCJ(Mlk);return VWl.ZNi[A]
	@staticmethod
	def wpV(str_value):A=str_value.encode('utf-8');return list(struct.unpack(len(A)*'B',A))
	@staticmethod
	def NHk(b):
		if b<0:return None
		return VWl.xZU[b]
class yZW:aoD=0;Apn=1;TTE=2;EOC=3;XZj=4;ClT=5;Qlz=6;oWs=7;FRc=8;beJ=9;CLIENT_PUBLISH_RESPONSE=10;wFt=11;BCa=12;KZZ=13
class ssB:inO=0;OMZ=1;Xdm=2;mmS=3;vli=4;VdX=5;UFY=6;WHO=7;QUT=8;ERROR=9;DXs=10;RiS=11;VTl=12;eAm=13;zXS=14;zSb=15;ykt=16;wsX=17;lWK=18;XBf=19;LSA=20;GzR=21;Vxz=22;cxQ=23;yQX=24;ulT=25;aOE=26;fmO=27;AKb=28;DoJ=29;obh=30;UQb=31;abu=32;aMX=33;PTc=34
class Xiz:gLu=0;Lwg=1;JnR=2;dHF=3
class Xyu:hsL=0;Uyd=34;Ene=10;aUI=13;Flr=92
class UkE:CNU=1;QBs=2;xiQ=3;PAG=4
class XAE:xsd=0;EDw=1;BoY=2;InT=3;mSN=4;MEf=5;Txg=6;tjT=7;vKL=8
class qae:SNAPSHOT='1';UPDATE='2';RECOVERED='3';HISTORICAL='4'
class IEf:WFt='d';rSG='a'
VWl.oIC()