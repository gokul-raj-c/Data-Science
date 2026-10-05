import re

mylist=[
    'i am haappy',
    'htpps://',
    '$1000 rs'
]

class DataHandling():
    def clean_text(self,mylist):
        cleaned_list = []
        for text in mylist:
            # Remove URLs (including misspelled htpps://)
            text = re.sub(r'https?://\S+|htpps://\S*', '', text)

            # Remove special characters
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

            # Remove extra spaces
            text = re.sub(r'\s+', ' ', text).strip()

            # Convert to lowercase
            text = text.lower()

            cleaned_list.append(text)

        return cleaned_list

obj = DataHandling()
result = obj.clean_text(mylist)

print(result)