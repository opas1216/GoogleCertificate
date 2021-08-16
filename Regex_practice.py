import re
def check_web_address(text):
    '''The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it
    contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and
     a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill
     in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and
     end-of-line characters, and character classes.'''
    pattern = r"^[\w\.\-\+]*\.[a-zA-Z]*$"
    result = re.search(pattern, text)
    return result != None

def check_time(text):
    pattern = r"[\d]+\:[0-59]+\s?[am|AM|pm|PM]"
    result = re.search(pattern, text)
    return result != None

def contains_acronym(text):
    pattern = r"\([A-Z\d]+[a-zA-Z\d]+\)"
    result = re.search(pattern, text)
    if result!= None:
        print(result)
    return result != None

def extract_pid(log_line):
    # regex = r"\[(\d+)\]"
    regex = r"\[(\d+)\][\:\s]+([A-Z]+)"
    # regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    print(f"Result = {result}")
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


def transform_record(record):
  new_record = re.sub(r"([\d|-]+)", r"+1-\1", record)
  return new_record


def multi_vowel_words(text):
  pattern = r"\b\w*[a|e|i|o|u]{3}\w*\b"
  result = re.findall(pattern, text)
  return result


def transform_comments(line_of_code):
  result = re.sub(r"[#]{1,3}", "//", line_of_code)
  return result


def convert_phone_number(phone):
  result = re.sub(r"([\d]{3})-([\d]{3})-([\d]{4}\b)", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300




# print(transform_comments("### Start of program"))
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable"))
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable"))
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)"))
# # Should be "  return(number)"




# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']
# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# # ['Obviously', 'queen', 'courageous', 'gracious']
# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# # ['rambunctious', 'quietly', 'delicious']
# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# # ['queue']
# print(multi_vowel_words("Hello world!"))
# # []




# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator
# print(transform_record("Eli Jones,684-3481127,IT specialist"))
# # Eli Jones,+1-684-3481127,IT specialist
# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer
# print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# # Charlie Rivera,+1-698-746-3357,Web Developer





#
# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True


# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]")) # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


