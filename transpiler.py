#Transpiler for config.txt

def read():
    config = open("config.txt").readlines()
    
    R = list()
    temp_image = list()
    add = False
    go = True
    
    for line in config:
        if go:
            "---Get image---"
            if line.__contains__("'''"):
                if add: #End loop
                    add = False
                    go = False
                    
                    temp_image = temp_image[1:]
                
                else: #Set off loop
                    add = True

            if add: #During loop
                temp_image.append(line[:-1])
        
        elif line.strip() != "":
            "---Scan functions---"
            out = list()
                        
            line = line.split()
            cline = line.copy()[1:]
            out.append(line.pop(0))
            out.append("(")
            
            for arg in cline:
                out.append(line.pop(0))
                out.append(",")

            out.append(")")
            R.append("".join(out))

    #Modify image so all lines have the same amount of chars
    line_max = len(max(temp_image, key=len))
    image = [x + (" " * (line_max - len(x))) for x in temp_image]
    R.insert(0, image)

    return(R)
