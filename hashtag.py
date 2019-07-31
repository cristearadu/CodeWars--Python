def generate_hashtag(s):

    return "#" + ''.join((item[0].upper()+item[1:].lower()) for item in s.split() if s.split() )


print(generate_hashtag(" hello there thanks for trying my Kata"))
print(generate_hashtag(" "))

def generate_hashtag(s):
    ans = "#"+str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
print(generate_hashtag(" hello there thanks for trying my Kata"))
print(generate_hashtag(" "))

