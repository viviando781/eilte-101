def main():
    list1 = ['JIO68Y', 'GYF893', 'UGDUY1', 'GUI314', 'UISAD', 'HIOG53', 'BIVYU2', 'BYUT21']
    name = input('What is your name? ')
    print(f'Hi {name}, how can we help you?')
    print('1. Returns')
    print('2. Exchange')
    
    num = int(input("Enter 1 or 2: "))
    
    if num == 1:
        receipt = input('Please enter your receipt number: ')
        if receipt in list1:
            print('We secussfuly got your order.')
        else:
            print('Sorry, we do not have your order.')
    elif num = 2:
        stuff = input('What do you want to exchange? ')
        receipt2 = input('Please enter your receipt number: ')
        if receipt2 in list1:
            print('We secussfuly got your order.')
        else:
            print('Sorry, we do not have your order.')
main()
