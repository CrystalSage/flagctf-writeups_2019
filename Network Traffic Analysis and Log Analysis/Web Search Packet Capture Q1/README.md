# Web Search Packet Capture Q1 (15)

## Description
```
All of the questions in this section pertain to the attached packet capture file.
On what website did the user submit search queries? (Give the full URL without the protocol, eg. 2019.flagctf.com)
```



Analyzing the [pcap file](https://github.com/CrystalSage/flagctf-writeups_2019/blob/master/Network%20Traffic%20Analysis%20and%20Log%20Analysis/Web%20Search%20Packet%20Capture%20Q1/WebSearchingFlagCTF2019.pcapng) with Wireshark and filtering for GET requests as:
  <p>http.request.method==GET</p>
We get a list of all the search queries. 

Following the TCP stream, it is realized that the queries were submitted from Host: "web.mit.edu"

Thus the flag is :
<p><h3> Flag :web.mit.edu</h3></p>
