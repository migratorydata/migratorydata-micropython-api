from ..migratorydata_client import MigratoryDataMessage
class hpI:WLw=0;irW=1;MOw=2;PPc=3
class hbd:
	def __init__(A,operation,wst):A.operation=operation;A.wst=wst
	def __repr__(A):
		D=' - ';B='OPERATION '+str(A.operation)+D;B+='Headers '
		for C in A.wst:E=str(int(C));F=str(A.wst.get(C));B+=E+': '+F+D
		return B
class ETT(MigratoryDataMessage):
	def __init__(A,_subject,_content,closure,retained,_message_type,qos_,_reply_subject,_compression):super().__init__(_subject,_content,closure);A._retained=retained;A._message_type=_message_type;A.laJ=qos_;A._reply_to_subject=_reply_subject;A._compression=_compression
	def EAr(A,OmT):A._seq=OmT
	def kvC(A,epoch):A._epoch=epoch