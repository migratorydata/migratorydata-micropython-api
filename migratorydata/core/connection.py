_D='No existing operation for msg: '
_C=True
_B=False
_A=None
import time
from migratorydata.core.parse import NgC
from migratorydata.core.io import wPB,cjf
from migratorydata.migratorydata_message import *
from migratorydata.protocol.codec import MNt,Mbl
from migratorydata.core.subject import rhz
from migratorydata.protocol.push_protocol import *
from migratorydata.protocol.message import SIq,xST
from migratorydata.core.network import ubN
class FLJ:vyj=0;mUL=1;YhD=2
class ZTk:NNC=0;LeU=1
class Connection:
	def __init__(self,configuration,listener_notifier,GiK,logger):self._reconnect_retries=0;self._session=-1;self._socket=_A;self._reader=_A;self._writer=_A;self._reconnected=_B;self._session_received=_B;self._listener_notifier=_A;self._servers_down_count=0;self._is_server_down=_B;self._max_message_size=_A;self._node_type=FLJ.vyj;self._SM=rhz();self._logger=logger;self._conf=configuration;self._listener_notifier=listener_notifier;self._cluster=GiK;self._CS=ZTk.NNC;self._PE=Mbl();self._TE=MNt();self._message_listener=fOm();self._message_listener.NgP(self);self._cluster_token=_A;self._last_sent_ping_ticks=time.ticks_ms();self._last_received_ping_ticks=time.ticks_ms();self._keep_alive_time=configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
	def tAz(self):return self._message_listener
	def JLZ(self,vrD):
		OFn=_A;OFn=NgC.Pff(vrD,self._logger)
		if len(OFn)>0:self.ELl(OFn)
		self._last_received_ping_ticks=time.ticks_ms()
	def ELl(self,OFn):
		for tdG in range(0,len(OFn)):
			message=OFn[tdG]
			if message.operation==QeI.CLIENT_PUBLISH_RESPONSE or message.operation==QeI.BwO or message.operation==QeI.JtY or message.operation==QeI.raQ or message.operation==QeI.tPQ or message.operation==QeI.piP or message.operation==QeI.HZk or message.operation==QeI.rPQ:self.tAz().on_message(message)
			elif message.operation==QeI.zLx:break
			else:self._logger.warn(_D+str(message))
	def connect(self):
		if self._socket is not _A:self.disconnect()
		try:
			xOh=self._cluster.hUR();self._logger.info('Connecting to the clust Member: '+str(self._cluster.uAu()));self._socket=ubN.bPO(xOh.Lhm(),xOh.Luu(),self._conf.encryption,self._conf.socket_timeout_seconds);self._writer=cjf(self._socket,self);self._reader=wPB(self._socket,self);vrD=self._TE.fhl(self._cluster.uAu().Lhm(),self._conf.encryption)
			if len(vrD.yKx)>0:self._writer.write(vrD.yKx)
			self._reader.read()
		except Exception as LqI:print(LqI);import sys;sys.print_exception(LqI);self._logger.info('Failed to Connect: '+str(self._cluster.uAu()))
		self.PIe();self._reader.read()
	def PIe(self):vrD=self._TE.GDg();rwP=self._conf;self._PE.tPH(vrD.yKx,rwP.entitlement_token,rwP.session_type,rwP.user_agent,rwP.nBj);self._TE.vSZ(vrD);self._write(vrD.DFN())
	def lfg(self):self.Gqo('');self.disconnect();self._cluster.KPV(self._cluster.uAu());self._reconnected=_C;self.connect()
	def disconnect(self):
		if self._socket is not _A:self._socket.close()
		self._socket=_A;self._writer=_A;self._reader=_A;self.AgP()
	def MzQ(self):self.disconnect()
	def AgP(self):self._CS=ZTk.NNC;self._session=-1;self._session_received=_B
	def subscribe(self,qFN,history):
		if qFN is _A or len(qFN)==0:return
		qFN=QKt.LmM(qFN);aRz=list(set(qFN)-set(self._SM.lwg()))
		if len(aRz)==0:return
		self._SM.uQr(aRz,history)
		if self._CS==ZTk.LeU:self.YvN(aRz)
	def YvN(self,subjects_string):
		vrD=self._TE.GDg()
		for qpH in subjects_string:self.VYl(vrD,self._SM.get_subject(qpH))
		self._TE.vSZ(vrD);self._write(vrD.DFN());self._reader.read()
	def VYl(self,vrD,qpH):self._PE.eno(vrD.yKx,qpH,self._session)
	def unsubscribe(self,subjects_string):
		if subjects_string is _A or len(subjects_string)==0:return
		Nrd=list(set(subjects_string)&set(self._SM.lwg()))
		if len(Nrd)==0:return
		Myl=self._SM.jyu(Nrd)
		if self._CS==ZTk.LeU:self.tKT(Myl)
	def tKT(self,qFN):
		vrD=self._TE.GDg()
		for qpH in qFN:self._PE.GWM(vrD.yKx,self._session,qpH)
		self._TE.vSZ(vrD);self._write(vrD.DFN());self._reader.read()
	def publish(self,message):
		if self.FXL():self.lfg()
		if self._CS!=ZTk.LeU:
			self.lfg()
			if self._CS!=ZTk.LeU:self.tUn(M.NOTIFY_PUBLISH_FAILED,message);return
		self.Yis(message)
	def Yis(self,message):
		Nyp=message.get_reply_to_subject()
		if Nyp is not _A and QKt.kVP(Nyp)is _C and self._SM.QxT(Nyp)is _B:self.subscribe([Nyp],0)
		vrD=self._TE.GDg();self._PE.Elg(vrD.yKx,message,self._session);self._TE.vSZ(vrD)
		if self._max_message_size is not _A and len(vrD.yKx)-vrD.Fvx>self._max_message_size:self.tUn(M.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED,message);return
		self._write(vrD.DFN())
		if self._reader!=_A:self.check_for_messages()
	def tUn(self,notification,message):
		if message is not _A and message.get_closure()is not _A:self._listener_notifier.on_status(notification,message.get_closure())
	def _write(self,message):
		if self._writer is not _A:self._writer.write(message)
	def check_for_messages(self):
		if self.FXL():self.lfg()
		if self._CS!=ZTk.LeU:self.lfg()
		if self._reader!=_A:return self._reader.check_for_messages()
		return _A
	def yda(self):
		LnU=time.ticks_ms()
		if self._CS!=ZTk.LeU and time.ticks_add(self._last_sent_ping_ticks,self._conf.PING_INTERVAL)<LnU:self.aop();self._last_sent_ping_ticks=LnU
	def aop(self):
		vrD=self._TE.GDg();self._PE.GnG(vrD.yKx,self._session);self._TE.vSZ(vrD)
		if self._writer is not _A:self._write(vrD.DFN())
	def ZGG(self):
		vrD=self._TE.GDg();self._PE.aoa(vrD.yKx,self._conf.entitlement_token,self._session);self._TE.vSZ(vrD)
		if self._writer is not _A:self._write(vrD.DFN())
	def Gqo(self,disconnect_info):
		self._logger.error('['+str(disconnect_info)+'] ['+str(self._cluster.uAu())+']');self._logger.info('Lost connection with the clust Member: '+str(self._cluster.uAu()))
		if self._session_received is _B:
			self._servers_down_count+=1
			if self._is_server_down is _B:
				if self._servers_down_count>=self._conf.servers_down_before_notify:self._is_server_down=_C;self._listener_notifier.on_status(M.NOTIFY_SERVER_DOWN,self._cluster.uAu().vJB())
	def jBm(self):self._is_server_down=_B;self._servers_down_count=0
	def aPu(self):self._logger.info('Connected to the clust Member: '+str(self._cluster.uAu()));self.jBm();self._listener_notifier.on_status(M.NOTIFY_SERVER_UP,self._cluster.uAu().vJB())
	def RHi(self):self._CS=ZTk.NNC
	def FXL(self):
		LnU=time.ticks_ms()
		if self._CS==ZTk.LeU and time.ticks_add(self._last_received_ping_ticks,self._keep_alive_time)<LnU:return _C
		return _B
