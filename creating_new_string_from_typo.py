message = "A kong string with a silly typo"
message[2] = "l" # This will result in error

new_message = message[0:2] + "l" + message[3:]
print(new_message)

# message[2] = "l" # This will result in error <--- work around typos in strings