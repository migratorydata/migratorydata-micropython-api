from migratorydata.migratorydata_listener import *
from migratorydata.migratorydata_message import MigratoryDataMessage
from migratorydata.migratorydata_log_listener import MigratoryDataLogListener
class MigratoryDataClient:
	NOTIFY_SERVER_UP='NOTIFY_SERVER_UP';NOTIFY_SERVER_DOWN='NOTIFY_SERVER_DOWN';NOTIFY_DATA_SYNC='NOTIFY_DATA_SYNC';NOTIFY_DATA_RESYNC='NOTIFY_DATA_RESYNC';NOTIFY_SUBSCRIBE_ALLOW='NOTIFY_SUBSCRIBE_ALLOW';NOTIFY_SUBSCRIBE_DENY='NOTIFY_SUBSCRIBE_DENY';NOTIFY_PUBLISH_OK='NOTIFY_PUBLISH_OK';NOTIFY_PUBLISH_FAILED='NOTIFY_PUBLISH_FAILED';NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED='NOTIFY_MESSAGE_SIZE_LIMIT_EXCEEDED';NOTIFY_PUBLISH_DENIED='NOTIFY_PUBLISH_DENIED';vRo='NOTIFY_CONNECT_OK';emj='NOTIFY_CONNECT_DENY';CONSTANT_WINDOW_BACKOFF='CONSTANT_WINDOW_BACKOFF';TRUNCATED_EXPONENTIAL_BACKOFF='TRUNCATED_EXPONENTIAL_BACKOFF'
	def __init__(self):self._client_impl=kgm()
	def connect(self):self._client_impl.KZd()
	def disconnect(self):self._client_impl.MzQ()
	def set_listener(self,listener):
		if issubclass(type(listener),MigratoryDataListener)is False:raise TypeError('Argument for set_listener must be a subclass MigratoryDataListener')
		self._client_impl.beo(listener)
	def get_listener(self):return self._client_impl.OWO()
	def set_log_listener(self,log_listener,log_level):
		A='Second argument for set_log_level must be a MigratoryDataLogLevel'
		if issubclass(type(log_listener),MigratoryDataLogListener)is False:raise TypeError('First argument for set_log_listener must be a subclass MigratoryDataLogListener')
		if type(log_level)is not int:raise TypeError(A)
		if log_level<0 or log_level>4:raise TypeError(A)
		self._client_impl.Btu(log_listener,log_level)
	def set_entitlement_token(self,entitlement_token):
		if type(entitlement_token)is not str:raise TypeError('Argument for set_entitlement_token must be of type string')
		self._client_impl.ZGh(entitlement_token)
	def set_servers(self,servers):self._check_if_is_string_list(servers,'set_servers');self._client_impl.HBQ(servers)
	def _check_if_is_string_list(self,string_list,method_name):
		B=' must be a list of strings';A='First argument for '
		if type(string_list)is not list:raise TypeError(A+method_name+B)
		for PuM in string_list:
			if type(PuM)is not str:raise TypeError(A+method_name+B)
	def subscribe(self,subject_list):self._check_if_is_string_list(subject_list,'subscribe');self._client_impl.qHc(subject_list,0)
	def subscribe_with_history(self,subject_list,number_of_historical_messages):
		self._check_if_is_string_list(subject_list,'subscribe_with_history')
		if type(number_of_historical_messages)is not int:raise TypeError('Second argument for subscribe_with_history must be of type int')
		self._client_impl.qHc(subject_list,number_of_historical_messages)
	def unsubscribe(self,subject_list):self._check_if_is_string_list(subject_list,'unsubscribe');self._client_impl.sJL(subject_list)
	def publish(self,message):
		if type(message)is not MigratoryDataMessage:raise TypeError('Argument for publish must be of type MigratoryDataMessage')
		self._client_impl.fWt(message)
	def set_encryption(self,encryption_bool):
		if type(encryption_bool)is not bool:raise TypeError('Argument for set_encryption must be of type bool')
		self._client_impl.xBa(encryption_bool)
	def get_subjects(self):return self._client_impl.HDa()
	def check_for_messages(self):return self._client_impl.check_for_messages()
from migratorydata.core.client_impl import kgm