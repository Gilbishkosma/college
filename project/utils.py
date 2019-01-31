import re

def validate_password(password):
	if len(password)<6:
		return False,'Password should be at least 6 characters long'
	if not any(char.isdigit() for char in password):
		return False,'Password should contain at least one digit'
	return True,''

def get_error(form):
	errors=dict(form.errors)
	key=tuple(errors.keys())[0]
	error=errors[key]
	key_replace_regex=(r'((non_field_errors)|(__all__))')
	key_replace_regex=re.compile(key_replace_regex)
	key=re.sub(key_replace_regex,'',key)
	if isinstance(error,(tuple,list)):
		return ((key +' : ') if key else '')+error[0]
	tkey=tuple(error.keys())[0]
	tkey=re.sub(key_replace_regex,'',tkey)
	message=((key +' : ') if key else '')+ error[tkey][0]
	return message