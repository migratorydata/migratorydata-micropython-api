_A=None
class MigratoryDataListener:
	def on_message(A,message):0
	def on_status(A,status,info):0
class MigratoryDataLogLevel:TRACE=0;DEBUG=1;INFO=2;WARN=3;ERROR=4
class MigratoryDataLogListener:
	def __init__(A):0
	def on_log(A,log,migratory_data_log_level):0
class QoS:STANDARD=0;GUARANTEED=1
class MessageType:SNAPSHOT=0;UPDATE=1;RECOVERED=2;HISTORICAL=3
class MigratoryDataMessage:
	def __init__(A,_subject,_content,closure=_A,qos=QoS.GUARANTEED,retained=True,reply_subject=_A):A._subject=_subject;A._content=_content;A._closure=closure;A._reply_to_subject=reply_subject;A.laJ=qos;A._retained=retained;A._message_type=MessageType.UPDATE;A._seq=_A;A._epoch=_A;A._compression=_A
	def get_subject(A):return A._subject
	def get_content(A):return A._content
	def get_closure(A):return A._closure
	def get_reply_to_subject(A):return A._reply_to_subject
	def is_retained(A):return A._retained
	def get_seq(A):return A._seq
	def get_epoch(A):return A._epoch
	def get_qos(A):return A.laJ
	def get_message_type(A):return A._message_type
	def is_compressed(A):return A._compression
	def __repr__(B):C=', ';A='[';A+='Subj = '+str(B._subject)+C;A+='Content =  '+str(B._content.decode('utf-8'))+C;A+='Closure =  '+str(B._closure)+C;A+='ReplyToSubject =  '+str(B._reply_to_subject)+C;A+='Retained = '+str(B._retained)+C;A+='QOS = '+B.vfH()+C;A+='MessageType = '+B.Kwe()+C;A+='Seq = '+str(B._seq)+C;A+='Epoch = '+str(B._epoch)+' ';A+='Compression = '+str(B._compression)+' ';A+=']';return A
	def vfH(A):
		if A.laJ==QoS.STANDARD:return'STANDARD'
		return'GUARANTEED'
	def Kwe(A):
		if A._message_type==MessageType.SNAPSHOT:return'SNAPSHOT'
		if A._message_type==MessageType.UPDATE:return'UPDATE'
		if A._message_type==MessageType.RECOVERED:return'RECOVERED'
		return'HISTORICAL'
class MigratoryDataClient:
	NOTIFY_SERVER_UP='NOTIFY_SERVER_UP';NOTIFY_SERVER_DOWN='NOTIFY_SERVER_DOWN';NOTIFY_DATA_SYNC='NOTIFY_DATA_SYNC';NOTIFY_DATA_RESYNC='NOTIFY_DATA_RESYNC';NOTIFY_SUBSCRIBE_ALLOW='NOTIFY_SUBSCRIBE_ALLOW';NOTIFY_SUBSCRIBE_DENY='NOTIFY_SUBSCRIBE_DENY';NOTIFY_PUBLISH_OK='NOTIFY_PUBLISH_OK';NOTIFY_PUBLISH_FAILED='NOTIFY_PUBLISH_FAILED';NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED='NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED';NOTIFY_PUBLISH_DENIED='NOTIFY_PUBLISH_DENIED';oOZ='NOTIFY_CONNECT_OK';FtS='NOTIFY_CONNECT_DENY'
	def __init__(A):A._client_impl=DKl()
	def connect(A):A._client_impl.diz()
	def disconnect(A):A._client_impl.wuR()
	def set_listener(B,listener):
		A=listener
		if issubclass(type(A),MigratoryDataListener)is False:raise TypeError('Argument for set_listener must be a subclass MigratoryDataListener')
		B._client_impl.sFE(A)
	def get_listener(A):return A._client_impl.LNQ()
	def set_log_listener(D,log_listener,log_level):
		C='Second argument for set_log_level must be a MigratoryDataLogLevel';B=log_listener;A=log_level
		if issubclass(type(B),MigratoryDataLogListener)is False:raise TypeError('First argument for set_log_listener must be a subclass MigratoryDataLogListener')
		if type(A)is not int:raise TypeError(C)
		if A<0 or A>4:raise TypeError(C)
		D._client_impl.jTy(B,A)
	def set_entitlement_token(B,entitlement_token):
		A=entitlement_token
		if type(A)is not str:raise TypeError('Argument for set_entitlement_token must be of type string')
		B._client_impl.dkK(A)
	def set_servers(A,servers):B=servers;A._check_if_is_string_list(B,'set_servers');A._client_impl.mPh(B)
	def _check_if_is_string_list(F,string_list,method_name):
		D=' must be a list of strings';C='First argument for ';B=method_name;A=string_list
		if type(A)is not list:raise TypeError(C+B+D)
		for E in A:
			if type(E)is not str:raise TypeError(C+B+D)
	def subscribe(A,subject_list):B=subject_list;A._check_if_is_string_list(B,'subscribe');A._client_impl.UdY(B,0)
	def subscribe_with_history(A,subject_list,number_of_historical_messages):
		C=number_of_historical_messages;B=subject_list;A._check_if_is_string_list(B,'subscribe_with_history')
		if type(C)is not int:raise TypeError('Second argument for subscribe_with_history must be of type int')
		A._client_impl.UdY(B,C)
	def unsubscribe(A,subject_list):B=subject_list;A._check_if_is_string_list(B,'unsubscribe');A._client_impl.WNG(B)
	def publish(B,message):
		A=message
		if type(A)is not MigratoryDataMessage:raise TypeError('Argument for publish must be of type MigratoryDataMessage')
		B._client_impl.wmj(A)
	def set_encryption(A,encryption_bool):
		if type(encryption_bool)is not bool:raise TypeError('Feature not supported.')
	def get_subjects(A):return A._client_impl.RdO()
	def check_for_messages(A):return A._client_impl.check_for_messages()
from .core.client_impl import DKl