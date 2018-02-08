score = input("Enter Score: ")

try:
    fscore = float(score)
except:
    print ("score should be numeric ")
    quit()

if  fscore >= 0.9 :
    print ("A")

elif fscore >= 0.8 :
    print ("B")

elif fscore >= 0.7 :
    print ("C")

elif fscore >= 0.6 :
    print ("D")

else :
    print ("F")
