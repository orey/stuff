import os
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

#---------------------------------------------count_words
def count_words(filename):
    # Get English stop words
    stop_words = set(stopwords.words('english'))
    
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            text = f.read().lower()  # Convert to lowercase
        except Exception as e:
            print(e)
            print(f"Problem with {filename}. Skipping...")
            return False
    
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Filter out stop words and non-alphabetic tokens
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    
    # Count occurrences
    word_counts = Counter(filtered_tokens)
    
    return word_counts


#---------------------------------------------count_words_in_files
def count_words_in_file(root, dict):
    for root, folders, files in os.walk(root):
        for f in files:
            if not f.endswith(".txt"):
                print(f"Not a text file: {f}")
            counts = count_words(os.path.join(root,f))
            if counts == False:
                continue

            # Print results sorted by frequency
            print(f)
            for word, count in counts.most_common():
                print(f"{word}: {count} | ", end="")
                if word in dict:
                    dict[word] += count
                else:
                    dict[word] = count
            print("\n")
    #sort
    sorted_dict = {}
    for key in sorted(dict, key=dict.get):
        sorted_dict[key] = dict[key]
    print(sorted_dict)

    
#--------------------------------------------- main
if __name__ == "__main__":
    dict = {}
    root = "C:\\ct\\c\\GREECE\\"
    count_words_in_file(root, dict)
    
                





        
