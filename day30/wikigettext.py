import wikipedia, re
wikipedia.set_lang("ru")

def getwiki(s):
    try:
        my = wikipedia.page(s)
        wikitext = my.content[:500]
        wikimas = wikitext.split(".")
        wikimas = wikimas[:-1]
        wikires= ""
        for line in wikimas:
            
            if (len(line.strip())>5):
                wikires += line+"."
            
        
        wikires = re.sub('\([^()]*\)','', wikires)
        wikires = re.sub('\{^\{\}]*\}','',wikires)
        return wikires
            
    except:
        return "Такой информации найти не смогли"