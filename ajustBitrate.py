import dpkt

def modifyNextTimeStamp(pcap, writer, currentTime, bps):

    for ts, buff in pcap:

        ts = currentTime
        writer.writepkt(buff, ts)

        advancement = len(buff) / bps
        if len(buff)==0:
            pass
        return currentTime + advancement
    return currentTime * -1


def main(pcapFileName, outputPcap, startBPS, aimBPS, duration, increments):
    currentBPS = startBPS
    relitiveTime=0
    nextIncrement=duration

    pcapRawFile = open(pcapFileName,'rb')
    pcapData = dpkt.pcap.Reader(pcapRawFile)
    faralong=0
    while currentBPS < aimBPS:
        while relitiveTime < nextIncrement:
            relitiveTime = modifyNextTimeStamp(pcapData, outputPcap, relitiveTime, currentBPS)
            if relitiveTime < 0:
                pcapRawFile.close()
                pcapRawFile = open(pcapFileName,'rb')
                pcapData = dpkt.pcap.Reader(pcapRawFile)

                relitiveTime=relitiveTime * -1

        faralong += 1
        print(" you have compleated " + faralong + "hours")

        currentBPS = nextIncrement
        nextIncrement += duration
        currentBPS += increments
    pcapRawFile.close()



if __name__=='__main__':
    pcapEmptyFile = open("theBigYin.pcap",'wb')
    writer = dpkt.pcap.Writer(pcapEmptyFile)
    main("test.pcap", writer, 65536,(1*1024*1024),  (60*60), 8192)


#aim bytes per second
# bytes per second = bytes / time 
# bytes / bytes per second = time