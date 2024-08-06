def count_vowel(String):
    vovels = "aeiouAEIOU"
    cnt = 0

    for char in String:
        if char in vovels:
            cnt += 1
    
    return cnt

vovels = input("Enter string: ")
print(f'Vowel count in "{vovels}" is: {count_vowel(vovels)}')