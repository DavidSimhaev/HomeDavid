def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    
    index_start = text.find(start)
    index_end = text.find(end)
    l = []
    for word in range(index_start+1,index_end):
        l.append(text[word])
    text_ready = "".join(l)
    return text_ready    
                   
    
