# Computer-Security-CW2
Computer Security CW2

In this coursework I touch upon a number of security-related topics, namely encrypting and decrypting with
GPG, spoofing the sender of an email and performing a MitM attack(Man in the Middle attack). Full specifiactions can be found at cw2.pdf

Part 1: Use GPG for day-to-day usage, most importantly including signing and verifying signature. In addition to that, I encrypt and decrypt messages received through email.  

Part 2 : Send a spoofed email to cw-2@ed.ac.uk

Command is : mailx -r darth.vader@starwars.com -s "s1813106" cw-2@ed.ac.uk [CTRL + D]

Part 3: I perform a MitM attack. The scenario is : When Alice and Bob hear about encryption, they immediately set out to implement an encrypted chat client so that
they are sure no one eavesdrops their intimate discussions. They decide to use AES6 to encrypt their messages, since everyone says it’s the best. They also hear of the Diffie-Hellman key exchange (DHKE) and figure it would be cool to use a new secret key for AES every time they connect. Unfortunately Alice and Bob overlooked a fatal flaw: When communicating over the internet (or even locally), one cannot know with certainty that they are speaking to the intended party, at least not without using some form of cryptographic authentication.
