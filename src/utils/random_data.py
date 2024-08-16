from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(),
        "address": fake.street_address(),
        "full_name": fake.name() + fake.last_name(),
        "telephone": fake.phone_number(),
        "city": fake.city(),
        "country" : 'US',
        "province": 'US-MD',
        "postcode": fake.postcode(),
        "card_number": fake.credit_card_number(card_type="visa"),
        "expiration_date": fake.credit_card_expire(),
        "cvv": fake.credit_card_security_code(),
        "payment": 'Credit Card'
    }