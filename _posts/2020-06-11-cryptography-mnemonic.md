---
title: "Mnemonic Generation (BIP39) Algorithm"
categories:
  - Hacking
  -
tags:
  - Python
  - Cryptography
---

## Mnemonic Generation (BIP39) Algorithm
Mnemonic a tool that helps you remember an idea or phrase with a pattern of letters.
This article explains the Mnemonic Generation algorithm used for remembering bitcoin, ethereum or many other cryptography wallet secrets. It is also known as BIP39 standard.

It is always very difficult to remember a long hex number. This long hex number  can either be a root secret of a bitcoin wallet or an AES key to decrypt other secrets. Using Mnemonic Generation, we can convert the long hex number string to a Mnemonic and remember (or write down) the Mnemonic instead.


The following python program shows how the Mnemonic Generation algorithm works.

{% highlight python linenos %}
import urllib.request as urllib
import json

# Load the bitcoin BIP39 english word dictionary, total 2048 words
wordListUrl = "https://raw.githubusercontent.com/bitcoinjs/bip39/master/src/wordlists/english.json"
wordlist = list(json.load(urllib.urlopen(wordListUrl)))

# Creates 2 dictionarys
def createDic():
    alphadic = {}  # Maps word as key to int as value
    ralphadic = {}  # Reverses alphadic

    linenumber = 0
    for line in wordlist:
        line = line[:-1]
        alphadic[line] = linenumber
        ralphadic[linenumber] = line
        linenumber += 1

    return alphadic, ralphadic

# Creates a dictionary which can encode
# a hex digit from 0-f to binary representation
# key: (0, 1, 2, ... 9, A, B, C, D, E, F)
# val: (0000, 0001, 0010, ... 1110, 1111)
def createHexToBinDic():
    hex2bin = {}
    for y in range(16):
        if len(str(y).split()) == 2:
            z = 10 + ord(y) - chr("a")
        else:
            z = y
        hex2bin[hex(y)[2:]] = bin(z)[2:]

    for key in hex2bin:
        while len(hex2bin[key]) < 4:
            hex2bin[key] = "0" + hex2bin[key]  # hex2bin[c] = x

    return hex2bin

# let's try with a 256 byte example input
input = """
cf2997d3feda0981ccc4c5c55fcf17c3
ccdc4cbcaa67f4410af4f32eb2452f4e
674c449bb5b5aed3dae1d617c0829868
513dc0824e1a4c67c77c3b8d80281c60
c41afdbfc12c07ca94f3e8fd708b6d6a
551244cb434407c38c7a1976adc0b783
5025f9e1a0734804b5d8069b88d7657b
292dbc3c14351d1b15e3aba0678e2f97
"""

input = input.strip().replace("\n", "")


# mnemonic encoding algorithm, encode a hex number string to mnemonic
def encode(x):
    _, ralphadic = createDic()
    hex2bin = createHexToBinDic()

    binstr = "".join([hex2bin[c] for c in x])

    a = []
    vv = []
    for i in range(0, len(binstr), 11):
        v = binstr[i:i+11]
        if len(v) < 11:
            v += "0" * (11 - len(v))
        vv.append(v)
        a.append(int(v, 2))

    mnemonic = ""
    for q in a:
        mnemonic += ralphadic[q] + " "
    return mnemonic



# mnemonic decoding algorithm, decode a mnemonic string back to the orinal hex number
def decode(s):
    alphadic, _ = createDic()
    l=[]

    for word in s.split():
        w = bin(alphadic[word])[2:]
        a = "0" * (11 - len(w) ) + w
        l.append(a)
    r = "".join(l)
    out = ""
    for i in range(0, len(r), 4):
        out += hex(int(r[i: i + 4], 2))[2:]
    return out

if __name__ == "__main__":
  # TODO: remove the trailing extra 0s
  print((encode(input)))
  print(decode(encode(input)))
{% endhighlight %}
