# Network Scavenger Hunt

The goal of this activity is to learn to find out how your computer is connected to the internet.

## Beginning Labs
Beginning labs only require a web browser.

### Lab 1: What is my IP address?

Each computer on the internet is assigned its own Internet Protocol Address.  What is the address assigned to your computer?  (Hint: use a search to find a service that tells you what your IP address is).

### Lab 2: What is your WiFi network name?

Each computer that uses WiFi must connect to the network through a WiFi router that has a name?  How can you find out what your WiFi network name is?
(Hint: use a search service to find the instructions for your device: Chrome, Windows, Mac, iPad)

### Lab 3: Who provides your internet connection?

Every IP address is managed by a company that connects this address to the internet.  That company is called your *Internet Services Provider*.

Here is a tool that will help you find your ISP: [https://www.whoismyisp.org/](https://www.whoismyisp.org/)

## Lab 4: How fast is your internet connection?

Look for a program that can test your connection speed.  What is your download and upload speed?  What other information can you find about the time it takes to send a short packet of information back and forth from the server (latency).

## Lab 5: What is your MAC address?

For each network interface in your computer, there is a unique MAC address associated with it. This is called the Media Access Control (MAC) address.  This number is permanently burned into each device when it is manufactured and it is guaranteed to be unique across the internet.

You usually can find MAC addresses in the system settings, general information, or network settings/status of your device. Sometimes the MAC address is printed on a property tag or label so that your organization can track the device.

Here are some instructions on finding the MAC address on your Windows or Mac:
[What's a MAC Address and how do I find it?](https://slts.osu.edu/articles/whats-a-mac-address-and-how-do-i-find-it/)

Note that in this case "MAC" has nothing to do with the Apple Mac operating system!

## Advanced Labs

To do these labs, you will need to access your computer's command shell or Terminal (on the Mac).  If you are running ChromeOS your school may not have the ChromOS shell installed.

### Ping Test Lab

Ping is a useful program that will help you see the time it takes your computer to communicate with a report computer.  It is named after the way that submarines sent out sounds underwater to see what items were near it (sonar).  You can use it to debug network problems.

Search for how to use the "ping" program on your operating systems:

* **How do I run ping on Windows 10"**
* **How do I run ping on a Mac"**
* **How to run a ping test in Chrome OS** (requires ChromOS Shell crosh) [Video](https://www.youtube.com/watch?v=WOIeXlHPoPc) - your school may not have crosh enabled.

For example on the Mac use the Terminal and type "ping -c 10 google.com".  This will measure the time to get from your computer to google.com with a "count" of 10.

```
$ ping -c 10 google.com
PING google.com (142.250.191.142): 56 data bytes
64 bytes from 142.250.191.142: icmp_seq=0 ttl=50 time=47.229 ms
64 bytes from 142.250.191.142: icmp_seq=1 ttl=50 time=52.301 ms
64 bytes from 142.250.191.142: icmp_seq=2 ttl=50 time=43.634 ms
64 bytes from 142.250.191.142: icmp_seq=3 ttl=50 time=51.289 ms
64 bytes from 142.250.191.142: icmp_seq=4 ttl=50 time=51.612 ms
64 bytes from 142.250.191.142: icmp_seq=5 ttl=50 time=51.738 ms
64 bytes from 142.250.191.142: icmp_seq=6 ttl=50 time=48.213 ms
64 bytes from 142.250.191.142: icmp_seq=7 ttl=50 time=46.793 ms
64 bytes from 142.250.191.142: icmp_seq=8 ttl=50 time=56.455 ms
64 bytes from 142.250.191.142: icmp_seq=9 ttl=50 time=52.937 ms

--- google.com ping statistics ---
10 packets transmitted, 10 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 43.634/50.220/56.455/3.522 ms
```

The last column in the list is the time it took to make a round trip in milliseconds.  At the end of the test it will show you the minimum, average, maximum and standard deviation of the 10 trials.  The average of 50.22 is a reasonable number.  This is about 1/20th of a second.

Questions:

1. Why do you think there are variations in the times?
2. What do you think happens if one of the computers connecting your computers goes down? (crashes)

### Traceroute

You can also see the exact route that your computer takes to send data to and from any report system.  This is useful for debugging things when your connection to the internet is down.

```sh
traceroute www.google.com
```

This will show you the times it takes to reach each of the computers between your computers and the destination computer.

Search for "How to use traceroute on Windows/Mac" for more details.