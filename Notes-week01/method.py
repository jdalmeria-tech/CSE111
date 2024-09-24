text1 = "hello"
text2 = text1.upper  # Assigns the method reference, does NOT convert text1 to uppercase
print(text2)         # Outputs: <built-in method upper of str object at 0x...>
print(text2())       # Now calling the method, outputs: HELLO
