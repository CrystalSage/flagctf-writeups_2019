<h1>Web Search Packet Capture Q1 (15)</h1>
<hr>

<h1>Description</h1>
```
All of the questions in this section pertain to the attached packet capture file.
On what website did the user submit search queries? (Give the full URL without the protocol, eg. 2019.flagctf.com)
```
<hr>

Analyzing the pcap file with Wireshark and filtering for GET requests as:
  <p>http.request.method==GET</p>
We get a list of all the search queries. 

Following the TCP stream, it is realized that the queries were submitted from Host: "web.mit.edu"

Thus the flag is :
<p><h3> Flag :web.mit.edu</h3></p>
