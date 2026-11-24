# Mission 7 — How computers communicate

## 1. Task / objective
Explain basic network concepts, observe DNS and connectivity information safely, and describe what happens when a browser opens a website.

## 2. Work completed

### Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Connects devices across a small area. | Home or campus lab network. |
| MAN | Connects networks across a city or large campus. | City-wide municipal network. |
| WAN | Connects networks across large geographic areas. | The internet. |
| DNS | Finds network addresses associated with a domain name. | Looking up `example.com`. |
| Router | Forwards traffic between networks. | A home router sends traffic toward an internet provider. |
| Protocol | Rules that devices follow to exchange data. | HTTPS for secure web communication. |
| Packet switching | Breaks data into packets that can travel across networks. | Web page data travels in packets. |
| Client-server | A client requests a service and a server responds. | A browser requests a page from a website server. |

### Network observations
- `nslookup example.com` succeeded and returned two IPv4 address records. The local resolver address is omitted; DNS answers can change over time.
- `ping -c 1 example.com` received one reply: 1 packet transmitted, 1 received, 0% packet loss; round-trip time was 13.525 ms.
- A connectivity test helps check whether a remote host responds over the network.
- A DNS lookup displays the domain's resolved network address. DNS lets a browser find a server using a human-readable website name.

### What happens when a website opens
1. The browser acts as a client and reads the website name entered by the user.
2. DNS resolves the name to a network address.
3. The client sends a request using a protocol such as HTTPS, through the local network and router.
4. Routers forward packets toward the server across the WAN.
5. The server processes the request and sends response packets back to the client.
6. The browser reassembles the response and displays the page to the user.

## 3. Commands / tools used
- `nslookup example.com` — looked up DNS records for the example domain.
- `ping -c 1 example.com` — sent one packet and confirmed a reply from the public example host.

## 4. My understanding
DNS maps a name to an address, while routers forward packets between networks. The browser is the client, the website host is the server, and protocols define how their requests and responses are exchanged.

## 5. Difficulties faced
The initial elevated request for the connectivity check was rejected.

## 6. How I resolved them
After authorization, ran the one-packet connectivity check successfully and recorded its result.

## 7. Evidence / files
- This README contains the network concepts, DNS observation and website sequence.

## 8. Commit details
Commit: `Mission 7: Networking`. This mission and its verified connectivity result are included in the simplified published history.
