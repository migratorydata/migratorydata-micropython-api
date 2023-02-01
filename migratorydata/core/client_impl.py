_E='Error: subscribe() - invalid argument; expected a list of valid topics'
_D='Client is already running, Disconnect first'
_C=True
_B=False
_A=None
import sys
from migratorydata.core.network import uxM
from migratorydata.core.connection import Connection
from migratorydata.protocol.push_protocol import rOG
from migratorydata.core.logger import GwG
from migratorydata.core.util import QKt,LRT
class kgm:
	def __init__(A):A._running=_B;A._configuration=_A;A._connection=_A;A._servers=_A;A._migratory_data_listener=_A;A.Eje=rOG.UrT;A.TUm='MigratoryDataClient/v6.0 Python/'+str(sys.version);A._logger=GwG();A._configuration=LRT(A.Eje,A.TUm)
	def KZd(A):
		if A._running is _C:raise RuntimeError('Error: connect() - already connected')
		if A._servers is _A:raise RuntimeError('Error: connect() - no server to connect to; use set_servers() to specify one or more servers')
		if A._migratory_data_listener is _A:raise RuntimeError('Error: connect() - no listener set; use set_listener() to specify a listener handler')
		A._running=_C;D=uxM(A._servers,A._configuration.encryption);A._connection=Connection(A._configuration,A._migratory_data_listener,D,A._logger);A._connection.connect();B=A._configuration.get_subjects()
		for C in B:A._connection.subscribe([C],B[C])
	def HBQ(B,_servers):
		A=_servers
		if B._running is _C:raise RuntimeError('Error: set_servers() - already connected; use this method before connect()')
		if A is _A:raise TypeError('Error: set_servers() - servers has None value')
		if len(A)==0:raise ValueError('Error: set_servers() - The list of servers is empty')
		B._logger.info('Setting Servers to connect to: '+str(A));B._servers=A
	def OWO(A):B=A._migratory_data_listener;return B
	def beo(A,_listener):
		B=_listener
		if A._running is _B:
			if B is _A:raise TypeError('Listener has None value')
			A._migratory_data_listener=B
		else:raise RuntimeError(_D)
	def Btu(A,_log_listener,_log_level):
		if A._running is _B:A._logger.Cgz(_log_listener,_log_level)
		else:raise RuntimeError(_D)
	def MzQ(A):
		A._logger.info('Disposing')
		if A._running is _B:return
		A._running=_B
		if A._connection is not _A:A._connection.MzQ();A._connection=_A
	def ZGh(A,token):
		B=token
		if B is _A or len(B)==0:raise TypeError('Token is null or empty.')
		A._configuration.entitlement_token=B;A._logger.info('Configuring Entitlement token: '+B)
		if A._running is _C:A._connection.ZGG()
	def qHc(B,_subjects,history):
		D=history;A=_subjects
		if A is _A or len(A)==0:raise ValueError(_E)
		for C in A:
			if C is _A or len(C)==0 or QKt.kVP(C)is _B:raise TypeError('Subscribe with invalid qpH: '+str(C))
		if D<0:raise ValueError('Error: subscribeWithHistory() - the argument numberOfHistoricalMessages should be a positive number or zero!')
		B._logger.info('Subscribing to: '+str(A));B._configuration.uQr(A,D)
		if B._running is _C:B._connection.subscribe(A,D)
	def sJL(B,_subjects):
		A=_subjects
		if A is _A or len(A)==0:raise ValueError(_E)
		for C in A:
			if C is _A or len(C)==0 or QKt.kVP(C)is _B:raise TypeError('Unsubscribe with invalid qpH: '+str(C))
		B._logger.info('Unsubscribing from: '+str(A));B._configuration.XZx(A)
		if B._running is _C:B._connection.unsubscribe(A)
	def fWt(C,_message):
		B=_message
		if C._running is _C:
			A=B.get_subject();D=B.get_content()
			if A is _A or len(A)==0 or QKt.kVP(A)is _B:raise TypeError('Msg with invalid subj: '+str(A))
			if D is _A:raise TypeError('Msg with null content')
			C._connection.publish(B)
		else:raise RuntimeError('Error: publish() - not connected; use this method after connect()')
	def xBa(A,_encryption_bool):
		B=_encryption_bool
		if A._running is _B:A._logger.info('Configuring encryption to: '+str(B));A._configuration.encryption=B
		else:raise RuntimeError(_D)
	def WWL(A,nr):
		if A._running is _C:raise RuntimeError('Error: Notify_after_reconnect_retries() - already connected; use this method before connect')
		if nr<1:raise ValueError('Error: Notify_after_reconnect_retries() - invalid argument; expected a positive integer')
		A._configuration.servers_down_before_notify=nr;A._logger.info('Configuring the number of failed connection attempts before sending a notification: '+str(nr))
	def HDa(A):return list(A._configuration.get_subjects().keys())
	def check_for_messages(A):return A._connection.check_for_messages()