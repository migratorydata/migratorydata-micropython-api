from migratorydata.migratorydata_message import MigratoryDataMessage
class xST:Rot=0;Gfy=1;vUz=2;gYT=3
class vYC:
	def __init__(A,operation,axu):A.operation=operation;A.axu=axu
	def __repr__(A):
		D=' - ';B='OPERATION '+str(A.operation)+D;B+='Headers '
		for C in A.axu:E=str(int(C));F=str(A.axu.get(C));B+=E+': '+F+D
		return B
class SIq(MigratoryDataMessage):
	def __init__(A,_subject,_content,closure,retained,_message_type,qos_,_reply_subject,_compression):super().__init__(_subject,_content,closure);A._retained=retained;A._message_type=_message_type;A.NMN=qos_;A._reply_to_subject=_reply_subject;A._compression=_compression
	def Gop(A,HxA):A._seq=HxA
	def TwH(A,epoch):A._epoch=epoch