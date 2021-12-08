from random import sample, shuffle

digits = int(input('몇자리 수를 맞추시겠습니까?'))          #맞출 숫자의 개수를 입력받는다.
guesses = int(input('몇 번 만에 맞출 수 있나요?'))          #맞출 수 있는 기회를 입력받는다.

print('제가 생각한 숫자는', digits, '자리의 숫자입니다.')
print('이 숫자를 맞춰보세요.')
print('여기 힌트를 드리겠습니다.:')
print('이 말은:    이런 뜻입니다.:')
print('  pico         숫자는 맞지만 자리가 틀렸습니다.')    #pico는 숫자는 맞고 위치가 다름을 의미
print('  fermi        숫자와 자리가 맞습니다.')             #fermi는 숫자와 위치가 맞음을 의미
print('  bagels       숫자와 자리 모두 틀렸습니다.')        #숫자와 위치 모두 틀림을 의미
print('세 숫자는 반복된 숫자가 없습니다.')        

def playAgain():                                            #게임 재시작 여부를 입력받는다.
    print('한판 더? (yes or no)')
    return input().lower().startswith('y')

while True:
    letters = sample('0123456789', digits)                  #letters에 0부터 9까지 저장한다.

    if letters[0] == '0':                                   #만약 0이라면
        letters.reverse()                                   #letters리스트의 순서를 뒤집는다.

    number = ''.join(letters)                               #letters 리스트를 문자열로 반환하여 number에 저장

    print('숫자를 생각했습니다.')                            #랜덤한 세자리 숫자 설정 완료
    print('당신은', guesses, '번의 기회가 있습니다.')        #남은 기회 출력

    counter = 1
    while counter <= guesses :
        print('추리 #', counter)                            #몇번째 추리인지 출력
        guess = input()                                     #사용자로부터 숫자를 입력 받는다.

        if len(guess) != digits:                            #세자리 숫자가 아닌 수를 입력받을 경우
            print('잘못된 숫자입니다. 다시 입력하세요!')     #다시 입력하라는 메시지 출력
            continue

        clues = []

        for index in range(digits):                         #세자리 숫자에서 for문 실행
            if guess[index] == number[index]:               #입력받은 수와 생성한 수의 위치의 수가 같을 경우
                clues.append('fermi')                       #clues함수에 fermi저장
            elif guess[index] in number:                    #숫자는 같고 위치는 다를 경우
                clues.append('pico')                        #clues함수에 pico출력

        shuffle(clues)                                      #clues리스트 멤버 셔플

        if len(clues) == 0:                                 #clues 리스트가 비어있다면
            print('bagels')                                 #맞는 것이 없다는 bagels 출력
        else:
            print(' '.join(clues))                          #아닐경우 clues를 문자열로 출력

        counter += 1                                        #counter 1증가

        if guess == number:                                 #입력받은 수와 생성된 수가 일치할 경우
            print('정답입니다!')                            #정답 메시지 출력
            break

        if counter > guesses:                               #설정해둔 10번의 기회를 넘어갈 경우
            print('기회를 다 쓰셨네요. 정답은', number)      #기회 소진 메시지 출력 후 답을 출력
            break       

    if not playAgain():                                     #재시작하지 않는다는 키를 입력받으면
        break                                               #종료한다.