import json
import re

def create_fixture_json(file_path):
    '''
    create word.json strating from words.txt.
    :param file_path:
    :return:
    '''
    #Create temp file
    fixture_file = open('../fixtures/words.json','w')
    text_file = open(file_path)
    dict_list = []
    for line in text_file:
        dictionary = {}
        line = line.lower()
        line = re.sub(r'[^0-9a-z]', '', line)
        dictionary['model'] = 'urlshortener_app.Word'
        dictionary['pk'] = line
        dictionary['fields'] = {}
        dictionary['fields']['word_text'] = line
        dict_list.append(dictionary)
    json_text = json.dumps(dict_list)
    fixture_file.write(json_text)
    fixture_file.close()
    text_file.close()

def main():
    create_fixture_json('words.txt')
    # to load data into db use  python manage.py loaddata ./fixtures/words.json

if __name__ == '__main__':
    main()



