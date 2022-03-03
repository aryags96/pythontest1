def non_repeating_characters(s):
    while s!="":
        slen0=len(s)
        ch=s[0]
        s=s.replace(ch,"")
        slen1=len(s)
        if slen1==slen0-1:
            print("First non-repeating character=",ch)
            break
    else:
        print("No unique characters found")
s="djebdedbekfrnkfnduwbdwkd"
non_repeating_characters(s)

def non_repeating_characters_fast_find(str1):
    char_order=[]
    counts={}
    for c in str1:
        if c in counts:
            counts[c]+=1
        else:
            counts[c]=1
            char_order.append(c)
    for c in char_order:
        if counts[c]==1:
            return c
    return None
str1="djebdedbekfrnkfnduwbdwkd"
non_repeating_characters_fast_find(str1)

