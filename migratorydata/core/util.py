_A=False
import re
from .subject import *
class rLo:qsX=0;IKk=1;cKQ=2
class ASC:
	def __init__(self,session_type,user_agent):self.DoJ=6;self.session_type=session_type;self.user_agent=user_agent+', version:'+str(self.DoJ);self.DEFAULT_KEEP_ALIVE_TIMEOUT=30000;self.PING_INTERVAL=900000;self.servers_down_before_notify=1;self.entitlement_token=None;self.encryption=_A;self.socket_timeout_seconds=2;self._subjects={}
	def oVX(self,ALH,history):
		for Owg in ALH:self._subjects[Owg]=history
	def pWy(self,ALH):
		for Owg in ALH:
			try:del self._subjects[Owg]
			except KeyError:pass
	def get_subjects(self):return self._subjects
class Cis:
	tOn='OK';YFc='DENY';Mof='connection_active_close_keep_alive';iiL='connection_active_close_seq_higher';gQW='connection_passive_close';SBD='connection_error';fCu='cache_ok';Fpl='cache_ok_no_new_message';xog='cache_ok_new_epoch';tlS='end';Dkl='^\\/([^\\/]+\\/)*([^\\/]+|\\*)$'
	@staticmethod
	def Ovm(Rih):
		if not isinstance(Rih,str):return _A
		ksl=re.compile(Cis.Dkl)
		if ksl.search(Rih)is not None:return True
		return _A
	@staticmethod
	def VbE(ALH):
		GWw=[]
		for Owg in ALH:
			if Owg is not None and Cis.Ovm(Owg):GWw.append(Owg)
		return GWw
	@staticmethod
	def TaD(dGR,recv_seq,recv_seq_id,listener_notifier,logger):
		if dGR.GjX()!=recv_seq_id:dGR.MAP(recv_seq);dGR.RXI(recv_seq_id);return rLo.qsX
		if recv_seq<=dGR.get_seq():return rLo.IKk
		if recv_seq==dGR.get_seq()+1:
			if dGR.Yji()==CKs.aEp:dGR.PHn();listener_notifier.on_status(M.NOTIFY_DATA_SYNC,dGR.get_subject())
			dGR.MAP(dGR.get_seq()+1);return rLo.qsX
		if dGR.pIa()>0:logger.info('Missing Messages: expected message with sequence number: '+str(dGR.get_seq()+1)+', received instead message with sequence number:  '+str(recv_seq)+' !');return rLo.cKQ
		logger.info("Reset sequence: '"+str(dGR.get_seq()+1)+"'. The new sequence is: '"+str(recv_seq)+"' !");dGR.MAP(recv_seq);listener_notifier.on_status(M.NOTIFY_DATA_RESYNC,dGR.get_subject());return rLo.qsX
	@staticmethod
	def ShY(dGR,recv_seq,recv_seq_id):
		if dGR.GjX()!=recv_seq_id:dGR.MAP(recv_seq);dGR.RXI(recv_seq_id);return rLo.qsX
		if recv_seq<=dGR.get_seq():return rLo.IKk
		if dGR.Yji()==CKs.aEp:dGR.PHn()
		dGR.MAP(recv_seq);return rLo.qsX
from ..migratorydata_client import MigratoryDataClient as M