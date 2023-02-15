_D='No existing operation for msg: '
_C=True
_B=False
_A=None
import time
from .parse import zSm
from .io import zQr,LAC
from ..migratorydata_client import MessageType,QoS
from ..protocol.codec import tIS,AKi
from .subject import Kde
from ..protocol.push_protocol import *
from ..protocol.message import ETT,hpI
from .network import Npu
class FfN:RRF=0;uFA=1;tag=2
class CES:Esx=0;HkO=1
class Connection:
	def __init__(self,configuration,listener_notifier,xco,logger):self._reconnect_retries=0;self._session=-1;self._socket=_A;self._reader=_A;self._writer=_A;self._reconnected=_B;self._session_received=_B;self._listener_notifier=_A;self._servers_down_count=0;self._is_server_down=_B;self._max_message_size=_A;self._node_type=FfN.RRF;self._SM=Kde();self._logger=logger;self._conf=configuration;self._listener_notifier=listener_notifier;self._cluster=xco;self._CS=CES.Esx;self._PE=AKi();self._TE=tIS();self._message_listener=JvT();self._message_listener.Hyk(self);self._cluster_token=_A;self._last_sent_ping_ticks=time.ticks_ms();self._last_received_ping_ticks=time.ticks_ms();self._keep_alive_time=configuration.DEFAULT_KEEP_ALIVE_TIMEOUT
	def LZu(self):return self._message_listener
	def dJc(self,tzo):
		GCd=_A;GCd=zSm.LZV(tzo,self._logger)
		if len(GCd)>0:self.lKs(GCd)
		self._last_received_ping_ticks=time.ticks_ms()
	def lKs(self,GCd):
		for sEb in range(0,len(GCd)):
			message=GCd[sEb]
			if message.operation==Eid.CLIENT_PUBLISH_RESPONSE or message.operation==Eid.QaI or message.operation==Eid.rNl or message.operation==Eid.zOj or message.operation==Eid.eEO or message.operation==Eid.Nab or message.operation==Eid.MSM or message.operation==Eid.GgP:self.LZu().on_message(message)
			elif message.operation==Eid.mav:break
			else:self._logger.warn(_D+str(message))
	def connect(self):
		if self._socket is not _A:self.disconnect()
		try:
			DVm=self._cluster.RHG();self._logger.info('Connecting to the clust Member: '+str(self._cluster.NfP()));self._socket=Npu.mfO(DVm.cWq(),DVm.yhX(),self._conf.encryption,self._conf.socket_timeout_seconds);self._writer=LAC(self._socket,self);self._reader=zQr(self._socket,self);tzo=self._TE.ojs(self._cluster.NfP().cWq(),self._conf.encryption)
			if len(tzo.Htg)>0:self._writer.write(tzo.Htg)
			self._reader.read()
		except Exception as gjM:print(gjM);import sys;sys.print_exception(gjM);self._logger.info('Failed to Connect: '+str(self._cluster.NfP()));return
		self.Ljp();self._reader.read()
	def Ljp(self):tzo=self._TE.ofp();pMZ=self._conf;self._PE.tWU(tzo.Htg,pMZ.entitlement_token,pMZ.session_type,pMZ.user_agent,pMZ.lEu);self._TE.fdj(tzo);self._write(tzo.Abd())
	def pJX(self):self.bQV('');self.disconnect();self._cluster.bGK(self._cluster.NfP());self._reconnected=_C;self.connect()
	def disconnect(self):
		if self._socket is not _A:self._socket.close()
		self._socket=_A;self._writer=_A;self._reader=_A;self.EYv()
	def wuR(self):self.disconnect()
	def EYv(self):self._CS=CES.Esx;self._session=-1;self._session_received=_B
	def subscribe(self,jPL,history):
		if jPL is _A or len(jPL)==0:return
		jPL=dJh.MZo(jPL);xpI=list(set(jPL)-set(self._SM.uJQ()))
		if len(xpI)==0:return
		self._SM.TDx(xpI,history)
		if self._CS==CES.HkO:self.okU(xpI)
	def okU(self,subjects_string):
		tzo=self._TE.ofp()
		for sRv in subjects_string:self.NsN(tzo,self._SM.get_subject(sRv))
		self._TE.fdj(tzo);self._write(tzo.Abd());self._reader.read()
	def NsN(self,tzo,sRv):self._PE.bXi(tzo.Htg,sRv,self._session)
	def unsubscribe(self,subjects_string):
		if subjects_string is _A or len(subjects_string)==0:return
		Mxy=list(set(subjects_string)&set(self._SM.uJQ()))
		if len(Mxy)==0:return
		ZAz=self._SM.NZR(Mxy)
		if self._CS==CES.HkO:self.CGa(ZAz)
	def CGa(self,jPL):
		tzo=self._TE.ofp()
		for sRv in jPL:self._PE.diW(tzo.Htg,self._session,sRv)
		self._TE.fdj(tzo);self._write(tzo.Abd());self._reader.read()
	def publish(self,message):
		if self.TpD():self.pJX()
		if self._CS!=CES.HkO:
			self.pJX()
			if self._CS!=CES.HkO:self.Knj(M.NOTIFY_PUBLISH_FAILED,message);return
		self.cdt(message)
	def cdt(self,message):
		xAl=message.get_reply_to_subject()
		if xAl is not _A and dJh.oDT(xAl)is _C and self._SM.pxR(xAl)is _B:self.subscribe([xAl],0)
		tzo=self._TE.ofp();self._PE.Ouz(tzo.Htg,message,self._session);self._TE.fdj(tzo)
		if self._max_message_size is not _A and len(tzo.Htg)-tzo.PKd>self._max_message_size:self.Knj(M.NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED,message);return
		self._write(tzo.Abd())
		if self._reader!=_A:self.check_for_messages()
	def Knj(self,notification,message):
		if message is not _A and message.get_closure()is not _A:self._listener_notifier.on_status(notification,message.get_closure())
	def _write(self,message):
		if self._writer is not _A:self._writer.write(message)
	def check_for_messages(self):
		if self.TpD():self.pJX()
		if self._CS!=CES.HkO:self.pJX()
		if self._reader!=_A:return self._reader.check_for_messages()
		return _A
	def qJB(self):
		Rwd=time.ticks_ms()
		if self._CS!=CES.HkO and time.ticks_add(self._last_sent_ping_ticks,self._conf.PING_INTERVAL)<Rwd:self.xcr();self._last_sent_ping_ticks=Rwd
	def xcr(self):
		tzo=self._TE.ofp();self._PE.UgJ(tzo.Htg,self._session);self._TE.fdj(tzo)
		if self._writer is not _A:self._write(tzo.Abd())
	def AWj(self):
		tzo=self._TE.ofp();self._PE.LMB(tzo.Htg,self._conf.entitlement_token,self._session);self._TE.fdj(tzo)
		if self._writer is not _A:self._write(tzo.Abd())
	def bQV(self,disconnect_info):
		self._logger.error('['+str(disconnect_info)+'] ['+str(self._cluster.NfP())+']');self._logger.info('Lost connection with the clust Member: '+str(self._cluster.NfP()))
		if self._session_received is _B:
			self._servers_down_count+=1
			if self._is_server_down is _B:
				if self._servers_down_count>=self._conf.servers_down_before_notify:self._is_server_down=_C;self._listener_notifier.on_status(M.NOTIFY_SERVER_DOWN,self._cluster.NfP().nTw())
	def dBT(self):self._is_server_down=_B;self._servers_down_count=0
	def zIT(self):self._logger.info('Connected to the clust Member: '+str(self._cluster.NfP()));self.dBT();self._listener_notifier.on_status(M.NOTIFY_SERVER_UP,self._cluster.NfP().nTw())
	def FzV(self):self._CS=CES.Esx
	def TpD(self):
		Rwd=time.ticks_ms()
		if self._CS==CES.HkO and time.ticks_add(self._last_received_ping_ticks,self._keep_alive_time)<Rwd:return _C
		return _B
