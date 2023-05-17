import os

class ApiXInterpreter :    
    def unencodeCustomXXXX(encoder_file_name, encrypted_key, the_value_for_splitter):
        unencode = ""
        array_ascii = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9,"."," "]
        array_coded = []
        checker = []
        SPLIT = the_value_for_splitter
        file_path = os.path.join("encode", encoder_file_name + ".apixi")
        if os.path.isfile(file_path):
            with open("./encode/" + encoder_file_name + ".apixi", "r") as file:
                for line in file :
                    if line.strip() == "START" or line.strip() == "END":
                        checker.append(line)
                        continue
                    else:
                        array_coded.append(line.strip())
            if len(array_coded) != len(set(array_coded)):
                return "You cannot put the same encoded character in another!"
            else:             
                if len(array_coded) > len(array_ascii) :
                    return "Seems that the encoded file has more encoded content than the capacity of the Decrypt Function!\nPlease use the amount of 63 encoded lines.\nRemember : 63 lines of encrypted characters and 2 lines with START and END. Total of 65 lines in the file."
                elif len(array_coded) < len(array_ascii) :
                    return "Seems that the encoded file has less encoded content than the capacity of the Decrypt Function!\nPlease use the amount of 63 encoded lines.\nRemember : 63 lines of encrypted characters and 2 lines with START and END. Total of 65 lines in the file."
                else:
                    if len(checker) < 2 :
                        return "Please use file syntax like : \nSTART\n...\nencoded_caracter\n...\nEND"
                    elif checker[0] != "START" and checker[1] != "END" :
                        return "Please use file syntax like : \nSTART\n...\nencoded_caracter\n...\nEND"
                    else:  
                        if SPLIT not in encrypted_key :
                            return "Invalid key syntax. Check if your key is legit!"
                        else:
                            decode = encrypted_key.split(SPLIT)
                            for x in decode :
                                for i, element in enumerate(array_coded):
                                    if x == element :
                                        unencode += array_ascii[i]
                                        break
                                    else:
                                        continue
                            if len(unencode) == 0 or len(unencode) < len(decode) :
                                return "Invalid key. Please check if the key is valid!"
                            else :
                                return unencode
        else:
            return "Invalid coded file. Please check the filename or if there is a coded file!"
    
    def unencodeCustom(encoder_file_name, encrypted_key, the_value_for_splitter):
        unencode = ""
        array_ascii = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9,".", " "]
        array_coded = []
        checker = []
        SPLIT = the_value_for_splitter
        file_path = os.path.join("encode", encoder_file_name + ".apixi")
       
        with open("./encode/" + encoder_file_name + ".apixi", "r") as file:
            for line in file :
                if line.strip() == "START" or line.strip() == "END":
                    checker.append(line)
                    continue
                else:
                    array_coded.append(line.strip())
            
        decode = encrypted_key.split(SPLIT)
        for x in decode :
            for i, element in enumerate(array_coded):
                if x == element :
                    unencode += array_ascii[i]
                    break
                else:
                    continue
        
        return unencode
    
    def encodeCustom(name_for_key_file, key_non_encrypted, the_value_for_splitter, encoder_file):
        encode = ""
        array_ascii = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9,"."," "]
        array_coded = []
        checker = []
        index_of_ascii = []
        helper = 0
        SPLIT = the_value_for_splitter
        file_path = os.path.join("encode", encoder_file + ".apixi")
        with open("./encode/" + encoder_file + ".apixi", "r") as file:
            for line in file :
                if line.strip() == "START" or line.strip() == "END":
                    checker.append(line)
                    continue
                else:
                    array_coded.append(line.strip())
        split_key = list(key_non_encrypted)
        for i in split_key:
            for x in array_ascii:
                if i == x:
                    index = array_ascii.index(x)
                    index_of_ascii.append(index)
                    break
        for y in index_of_ascii :
            encode += array_coded[y]
            if  helper < (len(index_of_ascii) - 1):
                helper += 1
                encode += SPLIT
        file = open("./api/" + name_for_key_file + ".apix", "w")
        file.write(encode)
        file.close()

    def getKey(file_name) :
        file_path = os.path.join("api", file_name + ".apiX")
        if os.path.isfile(file_path):
            file = open("./api/" + file_name + ".apiX")
            content_file = file.read()
            file.close()
            return content_file
        else:
            return "Invalid coded file. Please check the filename or if there is a coded file!"