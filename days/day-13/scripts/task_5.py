# word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # False: 0 is not equal to input
word_per_page = int(input("Number of words per page: ")) # fix: should be single equal sign
total_words = pages * word_per_page


print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}") # issue with word_per_page
print(total_words)
