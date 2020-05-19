# number = int(input('Type the score. '))

# if number >= 90 and number <= 100:
#     print ('Your score is A. ')

# elif number >= 80 and number <= 89:
#     print ('Your score is B. ')

# elif number >= 70 and number <= 79:
#     print ('Your score is C. ')

# elif number >= 60 and number <= 69:
#     print ('Your score is D. ')

# else:
#      print ('Your score is F. ')

number = float(input('Type the score. '))

if number >= 90:
    letter = 'A'
    
elif number >= 80:
    letter = 'B'

elif number >= 70:
    letter = 'C'

elif number >= 60:
    letter = 'D'

else:
      letter = 'F'

print ('Your score is: ' + letter)
     