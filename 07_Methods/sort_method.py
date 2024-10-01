spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)


#when we want to pass our list in reverse order the simply pass reverse=True

spam.sort(reverse=True)
print(spam)


spamAlpha = ['a', 'z', 'A', 'Z']
spamAlpha.sort(key=str.lower)
print(spamAlpha)