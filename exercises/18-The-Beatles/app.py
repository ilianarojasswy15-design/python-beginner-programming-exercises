# ✅↓ Write your code here ↓✅
def sing():
    full_lyric = ""
    #i=
    for i in range(1,12):
        if i==11:
            full_lyric += "whisper words of wisdom, let it be"
        elif i==5:
            full_lyric += "there will be an answer,\n"
        else:
            full_lyric += "let it be,\n"
    #i=i+1

    return full_lyric

print(sing())