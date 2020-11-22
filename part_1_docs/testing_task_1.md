### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # An assignment operator has been used on line 22 instead of an equality operator, this will result in an error.
    if card.value = 1:
      return True
    # There should be a colon at the end of line 25, this may result in an error.
    else
      return False
   
  # On line 30, it should be 'def' instead of 'dif'.
  # There should also be a comma between card1 and card2. 
  dif highest_card(self, card1 card2):
  # On line 32, this should be indented.
  if card1.value > card2.value:
    # On line 34, it should state "return card1".
    return card
  else:
    return card2
  

# On line 40, there should be indentation so that the method definition lines up with the previous two method definitions.
def cards_total(self, cards):
  # On line 42, total is not defined - it needs to be given a value, for example total = 0. 
  total
  for card in cards:
    total += card.value
    # On line 47, the return statement needs to be placed outside of the for loop, because otherwise the statement will be returned for each card in cards.
    # Also, total needs to be converted to a string, as it will not be possible to concatenate a string with an integer.  A space will also need to be inserted for readability.
    return "You have a total of" + total
  
```
