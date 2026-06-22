# if we want to repeat the same thing 3x we can put print(meow) 3x, and copy paste it as many times as needed... but that's inefficient, especially if you need to change the repeat and to 50x
#print("meow")
#print("meow")
#print("meow")

#while is a contruct that allows us to repeat answers and questions
#below is an example where condition 1 is never true in condition 2, resulting in meows; but this will go on infinitely... be very careful o, o looping forever
#i = 3
#while i != 0:
#    print("meow")

#somehow eventually make the condition 1 match to condition 2
#i = 3
#while i != 0:
#    print("meow")
#    i = i - 1 #making the number 3 eventually reach 3 to 2 to 1 then 0 //// you can also reverse the whole thing as well, and count upward from i+1, just remember to change operations

# most computer science professionals count up from zero, if we we only want to repeat 3x, just succintly state up to 3
i = 0
while i < 3:
    print("meow")
    i += 1 #can succintly use += for i + 1
