p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    # Read input
    Input = input()
    
    # Exit condition
    if Input == "0":
        break
    
    # Split input into shift key and string to encode
    k, s = Input.split()
    k = int(k)
    
    # Initialize result string
    res = ""
    
    # Process each character in the input string
    for char in s:
        # Find the position of the character in the custom alphabet
        pos = p.index(char)
        # Calculate new position with shift, wrapping around if needed
        new_pos = (pos + k) % len(p)
        # Append the shifted character to the result
        res += p[new_pos]
    
    # Print the result
    print(res[::-1])