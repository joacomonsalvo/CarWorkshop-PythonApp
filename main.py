import os
import csv
import json
from googletrans import Translator

FILETYPE = '.csv'
SETTINGS_FILETYPE = '.json'
USERNAME = os.getlogin()
PATH = 'C:/Users/{}/Documents/Projects/Vehicles'.format(USERNAME)
JSON_LIST = []


class Data:

    @classmethod
    def settings(cls):
        with open(PATH + '/data_file' + SETTINGS_FILETYPE, 'r') as json_file:
            data = json.load(json_file)
            JSON_LIST.append(data['country'])
            JSON_LIST.append(data['language'])

    @classmethod
    def file_name(cls):
        filename = 'carsDATA'
        return filename


class Translations:
    def __init__(self):
        Data.settings()
        self.username = USERNAME
        self.translator = Translator()
        self.country = JSON_LIST[0]
        self.language = JSON_LIST[1]

    def start(self):
        if self.language == 'Spanish':
            content1 = self.translator.translate("Let's start with some information about your vehicle",
                                                 src='en', dest='es')
            start_text = content1.text
            print(start_text + ': \r\n')
        elif self.language == 'English':
            content1 = self.translator.translate("Let's start with some information about your vehicle",
                                                 src='en', dest='en')
            start_text = content1.text
            print(start_text + ': \r\n')

    def first_name(self):
        if self.language == 'Spanish':
            content = self.translator.translate('Owner Fist Name', src='en', dest='es')
            first_name = content.text
            firstname = input('{}: \r\n'.format(first_name)).title()
            return firstname
        elif self.language == 'English':
            content = self.translator.translate('Owner Fist Name', src='en', dest='en')
            first_name = content.text
            firstname = input('{}: \r\n'.format(first_name)).title()
            return firstname

    def last_name(self):
        if self.language == 'Spanish':
            content = self.translator.translate('Owner Last Name', src='en', dest='es')
            last_name = content.text
            lastname = input('{}: \r\n'.format(last_name)).title()
            return lastname
        elif self.language == 'English':
            content = self.translator.translate('Owner Last Name', src='en', dest='en')
            last_name = content.text
            lastname = input('{}: \r\n'.format(last_name)).title()
            return lastname

    def brand(self):
        if self.language == 'Spanish':
            content = self.translator.translate('Vehicle brand', src='en', dest='es')
            brand_text = content.text
            brand = input('{}: \r\n'.format(brand_text)).title()
            return brand
        elif self.language == 'English':
            content = self.translator.translate('Vehicle brand', src='en', dest='en')
            brand_text = content.text
            brand = input('{}: \r\n'.format(brand_text)).title()
            return brand

    def model(self):
        if self.language == 'Spanish':
            content = self.translator.translate('Vehicle model', src='en', dest='es')
            model_text = content.text
            model = input('{}: \r\n'.format(model_text)).title()
            return model
        elif self.language == 'English':
            content = self.translator.translate('Vehicle model', src='en', dest='en')
            model_text = content.text
            model = input('{}: \r\n'.format(model_text)).title()
            return model

    def plate(self):
        if self.language == 'Spanish':
            content = self.translator.translate('License Plate', src='en', dest='es')
            plate_text = content.text
            plate = input('{}: \r\n'.format(plate_text)).title()
            return plate
        elif self.language == 'English':
            content = self.translator.translate('License Plate', src='en', dest='en')
            plate_text = content.text
            plate = input('{}: \r\n'.format(plate_text)).title()
            return plate

    def year(self):
        if self.language == 'Spanish':
            content1 = self.translator.translate('Year', src='en', dest='es')
            year_text = content1.text
            year = input('{}: \r\n'.format(year_text)).title()

            if year.isdigit():
                return year
            else:
                content2 = self.translator.translate('The year must be written with just numbers', src='en',
                                                     dest='es')
                year_valid = content2.text

                print("{}".format(year_valid))

                year_class = Translations()
                year_class.year()

        elif self.language == 'English':
            content1 = self.translator.translate('Year', src='en', dest='en')
            year_text = content1.text
            year = input('{}: \r\n'.format(year_text)).title()

            if year.isdigit():
                return year
            else:
                content2 = self.translator.translate('The year must be written with just numbers', src='en',
                                                     dest='en')
                year_valid = content2.text

                print("{}".format(year_valid))

                year_class = Translations()
                year_class.year()

    def digit(self):
        translation = Translator()
        identification = 'ID' if self.language == 'English' else 'DNI'
        owner_id = input('{}: \r\n'.format(identification))

        if owner_id.isdigit():
            return owner_id
        else:
            pronoun = 'the'
            sentence = 'must contain only numbers'
            obj = Translations()

            if self.language == 'Spanish':
                content1 = translation.translate(pronoun, src='en', dest='es')
                content2 = translation.translate(sentence, src='en', dest='es')

                pronoun = content1.text
                sentence = content2.text

                print("{} {} {}".format(pronoun, identification, sentence))
                obj.digit()
            elif self.language == 'English':
                content1 = translation.translate(pronoun, src='en', dest='es')
                content2 = translation.translate(sentence, src='en', dest='es')

                pronoun = content1.text
                sentence = content2.text

                print("{} {} {}".format(pronoun, identification, sentence))
                obj.digit()


