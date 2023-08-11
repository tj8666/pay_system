from database.models import Transaction
from database.models import Card
from database import get_db

def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db())
    card_from_db = db.query(Card).filter_by(card_number=card_from).first()
    card_to_db = db.query(Card).filter_by(card_number=card_to).first()
    # Checking
    if card_from_db and card_to_db:
        # Checking balance
        if card_from_db.card.balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount

            new_transaction =