class JvT:
	def __init__(self):self._connection=_A
	def Hyk(self,connection):self._connection=connection
	def on_message(self,message):
		wst=message.wst
		if message.operation==Eid.eEO:self.wxf(wst)
		elif message.operation==Eid.QaI:self.tYD(wst,message)
		elif message.operation==Eid.MSM:self.Tib(wst)
		elif message.operation==Eid.CLIENT_PUBLISH_RESPONSE:self.tJI(wst)
		elif message.operation==Eid.Nab:self.YBu()
		elif message.operation==Eid.rNl:self.YfV(wst)
		elif message.operation==Eid.zOj:self.vEf(wst)
		elif message.operation==Eid.GgP:self.cik(wst)
		else:self._connection._logger.warn(_D+str(message))
	def Tib(self,wst):
		OYn=wst.get(LuJ.kFg)
		if OYn is not _A:
			self._connection.zIT();self._connection._session=OYn;self._connection._session_received=_C;self._connection._reconnect_retries=0;self._last_sent_ping_ticks=time.ticks_ms();wQU=wst.get(LuJ.HDn)
			if wQU is not _A and wQU==1:self._connection._node_type=FfN.uFA
			if wQU is not _A and wQU==2:self._connection._node_type=FfN.tag
			UZT=wst.get(LuJ.GnM)
			if UZT is not _A:self._keep_alive_time=UZT*1000*1.4
			self._connection._CS=CES.HkO;mTP=wst.get(LuJ.ueP);self.rZH(mTP);byQ=wst.get(LuJ.LEM)
			if byQ is not _A:self._connection._max_message_size=byQ
			kkc=wst.get(LuJ.obu);error=wst.get(LuJ.ERROR)
			if error is not _A and error==hpI.PPc:self._connection._listener_notifier.on_status(M.FtS,kkc)
			else:self._connection._listener_notifier.on_status(M.oOZ,kkc if kkc!=_A else'')
			jPL=self._connection._SM.aVe()
			if len(jPL)>0:self._connection.okU(jPL)
	def wxf(self,wst):0
	def YBu(self):0
	def tYD(self,wst,msg):
		sRv=wst.get(LuJ.Piu);VMc=self._connection._SM.get_subject(sRv)
		if VMc is _A:return
		mTP=wst.get(LuJ.ueP);self.rZH(mTP);bDQ=wst.get(LuJ.rLN);closure=wst.get(LuJ.vDS);retained=_B;DdJ=wst.get(LuJ.sBx)
		if DdJ is not _A and DdJ==1:retained=_C
		OXT=_B;Lay=wst.get(LuJ.vGY)
		if Lay is not _A and Lay==1:OXT=_C
		if OXT==_C:bDQ='Error: OXT is not yet implemented.'
		uKH=MessageType.UPDATE;wXQ=wst.get(LuJ.dOe)
		if wXQ is not _A:
			if wXQ==Edk.SNAPSHOT:uKH=MessageType.SNAPSHOT
			elif wXQ==Edk.RECOVERED:uKH=MessageType.RECOVERED
			elif wXQ==Edk.HISTORICAL:uKH=MessageType.HISTORICAL
		laJ=QoS.GUARANTEED;ynY=wst.get(LuJ.qHM)
		if ynY is not _A and ynY==QoS.STANDARD:laJ=QoS.STANDARD
		if self._connection._node_type==FfN.uFA and laJ==QoS.GUARANTEED:
			message=ETT(sRv,bDQ,closure,retained,uKH,QoS.GUARANTEED,wst.get(LuJ.ijN),OXT);OmT=wst.get(LuJ.NEo);hnO=wst.get(LuJ.vbm);message.EAr(OmT);message.kvC(hnO);CBW=dJh.WdE(VMc,OmT,hnO,self._connection._listener_notifier,self._connection._logger)
			if CBW==IGb.keW:self._connection._listener_notifier.on_message(message)
			elif CBW==IGb.jgT:self._connection.reconnect(dJh.COe,'seq_higher')
		elif self._connection._node_type==FfN.tag and laJ==QoS.GUARANTEED:
			message=ETT(sRv,bDQ,closure,retained,uKH,QoS.GUARANTEED,wst.get(LuJ.ijN),OXT);OmT=wst.get(LuJ.NEo);hnO=wst.get(LuJ.vbm);message.EAr(OmT);message.kvC(hnO);CBW=dJh.xPN(VMc,OmT,hnO,self._connection._listener_notifier,self._connection._logger)
			if CBW==IGb.keW:self._connection._listener_notifier.on_message(message)
		else:message=ETT(sRv,bDQ,closure,retained,uKH,QoS.STANDARD,wst.get(LuJ.ijN),OXT);self._connection._listener_notifier.on_message(message)
	def tJI(self,wst):
		if wst is _A:return
		closure=wst.get(LuJ.vDS);flq=wst.get(LuJ.obu)
		if closure is not _A and flq is not _A:
			status=M.NOTIFY_PUBLISH_FAILED
			if flq==dJh.wLA:status=M.NOTIFY_PUBLISH_DENIED
			elif flq==dJh.FyN:status=M.NOTIFY_PUBLISH_OK
			self._connection._listener_notifier.on_status(status,closure)
	def YfV(self,wst):
		mxD=wst.get(LuJ.obu);sRv=wst.get(LuJ.Piu)
		if mxD is not _A and sRv is not _A:
			mtb=_C;Zag=M.NOTIFY_SUBSCRIBE_DENY
			if mxD==bYU.YfS:Zag=M.NOTIFY_SUBSCRIBE_ALLOW;mtb=_B
			elif mxD==bYU.YDR:Zag=M.NOTIFY_SUBSCRIBE_DENY
			if mtb is _C:self._connection._SM.NZR([sRv])
			self._connection._listener_notifier.on_status(Zag,sRv)
	def vEf(self,wst):
		sRv=wst.get(LuJ.Piu);status=wst.get(LuJ.dOe);self._connection._logger.info('Recovery Status for subj: '+str(sRv)+' is:'+str(status))
		if dJh.Ari==status:
			jPL=self._connection._SM.uJQ()
			for s in jPL:
				VMc=self._connection._SM.get_subject(s);lBV=VMc.czA()
				if dJh.pzp==lBV or dJh.pHn==lBV or dJh.aje==lBV:VMc.yuY()
				else:VMc.DUx()
		else:
			VMc=self._connection._SM.get_subject(sRv)
			if VMc is not _A:VMc.fKx(status)
	def cik(self,wst):status=wst.get(LuJ.obu);info=wst.get(LuJ.meQ);self._connection._listener_notifier.on_status(status,info)
	def rZH(self,_received_cluster_token):
		if _received_cluster_token is not _A:
			if self._connection._cluster_token is _A:self._connection._cluster_token=_received_cluster_token
			elif _received_cluster_token!=self._connection._cluster_token:self._connection._cluster_token=_received_cluster_token;self._connection._SM.reO()
from .util import *