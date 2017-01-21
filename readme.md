# WiPy Rest Server for IOT

The primary goal of this project is to transform a WiPy 1 into a valorous nano Rest Server proposing a confortable api (based on Regular Expression and JSon) to easily control your objects and stuff.

Whatever, this project should also be compatible as-it with the WiPy 2

Nowadays, the WiPy 2 is available on the market... and we have thousands of WiPy 1 boards available on our hacking desk. 
It would be a very good idea to reuse them for various tasks. 

A first demo of the nano Rest Server concept is "irelay". iRelay transforms a quad relay board into "WiFi IoT relay" by using a WiPy.

The WiPy will start a local server to respond to REST request. Request can be issued from a WebBrowser, Curl command line utility, Python code (from a Raspberry-Pi) or even CSharp code.

# About security
As the WiPy 1 does not support TLS and SSL, everything send on the network are done in plain text.

So we recommend:
* To use it on your local/private network.
* To change the login/password to your WiPy. [See our French Tutorial](https://wiki.mchobby.be/index.php?title=Hack-wipy-wlan)
* To use it for project were security will not been an issue.
* To use it for project were hacking could not conduct to injury.
* To use it for project were hacking could not reveal information about private live.
* To not bringing it on the Internet  

# About documentation
All project will be documented at the best with wiring and samples.

Documentation will be found in the __doc__ folder. It will be sub-divised for each project.

Don't hesitate to read the documentation in those folders.

# IP Address
Using a static IP Address can really help in testing the various project.

You can fix the IP within your [__boot.py__](https://wiki.mchobby.be/index.php?title=Hack-wipy-wlan) or with your Internet Box.

In most of our samples, we will use the fixed IP 192.168.1.220   

# Projects available
* __irelay__ : control a Quad relay board with WiPy 1 and REST API

# About installing
Each __doc__ subfolder does contains appropriate installation instruction.

However, you can help yourself in installing the stuffs on your WiPy by using RShell utility.

RShell is [available on GitHub](https://github.com/dhylands/rshell).

We did also write a Frenh tutoriel "[utiliser RShell](https://wiki.mchobby.be/index.php?title=MicroPython-Hack-RShell) on the MCHobby Wiki. 

We did write the small script __rshell-wipy.sh__ to help you in figuring the needed parameter for contacting your WiPy with RShell on the air :-)

# Where to buy
You can find the following products on the MCHobby webshop (shop.mchobby.be)
* [WiPy, LoPy - IoT in Python](https://shop.mchobby.be/68-wipylopy-iot-en-python)
* [4 Relay module](https://shop.mchobby.be/breakout/632-module-quatre-relais-3232100006324.html)<br />[2 Relay module](https://shop.mchobby.be/breakout/507-module-deux-relais-3232100005075-pololu.html)<br />[1 Relay module](https://shop.mchobby.be/breakout/107-module-relais-3232100001077-pololu.html)
