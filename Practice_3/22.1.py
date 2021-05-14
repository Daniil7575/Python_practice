def encrypt_caesar(msg, shift):
    shift = shift if str(shift.__class__) == "<class \'int\'>" and shift > 0 else 3

    encrypted_msg = ""

    for i in msg:
        encrypted_msg += chr(((ord(i) % 1072 + shift % 32) % 32) + 1072) if i.islower() else \
                         chr(((ord(i.lower()) % 1072 + shift % 32) % 32) + 1072).upper() \
                         if i.isalpha() else i

    return encrypted_msg


def decrypt_caesar(msg, shift):
    shift = shift if str(shift.__class__) == "<class \'int\'>" and shift > 0 else 3

    decrypted_msg = ""

    for i in msg:
        decrypted_msg += chr(((ord(i) % 1072 + 32 - shift % 32) % 32) + 1072) if i.islower() else \
                         chr(((ord(i.lower()) % 1072 + 32 - shift % 32) % 32) + 1072).upper() \
                         if i.isalpha() else i

    return decrypted_msg


# msg = "Да здравствует салат Цезарь!"
# shift = 5
# encrypted = encrypt_caesar(msg, shift)
# decrypted = decrypt_caesar(encrypted, shift)
# print(encrypted)
# print(decrypted)

# Зг кзугефхецих фгогх Щикгуя!
# Да здравствует салат Цезарь!

# Йе мйхезцчзшкч цереч Ыкмехб!
# Да здравствует салат Цезарь!
