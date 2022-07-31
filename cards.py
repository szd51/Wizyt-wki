from faker import Faker

faker = Faker ('pl_PL')

class BaseContact:
    def __init__(self, first_name, last_name, phone_number_priv, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number_priv = phone_number_priv
        self.email = email

    def __str__ (self):
        return f'{self.first_name} {self.last_name} {self.phone_number_priv} {self.email}'

    def contact (self):
        return (f'Wybieram numer {self.phone_number_priv} i dzwonię do {self.first_name} {self.last_name}')

    def workcontact(self):
        return (f'Wybieram numer {self.phone_number_work} do firmy {self.company} i dzwonię do {self.first_name} {self.last_name}')

    @property
    def label_lenght(self):
        return ([len(self.first_name) + len(self.last_name)])

class BuissnesContact(BaseContact):
    def __init__(self, company, job, phone_number_work, *args, **kwargs):
        super(). __init__ (*args, **kwargs)
        self.company = company
        self.job = job
        self.phone_number_work = phone_number_work

persons = []

for i in range (3):
    person = BuissnesContact(first_name = faker.first_name(), last_name = faker.last_name(), phone_number_priv = faker.phone_number(), email = faker.email(), company = faker.company(), job = faker.job(), phone_number_work = faker.phone_number())
    persons.append(person)


for person in persons:
    print(person)
    print(person.contact())
    print(person.workcontact())
    print(person.label_lenght)

def create_contact(kind, how_many):
    contacts = []
    for i in range(how_many):
        if kind == 'd':
            contact = BaseContact(first_name = faker.first_name(), last_name = faker.last_name(), phone_number_priv = faker.phone_number(), email = faker.email())
            contacts.append(contact)
        elif kind == 'b':
            contact = BuissnesContact(first_name = faker.first_name(), last_name = faker.last_name(), phone_number_priv = faker.phone_number(), email = faker.email(), company = faker.company(), job = faker.job(), phone_number_work = faker.phone_number())
            contacts.append(contact)

if __name__ == "__main__":
    kind = input("Jaki rodzaj wizytówki utworzyć? b - biznesowa, d - domowa: ")
    how_many = int(input('Proszę podaj liczbę wizytówek do stworzenia '))
    contacts = create_contact(kind, how_many)
    print (contacts)