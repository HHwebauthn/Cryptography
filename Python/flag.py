import binascii
import base64
import random
import sys

#-----------------
# Binary decoding
#-----------------

with open("binary.txt", "rb") as binary_file:
	data = binary_file.read()
	message = data 
	binary_message = message.decode('utf-8')
	binary_values = binary_message.split(" ")
	ascii_string = " "
	for binary_values in binary_values:
		an_integer = int(binary_values, 2)
		ascii_character = chr(an_integer)
		ascii_string += ascii_character

print(ascii_string)

print("\n End of binaray message\n")
print("\n\n\n")


#-----------------
# HexDecoder
#-----------------
print("Hex message\n\n")

def decode_64(base64_flag):

	decode = base64_flag
	data = base64.b64decode(decode + "==")
	print(data)


decode_64("TmV3IGNoYWxsZW5nZSEgQ2FuIHlvdSBmaWd1cmUgb3V0IHdoYXQncyBnb2luZyBvbiBoZXJlPyBJdCBsb29rcyBsaWtlIHRoZSBsZXR0ZXJzIGFyZSBzaGlmdGVkIGJ5IHNvbWUgY29uc3RhbnQuIChoaW50OiB5b3UgbWlnaHQgd2FudCB0byBzdGFydCBsb29raW5nIHVwIFJvbWFuIHBlb3BsZSkuCmt2YnNxcmQsIGl5ZSdibyBrdnd5Y2QgZHJvYm8hIFh5ZyBweWIgZHJvIHBzeGt2IChreG4gd2tpbG8gZHJvIHJrYm5vY2QuLi4pIHprYmQ6IGsgY2VsY2RzZGVkc3l4IG1zenJvYi4gU3ggZHJvIHB5dnZ5Z3N4cSBkb2hkLCBTJ2ZvIGRrdW94IHdpIHdvY2NrcW8ga3huIGJvenZrbW9uIG9mb2JpIGt2enJrbG9kc20gbXJrYmttZG9iIGdzZHIgayBteWJib2N6eXhub3htbyBkeSBrIG5zcHBvYm94ZCBtcmtia21kb2IgLSB1eHlneCBrYyBrIGNlbGNkc2RlZHN5eCBtc3pyb2IuIE1reCBpeWUgcHN4biBkcm8gcHN4a3YgcHZrcT8gcnN4ZDogR28gdXh5ZyBkcmtkIGRybyBwdmtxIHNjIHF5c3hxIGR5IGxvIHlwIGRybyBweWJ3a2QgZWRwdmtxey4uLn0gLSBncnNtciB3b2t4YyBkcmtkIHNwIGl5ZSBjb28gZHJrZCB6a2Rkb2J4LCBpeWUgdXh5ZyBncmtkIGRybyBteWJib2N6eXhub3htb2MgcHliIGUsIGQsIHAsIHYgaywga3huIHEga2JvLiBJeWUgbWt4IHpieWxrbHZpIGd5YnUgeWVkIGRybyBib3drc3hzeHEgbXJrYmttZG9iYyBsaSBib3p2a21zeHEgZHJvdyBreG4gc3hwb2Jic3hxIG15d3d5eCBneWJuYyBzeCBkcm8gT3hxdnNjciB2a3hxZWtxby4gS3h5ZHJvYiBxYm9rZCB3b2RyeW4gc2MgZHkgZWNvIHBib2Flb3htaSBreGt2aWNzYzogZ28gdXh5ZyBkcmtkICdvJyBjcnlnYyBleiB3eWNkIHlwZG94IHN4IGRybyBrdnpya2xvZCwgY3kgZHJrZCdjIHpieWxrbHZpIGRybyB3eWNkIG15d3d5eCBtcmtia21kb2Igc3ggZHJvIGRvaGQsIHB5dnZ5Z29uIGxpICdkJywga3huIGN5IHl4LiBZeG1vIGl5ZSB1eHlnIGsgcG9nIG1ya2JrbWRvYmMsIGl5ZSBta3ggc3hwb2IgZHJvIGJvY2QgeXAgZHJvIGd5Ym5jIGxrY29uIHl4IG15d3d5eCBneWJuYyBkcmtkIGNyeWcgZXogc3ggZHJvIE94cXZzY3Igdmt4cWVrcW8uCnJnaG54c2RmeXNkdGdodSEgcWdmIGlzYWsgY3RodHVpa2UgZGlrIHprbnRoaGt4IHJ4cWxkZ254c2xpcSByaXN5eWtobmsuIGlreGsgdHUgcyBjeXNuIGNneCBzeXkgcWdmeCBpc3hlIGtjY2d4ZHU6IGZkY3lzbntoMHZfZGk0ZHVfdmk0ZF90X3I0eXlfcnhxbGQwfS4gcWdmIHZ0eXkgY3RoZSBkaXNkIHMgeWdkIGdjIHJ4cWxkZ254c2xpcSB0dSBwZnVkIHpmdHlldGhuIGdjYyBkaXR1IHVneGQgZ2MgenN1dHIgYmhndnlrZW5rLCBzaGUgdGQgeGtzeXlxIHR1IGhnZCB1ZyB6c2Ugc2Nka3ggc3l5LiBpZ2xrIHFnZiBraHBncWtlIGRpayByaXN5eWtobmsh")

