_A=False
import re
from migratorydata.core.subject import *
class tnn:rNX=0;LFK=1;TxA=2
class LRT:
	def __init__(self,session_type,user_agent):self.nBj=6;self.session_type=session_type;self.user_agent=user_agent+', version:'+str(self.nBj);self.DEFAULT_KEEP_ALIVE_TIMEOUT=30000;self.PING_INTERVAL=900000;self.servers_down_before_notify=1;self.entitlement_token=None;self.encryption=_A;self.socket_timeout_seconds=2;self._subjects={}
	def uQr(self,qFN,history):
		for qpH in qFN:self._subjects[qpH]=history
	def XZx(self,qFN):
		for qpH in qFN:
			try:del self._subjects[qpH]
			except KeyError:pass
	def get_subjects(self):return self._subjects
class QKt:
	VJP='OK';WZU='DENY';AfN='connection_active_close_keep_alive';AVc='connection_active_close_seq_higher';SiV='connection_passive_close';TLp='connection_error';DcN='cache_ok';YJJ='cache_ok_no_new_message';bve='cache_ok_new_epoch';BVP='end';SyG='^\\/([^\\/]+\\/)*([^\\/]+|\\*)$'
	@staticmethod
	def kVP(aii):
		if not isinstance(aii,str):return _A
		fLw=re.compile(QKt.SyG)
		if fLw.search(aii)is not None:return True
		return _A
	@staticmethod
	def LmM(qFN):
		CPw=[]
		for qpH in qFN:
			if qpH is not None and QKt.kVP(qpH):CPw.append(qpH)
		return CPw
	@staticmethod
	def sKa(sOZ,recv_seq,recv_seq_id,listener_notifier,logger):
		if sOZ.Ffz()!=recv_seq_id:sOZ.Gop(recv_seq);sOZ.YZi(recv_seq_id);return tnn.rNX
		if recv_seq<=sOZ.get_seq():return tnn.LFK
		if recv_seq==sOZ.get_seq()+1:
			if sOZ.ugI()==sHL.LPP:sOZ.AYu();listener_notifier.on_status(M.NOTIFY_DATA_SYNC,sOZ.get_subject())
			sOZ.Gop(sOZ.get_seq()+1);return tnn.rNX
		if sOZ.FWl()>0:logger.info('Missing Messages: expected message with sequence number: '+str(sOZ.get_seq()+1)+', received instead message with sequence number:  '+str(recv_seq)+' !');return tnn.TxA
		logger.info("Reset sequence: '"+str(sOZ.get_seq()+1)+"'. The new sequence is: '"+str(recv_seq)+"' !");sOZ.Gop(recv_seq);listener_notifier.on_status(M.NOTIFY_DATA_RESYNC,sOZ.get_subject());return tnn.rNX
	@staticmethod
	def ZmA(sOZ,recv_seq,recv_seq_id):
		if sOZ.Ffz()!=recv_seq_id:sOZ.Gop(recv_seq);sOZ.YZi(recv_seq_id);return tnn.rNX
		if recv_seq<=sOZ.get_seq():return tnn.LFK
		if sOZ.ugI()==sHL.LPP:sOZ.AYu()
		sOZ.Gop(recv_seq);return tnn.rNX
from migratorydata.migratorydata_client import MigratoryDataClient as M