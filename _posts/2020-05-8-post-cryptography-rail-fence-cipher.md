---
title: "Rail-fence Cipher"
categories:
  - Hacking
  -
tags:
  - Python
  - Cryptography
---

## Rail-fence Cipher
The rail fence cipher is a very simple cipher. It transposes the plaintext to form the cipher text. It can be combined with other ciphers, such as a substitution cipher, the combination of which is more difficult to break than either cipher on it's own.

The cipher is essentially a write down the columns, read along the rows cipher. This is equivalent to using an un-keyed columnar transposition cipher.

### Example 
The key for the railfence cipher is just the number of rails. To encrypt a piece of text, e.g.

Bunnies are awesome  
We write it out in a special way on a number of rails (the key here is 3)

```
B . . . i . . . a . . . a . . . o . .   
. u . n . e .   . r .   . w . s . m .
. . n . . . s . . . e . . . e . . . e
```

The cipher text is read off along the rows:

Biaaoune r wsmnseee

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
