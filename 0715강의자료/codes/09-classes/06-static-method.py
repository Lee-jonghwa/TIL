class StringUtils:

    def __init__(self):
        pass

    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
    
text = 'hello, world'

result1 = StringUtils.reverse_string(text)
result2 = StringUtils.capitalize_string(text)
 
print(result1) # dlrow ,olleh
print(result2) # Hello, world