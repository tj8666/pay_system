from main import app
from .transfer_models import P2PDent

# Запрос на перевод денег между картами
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    # Transfer money func
    result = transfer_data
    print(result)
    # If transfer success
    return {'status': 1, 'message': result}

# Func get last user transfers
@app.get('/api/monitoring')
async def user_payments(user_id: int, card_id: int = 0):
    pass

