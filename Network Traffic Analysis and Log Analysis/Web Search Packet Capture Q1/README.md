<h1>Web Search Packet Capture Q1 (15)</h1>
<hr>

<h1>Description</h1>
> Pardon my French
<hr>

Analyzing the pcap file with Wireshark and filtering for GET requests as:
  <p>http.request.method==GET</p>
We get a list of all the search queries. 

Following the TCP stream, it is realized that the queries were submitted from Host: "web.mit.edu"

Thus the flag is :
<p><h3> Flag :web.mit.edu</h3></p>
