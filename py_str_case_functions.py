# stored str inside a sentence is a few processes 
# first we have sentence that is a variable; then we have str which is 'THe quick ..' 
# = is the variable assignment
# 3 process; str, assignment; variable storing the str
#sentence.upper() doesnt change str itself or variable cuz doesnt permanly make change just on the variable
# data flow - when processes occur .. why somethign not changing? calling a process but not storing in variable or on obj made
# when want to change values create new var

#sentence = 'The quick brown fox jumped'
# sentence --> var
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence) 
print(sentence_two)
# havent changed initial str value but have with other str value (sentence_two)
# if change permantly other methods will call accidently and cause bugs