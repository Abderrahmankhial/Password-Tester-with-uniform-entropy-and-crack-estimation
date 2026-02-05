"""
this script purpose is to test he strength of password
what'll do is the following:
- take a password as input
- check its length
- check for the presence of uppercase letters, lowercase letters, digits, and special characters
- provide a strength rating based on the checks
- calculate the entropy of the password
- give suggestions for improving the password strength
- measure the time it would take to crack the password using brute-force methods
"""
import math

#calculate entropy
def calculate_entropy(password,chars):
    pool=0
    passwd_length = len(password)
    if chars[0]:
        pool=pool+10
    if chars[1]:
        pool=pool+26
    if chars[2]:
        pool=pool+26
    if chars[3]:
        pool=pool+32
    if pool == 0 or passwd_length == 0:
        return 0, pool
    entropy=passwd_length*math.log2(pool)
    return entropy,pool
    
#check what the input is made of 
def list_characteristics(password):
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False
    for i in password:
        if i.isnumeric():
            hasDigit=True
        elif i.islower():
            hasLower=True
        elif i.isupper():
            hasUpper=True
        else:
            hasSpecial=True
    # return after scanning all characters
    return (hasDigit, hasLower, hasUpper, hasSpecial)
def calculate_time_to_crack(pool,password_length):
    ONLINE_RATE = 3          # guesses/sec (rate-limited)
    OFFLINE_RATE = 1_000_000 # conservative offline
    total_possible_number=pool**password_length
    online=total_possible_number/(2*ONLINE_RATE)
    offline=total_possible_number/(OFFLINE_RATE*2)
    return online,offline
def rate(entropy):
    if entropy < 28:
        return "Very Weak"
    elif 28 <= entropy < 36:
        return "Weak"
    elif 36 <= entropy < 60:
        return "Reasonable"
    elif 60 <= entropy < 128:
        return "Strong"
    else:
        return "Very Strong"
def suggest_password(password):
    suggestions = []
    if len(password) < 12:
        suggestions.append("Increase the length of your password to at least 12 characters.")
    if not any(char.isupper() for char in password):
        suggestions.append("Include uppercase letters.")
    if not any(char.islower() for char in password):
        suggestions.append("Include lowercase letters.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include digits.")
    if not any(not char.isalnum() for char in password):
        suggestions.append("Include special characters.")
    return "\n".join(suggestions) if suggestions else "Your password is strong. No suggestions needed."
if __name__=="__main__":
    password = input("Enter a password to test its strength: ")
    chars=list_characteristics(password)
    entropy, pool = calculate_entropy(password,chars)
    online, offline = calculate_time_to_crack(pool,len(password))
    rating =rate(entropy)
    suggestions = suggest_password(password)

    print(f' Password analysis :\n Digits : {chars[0]} \n Lower characters : {chars[1]} \n Upper characters : {chars[2]} \n Special : {chars[3]} \n the entropy is {entropy:.2f} Bits \n Time to crack online : {online/60:.2f} minutes \n Time to crack offline : {offline/60:.2f} minutes\n Overall strength : {rating} \n Suggestions : {suggestions}')