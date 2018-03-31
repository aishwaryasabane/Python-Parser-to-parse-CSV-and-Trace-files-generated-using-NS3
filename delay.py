''' PROJECT 2 286
	GROUP NUMBER: 8'''
import re
c=[]
p=[]
b=[]
transmit=[]
receive=[]
MaxDelay = 0
TotalDelay = 0
matchl=[]
matchrec=[]
count=0
#Creating a Dictionary to map Nodelist to IP Addresses
AllNodes = [i for i in range(50)]
s='10.1.1.'
for i in range(1,51):
    b.append(s+str(i))

d=dict(zip(b,AllNodes))
#print(d)

#Performing operations on the Trace file
with open("IP_Trace.tr","r") as f:
	f1=f.read()
	s1=f1.strip()
	#print(s1)
	s2=s1.split("\n")

#Extracting only the packets having "Payload"
for k in s2:
	if k.find("Payload")!=-1:
		p.append(k)
#print("PAYLOAD************",p)

#Seperating the Transmitted and Received packets into separate lists
for item in p:
	if item.startswith("t"):
		transmit.append(item)
	elif item.startswith("r"):
		receive.append(item)
#print("TRANSMIT***********************",transmit)
#print("RECEIVE*************************",receive)
#print(len(transmit))
#print(len(receive))

#Matching the Source IP, Dest IP and id using regular expressions and normal conditions
for a in transmit:
	if ("/Tx(1)" in a):
		match=re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}',a)
		#match1=re.search(r'SequenceNumber: \d{1,2}',a)
		match2=re.search(r'id \d{1,}', a)
		#match3=re.search(r'/\w*?\((\d)\)',a)
		'''if "/Tx(0)" in a:	
		print(a)'''	
		#print(match3.group(0))
        	#print(match1,match,match2)
		#print(a.find("/Tx(0)"))

		if match and match2:		
			matchl.append(a)
		#print(ct)
		#print(matchl)	
			Transmit_Time = re.findall(r't(.*?)/',a)
			
			#print(ct)
			#print(Transmit_Time[0])
        		IP = match.group(0).split('>')
        		sourceIP = IP[0].strip()
			'''if sourceIP:
				ct+=1	
			print(sourceIP)'''
			#print(ct)
        		string = "/NodeList/" + str(d[sourceIP])
			'''if string:
				ct+=1	'''
			#print(string)
                	#print(IP,sourceIP)
			#print(ct)
        		if string in a: 
            			destinationIP = IP[1].strip()
            			#seqNumber = match1.group(0).split(': ')
            			#seqNumber = seqNumber[1]
            			srcid = match2.group(0).split(' ')
            			srcid = srcid[1]
                        	#print(IP,sourceIP,destinationIP,srcid)

            			for rec in receive:
					#print(len(recv))
					if ("/Rx(1)" in rec):
               					string = "/NodeList/" + str(d[destinationIP])
                				if string in rec:
                    					match = re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}', rec)
                    					#match1 = re.search(r'SeqNumber=\d{1,2}',rec)
                    					match2 = re.search(r'id \d{1,}',rec)
                                        		#print(match,match2)
					
                    					if match and match2:
								'''matchrec.append(rec)
								ct+=1
							print(matchrec)
							print(ct)'''
                        					Receive_Time = re.findall(r'r(.*?)/',rec)
								#print(Receive_Time[0])
                        					IP = match.group(0).split('>')
                        					rcvsourceIP = IP[0].strip()
                        					rcvdestIP = IP[1].strip()
                        					#rcv_seqnum = match1.group(0).split('=')
                        					#rcv_seqnum = rcv_seqnum[1]
                        					destid = match2.group(0).split(' ')
                        					destid = destid[1]
                                                		#print(IP,rcvsourceIP,rcvdestIP,destid)
					
                        					if sourceIP == rcvsourceIP and destinationIP == rcvdestIP and srcid == destid:
									count+=1
									print("The TOTAL PACKETS are:",count)
                            						if float(Transmit_Time[0]) < float(Receive_Time[0]):
										
										#print(count)
                                                        			#print(Transmit_Time[0],Receive_Time[0])
                                						delay = float(Receive_Time[0]) - float(Transmit_Time[0])
										c.append(delay)
         									
                                						TotalDelay = TotalDelay + delay
										#print("TOTAL DELAY",TotalDelay)
									
                                						#PacketsTransmitted_Total +=1
										
 										#print(PacketsTransmitted_Total)
                               	 						if MaxDelay < delay:
											#count+=1
                                    							MaxDelay = delay
                                						
										receive.remove(rec)
										#print(rec)
                                						break
										#print(Delay)
										#print(count) 
        			
		else: break   					

#print(PacketsTransmitted_Total)
AverageDelay = TotalDelay / count
#print(AverageDelay)
#printing the values of average and maximum delay
print('The AVERAGE DELAY is {}'.format(AverageDelay))
print('The MAXIMUM DELAY is {}'.format(MaxDelay))
#print('The TOTAL DELAY is {}'.format(TotalDelay))

#r 19.1814 /NodeList/13/$ns3::Ipv4L3Protocol/Rx(1) ns3::Ipv4Header (tos 0x0 DSCP Default ECN Not-ECT ttl 64 id 13 protocol 17 offset (bytes) 0 flags [none] length: 1028 10.1.1.13 > 10.1.1.2) ns3::UdpHeader (length: 1008 49154 > 9) Payload (size=1000)
#t 19.1814 /NodeList/13/$ns3::Ipv4L3Protocol/Tx(1) ns3::Ipv4Header (tos 0x0 DSCP Default ECN Not-ECT ttl 63 id 13 protocol 17 offset (bytes) 0 flags [none] length: 1028 10.1.1.13 > 10.1.1.2) ns3::UdpHeader (length: 1008 49154 > 9) Payload (size=1000)
