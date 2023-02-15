_A=False
import re
from .subject import *
class IGb:keW=0;ulp=1;jgT=2
class eRg:
	def __init__(self,session_type,user_agent):self.lEu=6;self.session_type=session_type;self.user_agent=user_agent+', version:'+str(self.lEu);self.DEFAULT_KEEP_ALIVE_TIMEOUT=30000;self.PING_INTERVAL=900000;self.servers_down_before_notify=1;self.entitlement_token=None;self.encryption=_A;self.socket_timeout_seconds=2;self._subjects={}
	def TDx(self,jPL,history):
		for sRv in jPL:self._subjects[sRv]=history
	def kRI(self,jPL):
		for sRv in jPL:
			try:del self._subjects[sRv]
			except KeyError:pass
	def get_subjects(self):return self._subjects
class dJh:
	FyN='OK';wLA='DENY';ehE='connection_active_close_keep_alive';COe='connection_active_close_seq_higher';gcs='connection_passive_close';UEz='connection_error';pzp='cache_ok';aje='cache_ok_no_new_message';pHn='cache_ok_new_epoch';Ari='end';JTC='^\\/([^\\/]+\\/)*([^\\/]+|\\*)$'
	@staticmethod
	def oDT(UGA):
		if not isinstance(UGA,str):return _A
		Ekj=re.compile(dJh.JTC)
		if Ekj.search(UGA)is not None:return True
		return _A
	@staticmethod
	def MZo(jPL):
		eOQ=[]
		for sRv in jPL:
			if sRv is not None and dJh.oDT(sRv):eOQ.append(sRv)
		return eOQ
	@staticmethod
	def WdE(VMc,recv_seq,recv_seq_id,listener_notifier,logger):
		if VMc.pEN()!=recv_seq_id:VMc.EAr(recv_seq);VMc.Keb(recv_seq_id);return IGb.keW
		if recv_seq<=VMc.get_seq():return IGb.ulp
		if recv_seq==VMc.get_seq()+1:
			if VMc.tcE()==FLh.RaK:VMc.DiG();listener_notifier.on_status(M.NOTIFY_DATA_SYNC,VMc.get_subject())
			VMc.EAr(VMc.get_seq()+1);return IGb.keW
		if VMc.KQQ()>0:logger.info('Missing Messages: expected message with sequence number: '+str(VMc.get_seq()+1)+', received instead message with sequence number:  '+str(recv_seq)+' !');return IGb.jgT
		logger.info("Reset sequence: '"+str(VMc.get_seq()+1)+"'. The new sequence is: '"+str(recv_seq)+"' !");VMc.EAr(recv_seq);listener_notifier.on_status(M.NOTIFY_DATA_RESYNC,VMc.get_subject());return IGb.keW
	@staticmethod
	def xPN(VMc,recv_seq,recv_seq_id):
		if VMc.pEN()!=recv_seq_id:VMc.EAr(recv_seq);VMc.Keb(recv_seq_id);return IGb.keW
		if recv_seq<=VMc.get_seq():return IGb.ulp
		if VMc.tcE()==FLh.RaK:VMc.DiG()
		VMc.EAr(recv_seq);return IGb.keW
from ..migratorydata_client import MigratoryDataClient as M