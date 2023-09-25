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
	

from time import time as stamp_t


i1 = int(input("---\n\nhow many passwords do you want?: "))

print("\n***\n")

that_text = ""

while i1 > 0:
	n_password = get_password()

	print("-\n{}".format( n_password ))

	that_text += "{}\n".format(n_password)
	i1 -= 1


i2 = input("\n-do you want to save it?(y/n):")

if i2 == "y":
    from time import time as stamp_t
    
    file = open("{}.txt".format(str( stamp_t() )) , "w")
    file.write(that_text)
    file.close()

    print("-\n-\nsaved successfully.\n")
else:
    pass


print("-\nthe end...\n")
