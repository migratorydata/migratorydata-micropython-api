from ..migratorydata_client import MigratoryDataLogListener,MigratoryDataLogLevel as LL
class yMm:
	def trace(A,message):0
	def debug(A,message):0
	def info(A,message):0
	def warn(A,message):0
	def error(A,message):0
class NxQ(MigratoryDataLogListener):
	def on_log(C,log,ll):
		B=ll;A=log
		if B==LL.TRACE:print(A)
		elif B==LL.DEBUG:print(A)
		elif B==LL.INFO:print(A)
		elif B==LL.WARN:print(A)
		elif B==LL.ERROR:print(A)
class glw(yMm):
	def __init__(A):A._list=NxQ();A._ll=LL.INFO
	def yqr(A,log_listener,log_level):A._list=log_listener;A._ll=log_level
	def error(A,message):
		if A._ll<=LL.ERROR:A._list.on_log(message,LL.ERROR)
	def trace(A,message):
		if A._ll<=LL.TRACE:A._list.on_log(message,LL.TRACE)
	def debug(A,message):
		if A._ll<=LL.DEBUG:A._list.on_log(message,LL.DEBUG)
	def warn(A,message):
		if A._ll<=LL.WARN:A._list.on_log(message,LL.WARN)
	def info(A,message):
		if A._ll<=LL.INFO:A._list.on_log(message,LL.INFO)