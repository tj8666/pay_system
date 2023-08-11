from fastapi import Body
from .profile_models import CardDent
from main import app
from .profile_models import UserDent

# User registarion
@app.post('/api/register-user')
async def user_reg(user_data: UserDent):
    print(user_data)
    # After registration give user id

    return {'status': 1, 'message': 'Registration complete'}

# Enter in User account
@app.post('/api/login-user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    # data check
    checker = None
    # If data correct, send User Id and user Data
    return {'status': 1, 'message': 'Logged in'}

# Add card
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    # call func from DB for add card
    result = card_data
    print(card_data)
    # If success
    return {'status': 1, 'message': result}
# get user data
@app.get('/api/user-data')
async def get_user_data(user_id: int):
    pass

# show all or exact user card
@app.get('/api-user-cards')
async def get_user_cards(user_id: int, card_id: int = 0):
    pass
