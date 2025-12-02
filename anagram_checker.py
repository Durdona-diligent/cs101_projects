def are_anagrams(string1, string2):
    a = string1.lower()
    b = string2.lower()
    cleaned_list1 = []
    cleaned_list2 = []
    for character in a:
        if 'a' <= character <= 'z':
            cleaned_list1.append(character)
    for character in b:
        if 'a' <= character <= 'z':
            cleaned_list2.append(character)
    cleaned_list1.sort()
    cleaned_list2.sort()
    return cleaned_list1 == cleaned_list2
print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))