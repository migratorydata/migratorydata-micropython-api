_A=None
import random,socket
class xgZ:
	wOa=80;Qrk=443;IdP=100
	def __init__(A,address,encryption):
		B=address;A._weight=xgZ.IdP;A._unparsed_address=B;F=B.find(' ')
		if F!=-1:
			A._weight=int(B[0:F])
			if A._weight<0 or A._weight>100:raise ValueError('The Weight of a clust Member must be between 0 and 100, Weight: '+str(A._weight))
		G=B.find(']');D=B.rfind(':');E=_A;C=_A
		if D!=-1 and D+1<len(B)and D>=G:E=B[0:D];C=int(B[D+1:])
		else:
			E=B
			if encryption:C=A.Qrk
			else:C=A.wOa
		if C<0 or C>65535:raise ValueError('Invalid Port number')
		if E=='':raise ValueError('Clust Member with null address')
		if E=='*':raise ValueError('Wildcard address (*) cannot be used to define a clust Member')
		A._address=E;A._port=C
	def UNC(A):return A._weight
	def zdG(A):return A._port
	def UlB(A):return A._address
	def Otx(A,UmV):
		if A._address==UmV._address:
			if A._port==UmV._port:return True
		return False
	def Kof(A):return A._unparsed_address
	def __repr__(B):A='[Host=';A+=str(B.UlB());A+=', Port=';A+=str(B.zdG());A+=']';return A
class rtB:
	def __init__(A,servers,encryption):
		B=servers;A._members=[];A._inactive_members=[];A._current_member=_A
		for C in range(0,len(B)):A._members.append(xgZ(B[C],encryption))
	def jhV(A):
		B=A.Mhg()
		if len(B)==0:A._inactive_members=[];B=list(A._members)
		C=A.BAN(B);A._current_member=B[C];return A._current_member
	def Mhg(A):
		B=list(A._members)
		for C in A._members:
			for D in A._inactive_members:
				if C.Otx(D):B.remove(C)
		return B
	def BAN(G,uWA):
		B=uWA;C=-1;A=0
		for E in B:A=A+E.UNC()
		if A==0:C=int(len(B)*random.uniform(0,1))
		else:
			F=int(A*random.uniform(0,1));A=0
			for D in range(0<len(B)):
				A=A+B[D].UNC()
				if A>F:C=D;break
		return C
	def MDy(A):return A._current_member
	def LJU(A,UmV):A._inactive_members.append(UmV)
class eHx:
	@staticmethod
	def jEg(host,kWw,encryption,socket_timeout_seconds):
		A=_A;A=socket.socket(socket.AF_INET,socket.SOCK_STREAM);A.settimeout(socket_timeout_seconds);B=socket.getaddrinfo(host,kWw)[0][-1];A.connect(B)
		if encryption is True:import ussl;A=ussl.wrap_socket(A)
		return A