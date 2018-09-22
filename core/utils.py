import hashlib
import string
import random

def random_key(size=10):
	chars = string.ascii_uppercase + string.digits
	return ''.join(random.choice(chars) for x in range(size))

def generate_hash_key(salt, random_str_size=10):
	random_str = random_key(random_str_size)
	text = random_str + salt
	return hashlib.sha224(text.encode('utf-8')).hexdigest()