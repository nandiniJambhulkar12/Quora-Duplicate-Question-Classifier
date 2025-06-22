import pickle

# Example list of common English stopwords
stopwords_list = [
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'in', 'on', 'for', 'at',
    'by', 'from', 'up', 'down', 'out', 'about', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being'
]

# Save the list to stopwords.pkl
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(stopwords_list, f)

print("stopwords.pkl file created successfully!")
