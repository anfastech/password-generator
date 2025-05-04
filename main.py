import string
import secrets
import shelve
import os
import time

''' DETAILS ABOUT THE PROGRAM: (GENEX: Password Generator)
This program is a simple yet powerful password generator and storage tool designed to help you manage your passwords securely.

Features:
1. Generates a random strong password of length 16 using a mix of uppercase letters, lowercase letters, digits, and punctuation (special characters).
2. Stores the last generated password in a local storage file.
3. Allows you to retrieve the last generated password.
4. Enables you to store the last generated password with a custom key (e.g., GOOGLE, FACEBOOK) for easy retrieval.
5. Stores keys in UPPERCASE for consistency.
6. Retrieves passwords using the stored keys.
7. Displays the last key used to store a password.
8. Shows all stored keys.
9. Provides an option to clear all stored data.

Usage:
- Generate a new password and save it.
- Retrieve the last generated password.
- Store the last generated password with a custom key.
- Retrieve a password using a custom key.
- View the last key used.
- View all stored keys.
- Clear all stored data if needed.

This program ensures that your passwords are generated securely and stored safely for future use.

More:
- The program uses the `shelve` module to store data persistently.
- Data is stored in a folder named 'DATA' in the root directory.
- The storage file is named 'GENEX_storage' and is created inside the 'DATA' folder.
- The storage file contains the last generated password, keys, and passwords associated with those keys.
- The `shelve` module automatically handles the creation of `.dat`, `.bak`, and `.dir` files for storage.

'''

# constants 
PASSWORD_LENGTH = 16
STORAGE_FOLDER = 'DATA'
STORAGE_FILE = os.path.join(STORAGE_FOLDER, 'GENEX_storage')
os.makedirs(STORAGE_FOLDER, exist_ok=True)

def get_last_password():
    with shelve.open(STORAGE_FILE) as storage:
        return storage.get('PG_LST_PASS', '')
    
def save_password(password):
    with shelve.open(STORAGE_FILE) as storage:
        storage['PG_LST_PASS'] = password
        
def generate_password():
    alphabet = string.ascii_letters.upper() + string.ascii_letters + string.digits + '!@#'
    # alphabet = string.ascii_letters.upper() + string.ascii_letters + string.digits + string.punctuation   
    return ''.join(secrets.choice(alphabet) for i in range(PASSWORD_LENGTH))

def store_last_pass_with_key():
    print(f'Existing Keys: {show_all_keys()}')
    KEY = input('Enter Unique key: ').upper()
    password = get_last_password()
    with shelve.open(STORAGE_FILE) as storage:
        storage['PG_LST_KEY'] = KEY
        storage[KEY] = password
        keys = storage.get('PG_KEYS', [])
        if KEY not in keys:
            keys.append(KEY)
        storage['PG_KEYS'] = keys
    return f'Password saved with key: {KEY}'
        
def get_pass_with_key():
    print(f'Existing Keys: {show_all_keys()}')
    KEY = input('Case Insensitive, Type \'google\' Hit Enter \nEnter key: ').upper()
    with shelve.open(STORAGE_FILE) as storage:
        return storage.get(KEY, 'Key not found')
    
def show_last_key():
    with shelve.open(STORAGE_FILE) as storage:
        return storage.get('PG_LST_KEY', 'No key found')

def show_all_keys():
    with shelve.open(STORAGE_FILE) as storage:
        return storage.get('PG_KEYS', 'No keys found')

def opt(arg):
    match arg:
        case '0':
            return 'EXIT'
        case '1':
            password = generate_password()
            print(f'Generated Password: {password}')
            save_password(password)
            return password
        case '2':
            return get_last_password()
        case '3':
            return store_last_pass_with_key()
        case '4':
            return get_pass_with_key()
        case '5':
            return show_last_key()
        case '6':
            return show_all_keys()
        case 'CLEAR':
            ''' Clear all stored data, including the storage file '''
            try:
                os.rmdir(STORAGE_FOLDER)
            except FileNotFoundError:
                    pass
            return print("Removed STORAGE_FILE")
        case _:
            return "Invalid Option"
        
        
def main():
    while True:
         try:
             time.sleep(1) # pause menu for 1 sec
             print('\n[1] Generate Password')
             print('[2] Get Last Password')
             print('[3] Store Last Password with [key]') 
             print('[4] Get Password with [key]')
             print('[5] Show Last Key')
             print('[6] Show All Keys')
             print('\n[CLEAR] To Clear Old Data')
             print('[0] Exit')
             option = input('Enter option: ').upper()
             print(f"\n{opt(option)}")
             if option == '0':
                 break
         except Exception as e:
             print(f"Error: {e}")
             pass
        

if __name__ == "__main__":
    main()


            
         
         
'''SAVE FOR LATER'''

# For Del a specific key:
            # with shelve.open(STORAGE_FILE) as storage:
            #     keys = storage.get('PG_KEYS', [])
            #     if '0' in keys:
            #         keys.remove('0')
            #         storage['PG_KEYS'] = keys
            #         print("0 found")
            #     else:
            #         print("No keys found")
            
# For Del data files with their ext
            # for ext in ['.dat', '.bak', '.dir']:
            #     try:
            #         os.remove(STORAGE_FILE + ext)
            #     except FileNotFoundError:
            #         pass