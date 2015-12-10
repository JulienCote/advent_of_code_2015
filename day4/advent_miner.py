#!/usr/bin/python2.7

import hashlib

def validate_key(key):
	return key[:6] == '000000'

hasher = hashlib.md5()
secret_key = 'bgvyzdsv'
answer = 1

hasher.update(secret_key + str(answer))

while not validate_key(hasher.hexdigest()):
	hasher = hashlib.md5()
	answer += 1
	hasher.update(secret_key + str(answer))

print answer
print hasher.hexdigest()






