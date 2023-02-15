_A=False
class FLh:eGV=0;MjB=1;RaK=2
class EAL:
	pzp='cache_ok';sRB=2
	def __init__(A,sRv,history):A._subject=sRv;A._history=history;A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=EAL.pzp;A._current_subscribe_type=FLh.eGV
	def get_seq(A):return A._seq
	def EAr(A,OmT):A._seq=OmT;A._messages_recieved_until_recovery+=1
	def pEN(A):return A._seq_id
	def Keb(A,hnO):A._seq_id=hnO
	def get_subject(A):return A._subject
	def uZy(A):return A._history
	def DUx(A):
		A._messages_recieved_until_recovery=0
		if A.thH():A._nr_of_consecutive_recoveries+=1
	def yuY(A):A._nr_of_consecutive_recoveries=0
	def KQQ(A):return A._messages_recieved_until_recovery
	def fKx(A,status):A._cache_recovery_status=status
	def czA(A):return A._cache_recovery_status
	def thH(A):return A._seq_id!=70000
	def NFG(A):
		type=FLh.eGV
		if A.thH():
			if A._nr_of_consecutive_recoveries>=EAL.sRB:
				if A._history>0:type=FLh.MjB
			else:type=FLh.RaK
		elif A._history>0:type=FLh.MjB
		if type==FLh.eGV or type==FLh.MjB:A.fKx(EAL.pzp);A.yuY()
		A._current_subscribe_type=type;return type
	def tcE(A):return A._current_subscribe_type
	def DiG(A):A._current_subscribe_type=FLh.eGV
	def UzO(A):A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=A.pzp;A._current_subscribe_type=FLh.eGV
	def __repr__(B):C=', ';A='[';A+='Subj = '+str(B._subject)+C;A+='Seq = '+str(B._seq)+C;A+='SeqId = '+str(B._seq_id)+C;A+='NeedRecovery = '+str(B._need_recovery)+C;A+='MessagesReceivedUntilRecovery = '+str(B._messages_recieved_until_recovery)+C;A+='CacheRecoveryStatus = '+str(B._cache_recovery_status)+C;A+='SubsType = '+str(B._current_subscribe_type)+C;A+='NrOfConsecutiveRecovery = '+str(B._nr_of_consecutive_recoveries);A+=']';return A
class Kde:
	def __init__(A):A._subject_table={};A._empty_subject=EAL('',0)
	def TDx(B,jPL,history):
		for A in jPL:
			C=B._subject_table.get(A)
			if C is None:B._subject_table[A]=EAL(A,history)
	def NZR(A,jPL):
		B=[]
		for C in jPL:
			D=A._subject_table.get(C)
			if D is not None:
				try:del A._subject_table[C];B.append(D)
				except KeyError:pass
		return B
	def uJQ(A):return A._subject_table.keys()
	def aVe(A):return A._subject_table
	def get_subject(A,sRv):return A._subject_table.get(sRv)
	def pxR(A,sRv):
		B=A._subject_table.get(sRv)
		if B is None:return _A
		else:return True
	def HER(A):return A._empty_subject
	def reO(A):
		for B in A._subject_table:A._subject_table[B].UzO()