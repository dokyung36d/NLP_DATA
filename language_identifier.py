import langid

def is_english_word_langid(word):
    # Detect the language of the word
    language, confidence = langid.classify(word)
    
    # Check if the detected language is English with high confidence
    return language == 'en' and confidence > 0.95