class Cars(Translations):

    def __init__(self):
        super().__init__()

        translations = Translations()
        translations.start()

        self.first_name = translations.first_name()
        self.last_name = translations.last_name()
        self.owner_id = translations.digit()
        self.brand = translations.brand()
        self.model = translations.model()
        self.year = translations.year()
        self.plate = translations.plate()

        self.filename = Data.file_name()
        self.filetype = FILETYPE
        self.dir_path = PATH
        self.filepath = self.dir_path + '/' + self.filename + self.filetype

    @classmethod
    def exist_file(cls, filepath):
        exist = os.path.isfile(filepath)
        return exist

    @classmethod
    def exist_dir(cls):
        if not os.path.exists(PATH):
            os.makedirs(PATH)

    @classmethod
    def writerow_if(cls, csv_writer):
        writepath = PATH + '/' + Data.file_name() + FILETYPE
        if Cars.exist_file(writepath):    
            pass  
        else:
            csv_writer.writeheader()
    
    def data_dict(self):
        if JSON_LIST[1] == 'English':   
            data = [{'First Name': self.first_name,
                'Last Name': self.last_name,
                'ID': self.owner_id,
                'Brand': self.brand,
                'Model': self.model,
                'Year': self.year,
                'License Plate': self.plate}]
                
            return data

        elif JSON_LIST[1] == 'Spanish':
            data = [{'Nombre': self.first_name,
                'Apellido': self.last_name,
                'DNI': self.owner_id,
                'Marca': self.brand,
                'Modelo': self.model,
                'Anualidad': self.year,
                'Licencia': self.plate}]
                
            return data
        return data
    
    
class Writter(Cars):
    def __init__(self):
        user2 = Cars()
        self.fieldnames = Writter.fieldnames1()
        self.data = user2.data_dict()

    @classmethod
    def fieldnames1(cls):
        if JSON_LIST[1] == 'English':  
            fieldnames = ['First Name', 'Last Name', 'ID', 'Brand', 'Model', 'Year', 'License Plate']
            return fieldnames

        elif JSON_LIST[1] == 'Spanish':
            fieldnames = ['Nombre', 'Apellido', 'DNI', 'Marca', 'Modelo', 'Anualidad', 'Licencia']
            return fieldnames
            
        return fieldnames

    def write_data(self):
        with open(PATH + '/data.csv', 'a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            Cars.writerow_if(csv_writer)
            for i in self.data:
                csv_writer.writerow(i)        


def app():
    Cars.exist_dir()
    user = Writter()
    user.write_data()


app()