print("\n End of Hex message\n")

print("\n\n\n")

#---------------
# caeser cipher
#---------------


# def encrypt(text,s):
# 	result = ""
# 	# transverse the plain text
# 	for i in range(len(text)):
# 		char = text[i]
# 		# Encrypt uppercase characters in plain text
# 		if (char.isupper()):
# 			result += chr((ord(char) + s-65) % 26 + 65)
# 		# Encrypt lowercase characters in plain text
# 		else:
# 			result += chr((ord(char) + s - 97) % 26 + 97)
# 		return result
# #check the above function

# text = ("nkvbsqrd, iye'bo kvwycd drobo! Xyg pyb dro psxkv (kxn wkilo dro rkbnocd...) zkbd: k celcdsdedsyx mszrob. Sx dro pyvvygsxq dohd, S'fo dkuox wi wocckqo kxn bozvkmon ofobi kvzrklodsm mrkbkmdob gsdr k mybboczyxnoxmo dy k nsppoboxd mrkbkmdob - uxygx kc k celcdsdedsyx mszrob. Mkx iye psxn dro psxkv pvkq? rsxd: Go uxyg drkd dro pvkq sc qysxq dy lo yp dro pybwkd edpvkq{...} - grsmr wokxc drkd sp iye coo drkd zkddobx, iye uxyg grkd dro mybboczyxnoxmoc pyb e, d, p, v k, kxn q kbo. Iye mkx zbylklvi gybu yed dro bowksxsxq mrkbkmdobc li bozvkmsxq drow kxn sxpobbsxq mywwyx gybnc sx dro Oxqvscr vkxqekqo. Kxydrob qbokd wodryn sc dy eco pboaeoxmi kxkvicsc: go uxyg drkd 'o' crygc ez wycd ypdox sx dro kvzrklod, cy drkd'c zbylklvi dro wycd mywwyx mrkbkmdob sx dro dohd, pyvvygon li 'd', kxn cy yx. Yxmo iye uxyg k pog mrkbkmdobc, iye mkx sxpob dro bocd yp dro gybnc lkcon yx mywwyx gybnc drkd cryg ez sx dro Oxqvscr vkxqekqo.\nrghnxsdfysdtghu! qgf isak cthtuike dik zknthhkx rxqldgnxsliq risyykhnk. ikxk tu s cysn cgx syy qgfx isxe kccgxdu: fdcysn{h0v_di4du_vi4d_t_r4yy_rxqld0}. qgf vtyy cthe disd s ygd gc rxqldgnxsliq tu pfud zftyethn gcc ditu ugxd gc zsutr bhgvykenk, she td xksyyq tu hgd ug zse scdkx syy. iglk qgf khpgqke dik risyykhnk!")
# s = 1
# text.upper()
# print("Plain Text : " + text)
# print("Shift pattern : " + str(s))
# print ("Cipher: " + encrypt(text,s))


#-----------------
# alphabet cipher
#-----------------


# flag = "vtsoid{x0l_ty4tk_ly4t_j_h4oo_hngbt0}" 

# enycpt_key = 'iphuasdyjefomxwbcnktvqlrgz'
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# utflag{x0w_th4ts_wh4t_i_c4ll_crybt0}

# utflag
# vtsoid




# import random, sys

# LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def main():
# 	message = ''
# 	if len(sys.argv) > 1:
# 		with open(sys.argv[1], 'r') as f:
# 			message = f.read()
# 	else:
# 		message = input("Enter your message: ")
# 	mode = raw_input("E for Encrypt, D for Decrypt: ")
# 	key = ''
   
# 	while checkKey(key) is False:
# 		key = input("Enter 26 ALPHA key (leave blank for random key): ")
# 		if key == '':
# 			key = getRandomKey()
# 		if checkKey(key) is False:
# 			print('There is an error in the key or symbol set.')
# 	translated = translateMessage(message, key, mode)
# 	print('Using key: %s' % (key))
# 	if len(sys.argv) > 1:
# 		fileOut = 'enc.' + sys.argv[1]
# 		with open(fileOut, 'w') as f:
# 			f.write(translated)
# 		print('Success! File written to: %s' % (fileOut))
# 	else: print('Result: ' + translated)

# # Store the key into list, sort it, convert back, compare to alphabet.
# def checkKey(key):
# 	keyString = ''.join(sorted(list(key)))
# 	return keyString == LETTERS
# def translateMessage(message, key, mode):
# 	translated = ''
# 	charsA = LETTERS
# 	charsB = key
# 	# If decrypt mode is detected, swap A and B
# 	if mode == 'D':
# 		charsA, charsB = charsB, charsA
# 	for symbol in message:
# 		if symbol.upper() in charsA:
# 			symIndex = charsA.find(symbol.upper())
# 			if symbol.isupper():
# 				translated += charsB[symIndex].upper()
# 			else:
# 				translated += charsB[symIndex].lower()

# 			# else:
# 				translated += symbol
# 				return translated
# def getRandomKey():
# 	randomList = list(LETTERS)
# 	random.shuffle(randomList)
# 	return ''.join(randomList)
# if __name__ == '__main__':
# 	main()