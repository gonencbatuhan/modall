

#producing easy-reading passwords
def get_password():
	new_password = ""
	
	import string
	from random import randint as r_int
	
	char_list = string.ascii_lowercase + string.ascii_uppercase + string.digits
	
	list_size = len(char_list) - 1
	
	v1 = 0
	v2 = 0
	
	while v1 < 3:
		new_part = ""
		
		while v2 < 5:
			new_part += char_list[r_int(0, list_size)]
			v2 += 1
		
		if v1 != 2:
			new_password += "{}-".format(new_part)
			
		else:
			new_password += new_part
			break
			
		v2 = 0
		v1 += 1	
		
	return new_password
	

i1 = int(input("---\n\nhow many passwords do you want?: "))

while i1 > 0:
	print("-\n{}\n-\n".format( get_password() ))
	i1 -= 1
	
print("-\n-\n-\n-\nthe end...\n")
