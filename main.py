"Modules"
import os
import csv
import json
from googletrans import Translator
from datetime import datetime

FILETYPE = '.csv'
SETTINGS_FILETYPE = '.json'
USERNAME = os.getlogin()
PATH = 'C:/Users/{}/Documents/Projects/Vehicles'.format(USERNAME)

config = []
datadict = []


class Data:
    "This class contains the fundamental data methods"

    @classmethod
    def settings(cls):
        "Gets language & country from json file"
        with open(PATH + '/config/data_file' + SETTINGS_FILETYPE, 'r') as json_file:
            data = json.load(json_file)
            config.append(data['country'])
            config.append(data['language'])

    @classmethod
    def file_name(cls):
        "Return filename"
        filename = 'data'
        return filename


class Translations:
    "Translate all inputs"
    def __init__(self):
        Data.settings()
        self.username = USERNAME
        self.translator = Translator()
        self.country = config[0]
        self.language = config[1]

    def start(self):
        "Start message"
        start_msg = "Let's start with some information about your vehicle"
        if self.language == 'Spanish':
            content1 = self.translator.translate(start_msg, src='en', dest='es')
            start_text = content1.text
            print(start_text + ': \r\n')
        elif self.language == 'English':
            content1 = self.translator.translate(start_msg, src='en', dest='en')
            start_text = content1.text
            print(start_text + ': \r\n')

    def first_name(self):
        "Translation of Input First Name message"
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
        "Translation of Input Last Name message"
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
        "Translation of Input Brand message"
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
        "Translation of Input Model message"
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
        "Translation of Input Plate message"
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
        "Translation of Input Year message"
        if self.language == 'Spanish':
            content1 = self.translator.translate('Year', src='en', dest='es')
            year_text = content1.text
            year = input('{}: \r\n'.format(year_text)).title()

            if year.isdigit():
                return year
            else:
                content2 = self.translator.translate('Year must be written with numbers', src='en',
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
                content2 = self.translator.translate('Year must be written with numbers', src='en',
                                                     dest='en')
                year_valid = content2.text

                print("{}".format(year_valid))

                year_class = Translations()
                year_class.year()

    def digit(self):
        "ID Translation and Processing"
        translation = Translator()
        identification = 'ID' if self.language == 'English' else 'DNI'
        owner_id = input('{}: \r\n'.format(identification))

        if owner_id.isdigit():
            return owner_id
        else:
            pronoun = 'The'
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
                content1 = translation.translate(pronoun, src='en', dest='en')
                content2 = translation.translate(sentence, src='en', dest='en')

                pronoun = content1.text
                sentence = content2.text

                print("{} {} {}".format(pronoun, identification, sentence))
                obj.digit()


class Cars(Translations):
    "Cars Data class and file/dir methods"

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
        self.date = Cars.datetime_csv()

        self.filename = Data.file_name()
        self.filetype = FILETYPE
        self.dir_path = PATH
        self.filepath = self.dir_path + '/' + self.filename + self.filetype

        datadict.append(self.first_name)
        datadict.append(self.last_name)
        datadict.append(self.owner_id)
        datadict.append(self.brand)
        datadict.append(self.model)
        datadict.append(self.year)
        datadict.append(self.plate)
        datadict.append(self.date)

        self.datadict = datadict

    @classmethod
    def datetime_csv(cls):
        now = datetime.now()
        return now

    @classmethod
    def exist_file(cls, filepath):
        "Exist File"
        exist = os.path.isfile(filepath)
        return exist

    @classmethod
    def exist_dir(cls):
        "Exist Dir"
        if not os.path.exists(PATH):
            os.makedirs(PATH)


class Writter(Cars):
    "Final Data Processing"
    def __init__(self):
        super().__init__()
        self.fieldnames = Writter.fieldnames1()
        self.data = Writter.data_dict()

    @classmethod
    def fieldnames1(cls):
        "Fieldnames by Language"
        user_language = config[1]
        if user_language == 'English':
            fieldnames = ['First Name','Last Name', 'ID', 'Brand', 'Model', 'Year', 'License Plate', 'Date']
            return fieldnames

        elif user_language == 'Spanish':
            fieldnames = ['Nombre', 'Apellido', 'DNI', 'Marca', 'Modelo', 'Anualidad', 'Licencia', 'Fecha']
            return fieldnames
        return fieldnames
    
    @classmethod
    def data_dict(cls):
        "Dict Data by Language"
        if config[1] == 'English':
            data = [{'First Name': datadict[0],
                'Last Name': datadict[1],
                'ID': datadict[2],
                'Brand': datadict[3],
                'Model': datadict[4],
                'Year': datadict[5],
                'License Plate': datadict[6],
                'Date': datadict[7]}]
            return data

        elif config[1] == 'Spanish':
            data = [{'Nombre': datadict[0],
                'Apellido': datadict[1],
                'DNI': datadict[2],
                'Marca': datadict[3],
                'Modelo': datadict[4],
                'Anualidad': datadict[5],
                'Licencia': datadict[6],
                'Fecha': datadict[7]}]

            return data
        return data

    def write_data(self):
        "Write Data"
        writepath = PATH + '/' + Data.file_name() + FILETYPE

        if Cars.exist_file(writepath):
            with open(PATH + '/data.csv', 'a', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                for i in self.data:
                    csv_writer.writerow(i)
        else:
            with open(PATH + '/data.csv', 'a', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                csv_writer.writeheader()
                for i in self.data:
                    csv_writer.writerow(i)

def app():
    "APP"
    Cars.exist_dir()
    user = Writter()
    user.write_data()


app()
