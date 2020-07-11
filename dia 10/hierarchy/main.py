from dog import Dog
from races import JackRussellTerrier
from races import Dachsund
from races import Bulldog

#o bien para hacer los 3 imports anteriores d ela siguiente manera
#import races import *

lea = Dog('Lea', 2)
Jack = JackRussellTerrier('Jack', 3)
buddy = Dachsund('Buddy', 9)
billy = Bulldog('Billy', 2)

print(lea)
print(lea.speak('Guof'))
print(Jack.species)
print(buddy.name)
print(buddy)
print(billy.speak('Woof'))
