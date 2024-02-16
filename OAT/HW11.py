#задача
#Класс Книга должен содержать информацию о названии, авторе и жанре книги.
# Метод show должен показать информацию об объекте.
# Создайте два разных объекта и вызовите у них метод show

class Book:
    def __init__(self, name, autor, genre):
        self.name = name
        self.autor = autor
        self.genre = genre

    def show(self):
        print(f'Книга "{self.name}" написана автором {self.autor} в жанре {self.genre}.')

my_book = Book('Гиблое место', 'Антон Грановский', 'историческое фентези')
dother_book = Book('Читаем перед сном', 'Евгений Сосновский', 'детские стихотворения')
my_book.show()
dother_book.show()

# задача
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе
# Метод show должен показать информацию об объекте.
# Создайте два разных объекта и вызовите у них метод show

class Bank_account:
    def __init__(self, name, birthday, account_balance, currency):
        self.name = name
        self.birthday = birthday
        self.account_balance = account_balance
        self.currency = currency

    def show(self):
        print(f'Имя клиента банка: {self.name}\nДата рождения: {self.birthday}\nБаланс счета: {self.account_balance}{self.currency}', '\n')

client_1 = Bank_account('Миров Алексей', '2000-05-09', '7800', '$')
client_2 = Bank_account('Lionov Jon', '1995-08-10', '2300', '€')
client_1.show()
client_2.show()