class fOm:
	def __init__(self):self._connection=_A
	def NgP(self,connection):self._connection=connection
	def on_message(self,message):
		axu=message.axu
		if message.operation==QeI.tPQ:self.nyZ(axu)
		elif message.operation==QeI.BwO:self.Xut(axu,message)
		elif message.operation==QeI.HZk:self.EHK(axu)
		elif message.operation==QeI.CLIENT_PUBLISH_RESPONSE:self.krZ(axu)
		elif message.operation==QeI.piP:self.mVL()
		elif message.operation==QeI.JtY:self.QAz(axu)
		elif message.operation==QeI.raQ:self.fPC(axu)
		elif message.operation==QeI.rPQ:self.CxT(axu)
		else:self._connection._logger.warn(_D+str(message))
	def EHK(self,axu):
		FFW=axu.get(qUd.yvl)
		if FFW is not _A:
			self._connection.aPu();self._connection._session=FFW;self._connection._session_received=_C;self._connection._reconnect_retries=0;self._last_sent_ping_ticks=time.ticks_ms();XEA=axu.get(qUd.Fxy)
			if XEA is not _A and XEA==1:self._connection._node_type=FLJ.mUL
			if XEA is not _A and XEA==2:self._connection._node_type=FLJ.YhD
			Qhb=axu.get(qUd.YyQ)
			if Qhb is not _A:self._keep_alive_time=Qhb*1000*1.4
			self._connection._CS=ZTk.LeU;sbc=axu.get(qUd.wbx);self.Ubv(sbc);GeA=axu.get(qUd.Yns)
			if GeA is not _A:self._connection._max_message_size=GeA
			fKI=axu.get(qUd.Huq);error=axu.get(qUd.ERROR)
			if error is not _A and error==xST.gYT:self._connection._listener_notifier.on_status(M.emj,fKI)
			else:self._connection._listener_notifier.on_status(M.vRo,fKI if fKI!=_A else'')
			qFN=self._connection._SM.wCp()
			if len(qFN)>0:self._connection.YvN(qFN)
	def nyZ(self,axu):0
	def mVL(self):0
	def Xut(self,axu,msg):
		qpH=axu.get(qUd.CMD);sOZ=self._connection._SM.get_subject(qpH)
		if sOZ is _A:return
		sbc=axu.get(qUd.wbx);self.Ubv(sbc);PrM=axu.get(qUd.OWx);closure=axu.get(qUd.uFN);retained=_B;wPK=axu.get(qUd.yvW)
		if wPK is not _A and wPK==1:retained=_C
		IDI=_B;pjF=axu.get(qUd.vPj)
		if pjF is not _A and pjF==1:IDI=_C
		if IDI==_C:PrM='Error: IDI is not yet implemented.'
		FMg=MessageType.UPDATE;Oll=axu.get(qUd.nvQ)
		if Oll is not _A:
			if Oll==oUK.SNAPSHOT:FMg=MessageType.SNAPSHOT
			elif Oll==oUK.RECOVERED:FMg=MessageType.RECOVERED
			elif Oll==oUK.HISTORICAL:FMg=MessageType.HISTORICAL
		NMN=QoS.GUARANTEED;Wrb=axu.get(qUd.QlV)
		if Wrb is not _A and Wrb==QoS.STANDARD:NMN=QoS.STANDARD
		if self._connection._node_type==FLJ.mUL and NMN==QoS.GUARANTEED:
			message=SIq(qpH,PrM,closure,retained,FMg,QoS.GUARANTEED,axu.get(qUd.BmE),IDI);HxA=axu.get(qUd.VDH);akk=axu.get(qUd.jMx);message.Gop(HxA);message.TwH(akk);gIe=QKt.sKa(sOZ,HxA,akk,self._connection._listener_notifier,self._connection._logger)
			if gIe==tnn.rNX:self._connection._listener_notifier.on_message(message)
			elif gIe==tnn.TxA:self._connection.reconnect(QKt.AVc,'seq_higher')
		elif self._connection._node_type==FLJ.YhD and NMN==QoS.GUARANTEED:
			message=SIq(qpH,PrM,closure,retained,FMg,QoS.GUARANTEED,axu.get(qUd.BmE),IDI);HxA=axu.get(qUd.VDH);akk=axu.get(qUd.jMx);message.Gop(HxA);message.TwH(akk);gIe=QKt.ZmA(sOZ,HxA,akk,self._connection._listener_notifier,self._connection._logger)
			if gIe==tnn.rNX:self._connection._listener_notifier.on_message(message)
		else:message=SIq(qpH,PrM,closure,retained,FMg,QoS.STANDARD,axu.get(qUd.BmE),IDI);self._connection._listener_notifier.on_message(message)
	def krZ(self,axu):
		if axu is _A:return
		closure=axu.get(qUd.uFN);KgU=axu.get(qUd.Huq)
		if closure is not _A and KgU is not _A:
			status=M.NOTIFY_PUBLISH_FAILED
			if KgU==QKt.WZU:status=M.NOTIFY_PUBLISH_DENIED
			elif KgU==QKt.VJP:status=M.NOTIFY_PUBLISH_OK
			self._connection._listener_notifier.on_status(status,closure)
	def QAz(self,axu):
		YuL=axu.get(qUd.Huq);qpH=axu.get(qUd.CMD)
		if YuL is not _A and qpH is not _A:
			gEH=_C;gpF=M.NOTIFY_SUBSCRIBE_DENY
			if YuL==IfT.ESZ:gpF=M.NOTIFY_SUBSCRIBE_ALLOW;gEH=_B
			elif YuL==IfT.kQd:gpF=M.NOTIFY_SUBSCRIBE_DENY
			if gEH is _C:self._connection._SM.jyu([qpH])
			self._connection._listener_notifier.on_status(gpF,qpH)
	def fPC(self,axu):
		qpH=axu.get(qUd.CMD);status=axu.get(qUd.nvQ);self._connection._logger.info('Recovery Status for subj: '+str(qpH)+' is:'+str(status))
		if QKt.BVP==status:
			qFN=self._connection._SM.lwg()
			for s in qFN:
				sOZ=self._connection._SM.get_subject(s);JFT=sOZ.wlz()
				if QKt.DcN==JFT or QKt.bve==JFT or QKt.YJJ==JFT:sOZ.DyP()
				else:sOZ.WWj()
		else:
			sOZ=self._connection._SM.get_subject(qpH)
			if sOZ is not _A:sOZ.qHo(status)
	def CxT(self,axu):status=axu.get(qUd.Huq);info=axu.get(qUd.APr);self._connection._listener_notifier.on_status(status,info)
	def Ubv(self,_received_cluster_token):
		if _received_cluster_token is not _A:
			if self._connection._cluster_token is _A:self._connection._cluster_token=_received_cluster_token
			elif _received_cluster_token!=self._connection._cluster_token:self._connection._cluster_token=_received_cluster_token;self._connection._SM.jNL()
from migratorydata.core.util import *