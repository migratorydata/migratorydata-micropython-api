_A=None
class QoS:STANDARD=0;GUARANTEED=1
class MessageType:SNAPSHOT=0;UPDATE=1;RECOVERED=2;HISTORICAL=3
class MigratoryDataMessage:
	def __init__(A,_subject,_content,closure=_A,qos=QoS.GUARANTEED,retained=True,reply_subject=_A):A._subject=_subject;A._content=_content;A._closure=closure;A._reply_to_subject=reply_subject;A.NMN=qos;A._retained=retained;A._message_type=MessageType.UPDATE;A._seq=_A;A._epoch=_A;A._compression=_A
	def get_subject(A):return A._subject
	def get_content(A):return A._content
	def get_closure(A):return A._closure
	def get_reply_to_subject(A):return A._reply_to_subject
	def is_retained(A):return A._retained
	def get_seq(A):return A._seq
	def get_epoch(A):return A._epoch
	def get_qos(A):return A.NMN
	def get_message_type(A):return A._message_type
	def is_compressed(A):return A._compression
	def __repr__(B):C=', ';A='[';A+='Subj = '+str(B._subject)+C;A+='Content =  '+str(B._content.decode('utf-8'))+C;A+='Closure =  '+str(B._closure)+C;A+='ReplyToSubject =  '+str(B._reply_to_subject)+C;A+='Retained = '+str(B._retained)+C;A+='QOS = '+B.GIw()+C;A+='MessageType = '+B.Xej()+C;A+='Seq = '+str(B._seq)+C;A+='Epoch = '+str(B._epoch)+' ';A+='Compression = '+str(B._compression)+' ';A+=']';return A
	def GIw(A):
		if A.NMN==QoS.STANDARD:return'STANDARD'
		return'GUARANTEED'
	def Xej(A):
		if A._message_type==MessageType.SNAPSHOT:return'SNAPSHOT'
		if A._message_type==MessageType.UPDATE:return'UPDATE'
		if A._message_type==MessageType.RECOVERED:return'RECOVERED'
		return'HISTORICAL'