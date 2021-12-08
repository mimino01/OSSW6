"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.

Adapted from code in https://inventwithpython.com/chapter14.html

"""


def encrypt(message, key):      #암호화한다.
    "Encrypt message with key."
    result = ''

    # Iterate letters in message and encrypt each individually.

    for letter in message:      #message내에서 for문 실행
        if letter.isalpha():        #letter가 알파벳이면

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)       #letter의 유니코드를 num에 저장

            if letter.isupper():        #letter의 값이 대문자라면
                base = ord('A')     #base에 A의 유니코드 값 저장
            else:
                assert letter.islower()     #letter의 값이 소문자라고 가정했을 때
                base = ord('a')     #base에 a의 유니코드 값 저장

            # The encryption equation:

            num = (num - base + key) % 26 + base        #num의 값에 대문자인지 소문자인지에 따른 유니코드 값을 빼고,
            #입력받은 key값을 더한 수 알파벳 개수로 빼준 뒤 대 소문자 여부에 따른 유니코드 값을 더해준다.

            result += chr(num)      #결과로 num의 문자를 더해준다.

        elif letter.isdigit():      #숫자인지 확인

            # TODO: Encrypt digits.
            result += letter        #결과에 letter값을 더한다.

        else:
            result += letter        #결과에 letter값을 더한다.

    return result


def decrypt(message, key):      #복호화한다.
    "Decrypt message with key."
    return encrypt(message, -key)       #입력받은 메시지에 키값을 마이너스로 적용시켜 encrypt함수를 실행한값을 돌려준다.


def decode(message):
    "Decode message without key."
    pass  # TODO


def get_key():      #키값 입력받기
    "Get key from user."
    try:
        text = input('Enter a key (1 - 25): ')      #1-25사이의 값을 입력받는다.
        key = int(text)     #정수로 저장한다.
        return key      #정수값 키를 반환
    except:
        print('Invalid key. Using key: 0.')     #예외 발생시
        return 0        #키값으로 0을 반환한다


print('Do you wish to encrypt or decrypt or brute force a message?')      #어떤 과정을 실행할 것인지 입력받는다.
choice = input()

if choice == 'encrypt':     #암호화 선택시
    phrase = input('Message: ')     #메시지를 입력받는다.
    code = get_key()        #키값을 입력 받는다.
    print('Encrypted message:', encrypt(phrase, code))
elif choice == 'decrypt':       #복호화 선택시
    phrase = input('Message: ')     #메시지를 입력받는다.
    code = get_key()        #키값을 입력 받는다.
    print('Decrypted message:', decrypt(phrase, code))
elif choice == 'decode':        #디코드 선택시
    phrase = input('Message: ')     #메시지를 입력받는다.
    print('Decoding message:')
    decode(phrase)
elif choice == 'brute':
    phrase = input('Message: ')
    print('Your translated text is: ')
    for key in range(1, 27):
        print(key, decrypt(phrase, key))
else:
    print('Error: Unrecognized Command')        #잘못 선택시 오류 메시지 출력
