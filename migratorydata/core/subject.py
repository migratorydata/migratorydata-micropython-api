_A=False
class CKs:Twe=0;GiL=1;aEp=2
class zNt:
	fCu='cache_ok';Ufp=2
	def __init__(A,Owg,history):A._subject=Owg;A._history=history;A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=zNt.fCu;A._current_subscribe_type=CKs.Twe
	def get_seq(A):return A._seq
	def MAP(A,VUx):A._seq=VUx;A._messages_recieved_until_recovery+=1
	def GjX(A):return A._seq_id
	def RXI(A,llS):A._seq_id=llS
	def get_subject(A):return A._subject
	def FlP(A):return A._history
	def yJU(A):
		A._messages_recieved_until_recovery=0
		if A.lsr():A._nr_of_consecutive_recoveries+=1
	def sjv(A):A._nr_of_consecutive_recoveries=0
	def pIa(A):return A._messages_recieved_until_recovery
	def QRV(A,status):A._cache_recovery_status=status
	def LFa(A):return A._cache_recovery_status
	def lsr(A):return A._seq_id!=70000
	def DKe(A):
		type=CKs.Twe
		if A.lsr():
			if A._nr_of_consecutive_recoveries>=zNt.Ufp:
				if A._history>0:type=CKs.GiL
			else:type=CKs.aEp
		elif A._history>0:type=CKs.GiL
		if type==CKs.Twe or type==CKs.GiL:A.QRV(zNt.fCu);A.sjv()
		A._current_subscribe_type=type;return type
	def Yji(A):return A._current_subscribe_type
	def PHn(A):A._current_subscribe_type=CKs.Twe
	def aed(A):A._seq=0;A._seq_id=70000;A._need_recovery=_A;A._nr_of_consecutive_recoveries=0;A._messages_recieved_until_recovery=0;A._cache_recovery_status=A.fCu;A._current_subscribe_type=CKs.Twe
	def __repr__(B):C=', ';A='[';A+='Subj = '+str(B._subject)+C;A+='Seq = '+str(B._seq)+C;A+='SeqId = '+str(B._seq_id)+C;A+='NeedRecovery = '+str(B._need_recovery)+C;A+='MessagesReceivedUntilRecovery = '+str(B._messages_recieved_until_recovery)+C;A+='CacheRecoveryStatus = '+str(B._cache_recovery_status)+C;A+='SubsType = '+str(B._current_subscribe_type)+C;A+='NrOfConsecutiveRecovery = '+str(B._nr_of_consecutive_recoveries);A+=']';return A
class RHW:
	def __init__(A):A._subject_table={};A._empty_subject=zNt('',0)
	def oVX(B,ALH,history):
		for A in ALH:
			C=B._subject_table.get(A)
			if C is None:B._subject_table[A]=zNt(A,history)
	def RMl(A,ALH):
		B=[]
		for C in ALH:
			D=A._subject_table.get(C)
			if D is not None:
				try:del A._subject_table[C];B.append(D)
				except KeyError:pass
		return B
	def JQe(A):return A._subject_table.keys()
	def kph(A):return A._subject_table
	def get_subject(A,Owg):return A._subject_table.get(Owg)
	def dqv(A,Owg):
		B=A._subject_table.get(Owg)
		if B is None:return _A
		else:return True
	def eAn(A):return A._empty_subject
	def gTc(A):
		for B in A._subject_table:A._subject_table[B].aed()