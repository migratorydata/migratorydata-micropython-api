_A=False
class sHL:JOu=0;CUr=1;LPP=2
class Kyl:
	DcN='cache_ok';AgO=2
	def __init__(A,qpH,history):A._subject=qpH;A._history=history;A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=Kyl.DcN;A._current_subscribe_type=sHL.JOu
	def get_seq(A):return A._seq
	def Gop(A,HxA):A._seq=HxA;A._messages_recieved_until_recovery+=1
	def Ffz(A):return A._seq_id
	def YZi(A,akk):A._seq_id=akk
	def get_subject(A):return A._subject
	def Ckb(A):return A._history
	def WWj(A):
		A._messages_recieved_until_recovery=0
		if A.fcX():A._nr_of_consecutive_recoveries+=1
	def DyP(A):A._nr_of_consecutive_recoveries=0
	def FWl(A):return A._messages_recieved_until_recovery
	def qHo(A,status):A._cache_recovery_status=status
	def wlz(A):return A._cache_recovery_status
	def fcX(A):return A._seq_id!=70000
	def qsb(A):
		type=sHL.JOu
		if A.fcX():
			if A._nr_of_consecutive_recoveries>=Kyl.AgO:
				if A._history>0:type=sHL.CUr
			else:type=sHL.LPP
		elif A._history>0:type=sHL.CUr
		if type==sHL.JOu or type==sHL.CUr:A.qHo(Kyl.DcN);A.DyP()
		A._current_subscribe_type=type;return type
	def ugI(A):return A._current_subscribe_type
	def AYu(A):A._current_subscribe_type=sHL.JOu
	def yGk(A):A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=A.DcN;A._current_subscribe_type=sHL.JOu
	def __repr__(B):C=', ';A='[';A+='Subj = '+str(B._subject)+C;A+='Seq = '+str(B._seq)+C;A+='SeqId = '+str(B._seq_id)+C;A+='NeedRecovery = '+str(B._need_recovery)+C;A+='MessagesReceivedUntilRecovery = '+str(B._messages_recieved_until_recovery)+C;A+='CacheRecoveryStatus = '+str(B._cache_recovery_status)+C;A+='SubsType = '+str(B._current_subscribe_type)+C;A+='NrOfConsecutiveRecovery = '+str(B._nr_of_consecutive_recoveries);A+=']';return A
class rhz:
	def __init__(A):A._subject_table={};A._empty_subject=Kyl('',0)
	def uQr(B,qFN,history):
		for A in qFN:
			C=B._subject_table.get(A)
			if C is None:B._subject_table[A]=Kyl(A,history)
	def jyu(A,qFN):
		B=[]
		for C in qFN:
			D=A._subject_table.get(C)
			if D is not None:
				try:del A._subject_table[C];B.append(D)
				except KeyError:pass
		return B
	def lwg(A):return A._subject_table.keys()
	def wCp(A):return A._subject_table
	def get_subject(A,qpH):return A._subject_table.get(qpH)
	def QxT(A,qpH):
		B=A._subject_table.get(qpH)
		if B is None:return _A
		else:return True
	def mXW(A):return A._empty_subject
	def jNL(A):
		for B in A._subject_table:A._subject_table[B].yGk()