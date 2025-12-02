def reformat_number(phone_number):
    cleaned_num = []
    for num in phone_number:
        if '0' <= num <= '9':
            cleaned_num.append(num)
    return cleaned_num
print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3