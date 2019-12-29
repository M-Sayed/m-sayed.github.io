---
layout: post
last_update_date: Dec 29, 2019
book_notes: false
title: Load balancer VS Reverse Proxy
brief: >-
  What is a load balancer? What's a reverse proxy? And what are the differences between both of them?
---

It happens a lot when these two terms come in front of me, and mostly, I say "Oh, no. I forgot again the difference between both of them!", so here I'm writing what I understand, so it can always be my only reference, and yours definitely if you found it useful. ;)

---

## Load Balancer

Let's imagine you have that application that is becoming too popular, and in a day you get millions of requests headed to your application's server, you notice that over time your server is responding with higher latency and a small throughput compared with that large number of requests, that's definitely going to drive users away from using your app.

Now, you realized that your application can not serve that huge number of requests and you decided to [scale it horizontally](https://en.wikipedia.org/wiki/Scalability#Horizontal), by having multiple servers, but now you have questions, don't you?

  1. How are the clients supposed to communicate with these servers?
  2. How will the load be **distributed/balanced** between these servers?

And here when a Load balancer intervenes to solve the problem - what a super hero. You can simply imagine a load balancer to be an intermediary piece of software - [or hardware](https://en.wikipedia.org/wiki/Load_balancing_(computing)) - that sits between your clients and your servers, the clients will not be communicating directly with your servers any more, instead, they will communicate with your load balancer.

When a client sends a request, the load balancer sends that request to one of your servers, you wonder, which server? I got many, right? The chosen server is determined by which algorithm you're using, and some of these algorithms are:
 1. Random
 2. Round Robin / weighted Round Robin
 3. Least connections / weighted least connections

After we knew what a load balancer really does, let's write down some of its pros & cons:

### Advantages:
1. Your server is no more considered a single point of failure, you got multiple servers running at the same time.
2. It will detect if any of the servers is down and divert the requests away from that server, so your clients get more successful responses.
3. It could be so helpful if your application requires [session persistence](https://www.nginx.com/resources/glossary/session-persistence).

### Disadvantages:
1. Increased complexity
2. One load balancer is considered a single point of failure

---

## Reverse Proxy

Load balancers seem to be really easier to understand, their name (i.e., load balancer) is so descriptive and tells what they mostly do, right? Then, what are reverse proxies? and why they confuse me?

Reverse Proxy is also an intermediary between your server(s) and your clients, but on the other hand, using them doesn't necessarily come with having multiple servers, you can set up a reverse proxy even if you have only one server, a reverse proxy is more like your application's "public face", It allows you to expose your reverse proxy's info to your clients instead of your servers' info, for example, you can expose the reverse proxy's IP address instead of your servers' and that will increase security and protect your servers from malicious clients and DDoS attacks.

Simply, A reverse proxy receives requests from the clients and send them to your servers, and receives responses from your server(s) and send them back to your clients.

### Advantages
1. It increases security
   1. can be used to protect the server from DDoS attacks
2. can be used for web acceleration - reducing the time it takes to generate a response and return it to the client - techniques:
   1. SSL termination
   2. Caching
   3. Compression
3. It can act as a load balancer

### Disadvantages
1. It increases complexity
2. One reverse proxy is a single point of failure.

#### Refs:
there are plenty of great references out there, so glad we have [the Internet](https://youtu.be/iDbyYGrswtg).

1. [https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/](https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/)
2. [https://serverfault.com/a/127022](https://serverfault.com/a/127022)
3. [https://stackoverflow.com/a/28829633/4643970](https://stackoverflow.com/a/28829633/4643970)
4. [https://youtu.be/S8J2fkN2FeI](https://youtu.be/S8J2fkN2FeI)
5. [https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
6. [https://github.com/donnemartin/system-design-primer#load-balancer](https://github.com/donnemartin/system-design-primer#load-balancer)
7. [https://www.jscape.com/blog/load-balancing-algorithms](https://www.jscape.com/blog/load-balancing-algorithms)
8. [https://www.nginx.com/resources/glossary/session-persistence](https://www.nginx.com/resources/glossary/session-persistence)
9. [https://en.wikipedia.org/wiki/Scalability#Horizontal](https://en.wikipedia.org/wiki/Scalability#Horizontal)
10. [https://en.wikipedia.org/wiki/Load_balancing_(computing)](https://en.wikipedia.org/wiki/Load_balancing_(computing))
