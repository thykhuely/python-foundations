import urllib

# urllib is a module in Python Standard Library

def read_text():
          
# Read text from document

          quotes = open("/Users/ThyKhueLy/Documents/STUDYING/UDACITY/Python Introduction/movie_quotes.rtf")
          contents_of_file = quotes.read()
          print(contents_of_file)
          quotes.close()
          check_profanity(contents_of_file)

def check_profanity(text_to_check):
          
# Check text for curse words

          connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
          output = connection.read()
          #print(output)
          connection.close()
          if "true" in output:
                    print("Profanity!!!")
          elif "false" in output:
                    print("This document has no curse words!")
          else:
                    print("Could not scan document properly")

read_text()
