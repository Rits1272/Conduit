import random
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits

def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
	'''
	This function simply generates a random string of length size(here 6).
	'''
	return ''.join(random.choice(chars) for _ in range(size))

	