---
title: "Enigma Machine in Python"
categories:
  - Hacking
tags:
  - Python
  - Cryptography
---

## Enigma Machine in Python

The Enigma machines were invented at the end of World War I by German engineer Arthur Scherbius and were mainly used to protect commercial, diplomatic and military communication. Enigma machines became more and more complex and were heavily used by the German army during World War II to encrypt radio signals.

The Enigma machine was used to both encrypt or decrypt Enigma messages (Enigma encryption is symmetric, which means that the same settings can be used to both encrypt or decrypt a message).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg/1024px-Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg)

We will use python to create an enigma encoder program to encrypt and decrypt messages using specific Enigma settings.
The article [here](https://hackaday.com/2017/08/22/the-enigma-enigma-how-the-enigma-machine-worked/) explains the detail of how enigma encoder works.

{% highlight python linenos %}

# ----------------- Enigma Settings -----------------
rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
ringPositions = "DEF"
plugboard = "AT BS DE FM IR KN LZ OW PV XY"
# ---------------------------------------------------

def caesarShift(str, amount):
	output = ""

	for i in range(0,len(str)):
		c = str[i]
		code = ord(c)
		if ((code >= 65) and (code <= 90)):
			c = chr(((code - 65 + amount) % 26) + 65)
		output = output + c

	return output

def encode(plaintext):
  global rotors, reflector,ringSettings,ringPositions,plugboard
  #Enigma Rotors and reflectors
  rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  rotor1Notch = "Q"
  rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  rotor2Notch = "E"
  rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  rotor3Notch = "V"
  rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  rotor4Notch = "J"
  rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotor5Notch = "Z"

  rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3,"IV":rotor4,"V":rotor5}
  rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch,"IV":rotor4Notch,"V":rotor5Notch}  

  reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
  reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}

  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rotorANotch = False
  rotorBNotch = False
  rotorCNotch = False

  if reflector=="UKW-B":
    reflectorDict = reflectorB
  else:
    reflectorDict = reflectorC

  #A = Left,  B = Mid,  C=Right
  rotorA = rotorDict[rotors[0]]
  rotorB = rotorDict[rotors[1]]
  rotorC = rotorDict[rotors[2]]
  rotorANotch = rotorNotchDict[rotors[0]]
  rotorBNotch = rotorNotchDict[rotors[1]]
  rotorCNotch = rotorNotchDict[rotors[2]]

  rotorALetter = ringPositions[0]
  rotorBLetter = ringPositions[1]
  rotorCLetter = ringPositions[2]

{% endhighlight %}
