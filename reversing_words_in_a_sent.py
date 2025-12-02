def reverse_words(sentence):
    parts = sentence.split()
    result = []
    for i in parts:
        result.append(i[::-1])
    final_result = " ".join(result)
    return final_result

print(reverse_words("Hello World"))