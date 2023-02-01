from ..migratorydata_client import MigratoryDataMessage
class EEk:plR=0;rhh=1;dsE=2;kmw=3
class TeB:
	def __init__(A,operation,xZU):A.operation=operation;A.xZU=xZU
	def __repr__(A):
		D=' - ';B='OPERATION '+str(A.operation)+D;B+='Headers '
		for C in A.xZU:E=str(int(C));F=str(A.xZU.get(C));B+=E+': '+F+D
		return B
class mka(MigratoryDataMessage):
	def __init__(A,_subject,_content,closure,retained,_message_type,qos_,_reply_subject,_compression):super().__init__(_subject,_content,closure);A._retained=retained;A._message_type=_message_type;A.aGP=qos_;A._reply_to_subject=_reply_subject;A._compression=_compression
	def MAP(A,VUx):A._seq=VUx
	def ogf(A,epoch):A._epoch=epoch