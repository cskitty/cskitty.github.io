---
title: "Simple Substitution Cipher"
last_modified_at: 2016-03-09T16:20:02-05:00
categories:
  - Hacking
  -
tags:
  - Python
  - Cryptography
---

## Simple Substitution Cipher
Simple Substitution Cipher differs from Caesar Cipher in that the cipher alphabet is not simply shifted, it uses a look up table (the key book) to find the encrypted alphabet.
 

The following python program shows how the Simple Substitution Cipher works.


{% highlight python linenos %}
import random
import copy

key = [chr(y + ord('a')) for y in range(26)]
alphalist = copy.deepcopy(key)
random.shuffle(key)

print("key -", " ".join(key))
def simplecipher(input, encrypt = True):
    global key, alphalist
    d = {}
    for i in range(len(alphalist)):
        if encrypt:
            d[alphalist[i]] = key[i]
        else:
            d[key[i]] = alphalist[i]
    output = ""
    for z in input:
        if z == " ":
            output += " "
        else:
            if z.isupper():
                output += d[z.lower()].upper()
            else:
                output += d[z.lower()]
    return output


plain = "This will be encrypted and decrypted"
ciphertext = simplecipher(plain)
decryptedtext = simplecipher(ciphertext, False)
print('ciphertext =', ciphertext)
print("decryptedtext =", decryptedtext)
{% endhighlight %}
