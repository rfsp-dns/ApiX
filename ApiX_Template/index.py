from library.apix import ApiXInterpreter as apix

VALUE = "Test123" #This is the value of a key

split_value = "mmmoo" #This will be the split of the key

split_value2 = "bbbbbbbbbbb" #Try not to use values that can be related to the encrypted characters

encript = apix.encodeCustom("my_api", VALUE, split_value,"company") #This will generate the encrypted key

key = apix.getKey("my_api") #You don't need to copy the key, you have this funcion

key_enc = apix.unencodeCustom("company", key, split_value) #This will unencrypt the key and make it like 'Test123' again

print("Encode : " + key) # Will print the encrypted 

print("Unencode : " + key_enc) # Will print the unencrypted
