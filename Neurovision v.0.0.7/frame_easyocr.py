import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import easyocr
class Recording_text():
    def __init__(self) -> None:
        pass
    def text_recognition_res(file_path, lng):
        reader = easyocr.Reader([lng])
        result = reader.readtext(file_path)
        l = []
        
        for index in range(len(result)):
            try:
                CORDINATE_HEIGHT = result[index][0][3][1] - result[index+1][0][3][1]
                if CORDINATE_HEIGHT < 10 and CORDINATE_HEIGHT > -10 :
                    l.append(result[index][1])
                else:
                    l.append(result[index][1])
                    l.append("\n")
                        
                    
            except:
                l.append(result[index][1])
                res = ""
                for i in l:
                    if i == "\n":
                        res += "\n"
                        continue
                    res += i+ " "
        try:
            res
        except:
            return ""
        return res
    

