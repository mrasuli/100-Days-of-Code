import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# number_of_ppl = len(names)

# choice = random.randint(0, number_of_ppl -1)

# p_name = names[choice]
# print(p_name)

the_person_who_will_pay = random.choice(names)
print(f"the person who will pay is {the_person_who_will_pay}")