s = """There has been a lot of research which shows the importance
 of physical health in avoiding anxiety and depression. The mind 
 and the body are highly interconnected. We can all make fairly
  easy changes in our lifestyle to include more exercise, healthier 
  eating, getting enough sleep, being exposed to sunlight and so on.
   Research into exercise has found that it has a positive impact on mood. 
   Physical activity stimulates the release of endorphins in the brain to produce the feel-good factor.
    Sleep is vitally important for children and adolescents to help concentration levels.
     A good night’s sleep also stops people being bad-tempered and flying off the handle."""

l = s.split(" ")
print(l)

l1 = ['a', 'b', 'c']
print(l1)

print(l[6])
s1 = l[6]
print(s1)

s2 = " ".join(l)
print(s2)
lis1 = l
lis1.sort()
print(lis1)

l1 = ['a']
print(l1)
l1.append('b')
print(l1)
del l1[1]
print(l1)
l1.append('b')
l1.append('c')
print(l1)

pullOut = l1.pop(3)
print(l1)
print(pullOut)
