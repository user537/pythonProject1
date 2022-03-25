def Survey():
    print('1) Blue')
    print('2) Red')
    print('3) Yellow')
    question = int(input('Out of these options\(1,2,3), which is your favourite?'))
    if question == 1:
        print('Nice!')
    elif question == 2:
        print('Cool')
    elif question == 3:
        print('Awesome!')
    else:
        print('That\'s not an option!')