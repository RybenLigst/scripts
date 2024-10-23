import string
import secrets

def generate_secure_password(length=12):
    if length < 4:
        raise ValueError("Довжина пароля повинна бути не менше 4 символів")
    
    # Визначаємо набори символів
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Гарантуємо, що в паролі буде хоча б по одному символу з кожної категорії
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Об'єднуємо всі можливі символи
    all_characters = uppercase + lowercase + digits + special

    # Додаємо випадкові символи до досягнення бажаної довжини
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Перемішуємо символи для додаткової безпеки
    secrets.SystemRandom().shuffle(password)

    # Перетворюємо список символів у рядок
    return ''.join(password)

# Приклад використання
if __name__ == "__main__":
    desired_length = 16  # Встановіть бажану довжину пароля
    secure_password = generate_secure_password(desired_length)
    print(f"Згенерований надійний пароль: {secure_password}")
