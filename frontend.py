import rsa


message_list = []
def add_message(message, encrypted):
        message_list.append([len(message_list) + 1, message, encrypted, 'Unsigned', ''])

close_menu = ''

while close_menu == '':
    inp = input(
    '\nMain Menu:\n'
    '(1) Log in as Guest\n'
    '(2) Log in as Owner\n'
    '(3) Exit\n'
    'Select a function by inputing 1, 2, or 3:\n'
    )

    if inp == '1':
        guest_inp = ''
        while guest_inp != 'exit':
            guest_inp = input(   
                            '\nGuest Menu:\n'
                            '(1) Post a new message\n'
                            '(2) Select an existing message\n'
                            '(3) Log out as Guest\n'
                            'Select a function:\n'
                        )
            if guest_inp == '1':
                new_message = input('Enter new message:\n')
                ask_to_encrypt = ''
                while ask_to_encrypt not in {'Y','N'}:
                    ask_to_encrypt = input('Would you like to encrypt this message? Y/N\n').upper()[0]
                    if ask_to_encrypt not in {'Y','N'}:
                        print('Invalid input. Please try again.\n')
                #Write new message into List
                if ask_to_encrypt == 'Y':
                    add_message(new_message, ask_to_encrypt)
                    message_list[len(message_list) - 1][1] = rsa.encryptString(message_list[len(message_list) - 1][1])
                else:
                    add_message(new_message, ask_to_encrypt)
                print('Message added to list\n')
            elif guest_inp == '2':
                #Display message and attributes
                if len(message_list) == 0:
                    print('\nThere are no messages to display\n')
                else:
                    print('\nIndex | Message | Encrypted | Signed')
                    for i in message_list:
                        print(i[0], '|', i[1][0:15], '|', i[2], '|', i[3])
                    message_number = input('Select a message by number:\n')
                    message_range = []
                    for i in range(1,len(message_list)+1):
                        message_range.append(str(i))
                    while message_number not in message_range:
                        message_number = input('Invalid input. Select a message by number:\n')
                    message_number = int(message_number)
                    print(message_list[message_number-1][1])
                    if message_list[message_number-1][4] == '':
                        print('Message has no digital signature\n')
                    else:
                        #Check the signature
                        #
                        #
                        pass

            elif guest_inp == '3':
                guest_inp = 'exit'
            else:
                print('Invalid input. Please make another selection.\n\n')
    elif inp == '2':
        #Insert Owner functions
        owner_inp = ''
        while owner_inp != 'exit':
            owner_inp = input(   
                            '\nOwner Menu:\n'
                            '(1) Post a new message\n'
                            '(2) Select an existing message\n'
                            '(3) Log out as Owner\n'
                            'Select a function:\n'
                        )
            if owner_inp == '1':
                new_message = input('Enter new message:\n')
                ask_to_encrypt = ''
                while ask_to_encrypt not in {'Y','N'}:
                    ask_to_encrypt = input('Would you like to encrypt this message? Y/N\n').upper()[0]
                    if ask_to_encrypt not in {'Y','N'}:
                        print('Invalid input. Please try again.\n')
                #Write new message into List
                if ask_to_encrypt == 'Y':
                    add_message(new_message, ask_to_encrypt)
                    message_list[len(message_list) - 1][1] = rsa.encryptString(message_list[len(message_list) - 1][1])
                else:
                    add_message(new_message, ask_to_encrypt)
                print('Message added to list\n')
            elif owner_inp == '2':
                #Display message and attributes
                if len(message_list) == 0:
                    print('There are no messages to display\n')
                else:
                    print('\nIndex | Message | Encrypted | Signed')
                    for i in message_list:
                        print(i[0], '|', i[1][0:15], '|', i[2], '|', i[3])
                    message_number = input('Select a message by number:\n')
                    message_range = []
                    for i in range(1,len(message_list)+1):
                        message_range.append(str(i))
                    while message_number not in message_range:
                        message_number = input('Invalid input. Select a message by number:\n')
                    message_number = int(message_number)
                    message_op_inp = ''
                    while message_op_inp != 'exit':
                        print(message_list[message_number-1][1])
                        message_op_inp = input(
                                                    'Would you like to:\n'
                                                    '(1) Sign this message\n'
                                                    '(2) Encrypt this message\n'
                                                    '(3) Decrypt this message\n'
                                                    '(4) Delete this message\n'
                                                    '(5) Exit Message Menu\n'
                                                )
                        if message_op_inp == '1':
                            if message_list[message_number-1][4] != '':
                                print('Message already has a digital signature\n')
                            else:
                                #Sign Message
                                #
                                #
                                pass
                        elif message_op_inp == '2':
                            if message_list[message_number - 1][2] == 'N':
                                message_list[message_number - 1][1] = rsa.encryptString(message_list[message_number - 1][1])
                                message_list[message_number - 1][2] = 'Y'
                                print('Message encrypted:\n' + message_list[message_number - 1][1] + '\n')
                                message_op_inp = 'exit'
                            else:
                                print('Message was already encrypted\n')
                        elif message_op_inp == '3':
                            if message_list[message_number - 1][2] == 'Y':
                                message_list[message_number - 1][1] = rsa.decryptString(message_list[message_number - 1][1])
                                message_list[message_number - 1][2] = 'N'
                                print('Message decrypted:\n' + message_list[message_number - 1][1] + '\n')
                                message_op_inp = 'exit'
                            else:
                                print('Message is not encrypted\n')
                        elif message_op_inp == '4':
                            delete_check = input('Are you sure you want to delete this message? Y/N\n')[0].upper()
                            if delete_check == 'Y':
                                del message_list[message_number-1]
                                for i in message_list:
                                    if i[0] > message_number:
                                        i[0] = i[0] - 1
                                message_op_inp = 'exit'
                        elif message_op_inp == '5':
                            message_op_inp = 'exit'
                        else:
                            print('Invalid input. Please try again.\n')
            elif owner_inp == '3':
                owner_inp = 'exit'
            else:
                print('Invalid input. Please make another selection.\n\n')
        pass
    elif inp == '3':
        ask_to_close = input('If you exit all data will be deleted. Do you want to continue? Y/N\n').upper()
        if ask_to_close[0] == 'N':
            inp = ''
        elif ask_to_close[0] == 'Y':
            close_menu = 1
        else:
            print('\nInvalid input. Please make another selection.\n')
    else:
        print('\nInvalid input. Please make another selection.\n')

