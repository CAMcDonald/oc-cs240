def generate_crypt(shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    crypt = {}

    for i in range(len(alpha)):
        crypt[alpha[i]] = alpha[(i + shift) % len(alpha)]
        crypt[alpha[i].upper()] = alpha[(i + shift) % len(alpha)].upper()

    return crypt 

def translate_message(message, shift):
    crypt = generate_crypt(shift)
    output = ''
    for i in range(len(message)):
        output += crypt.get(message[i], message[i])

    return output

message = 'Hello, World!'
print message
message2 = translate_message(message, 4)
print message2
message3 = translate_message(message2, -4)
print message3