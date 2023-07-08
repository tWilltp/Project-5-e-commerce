import stripe
from flask import Flask, jsonify
app = Flask(__name__)
stripe.api_key = "pk_test_51NOGOUI2Zfyzau0l8ZGFhfJfMUqcpyMyBIK7bAbcNGiGsYRfZJqmOYvOTyuItHj40M7fhRMKASr5fYRpthOyC2vQ004yBAXnMl"


@app.route('/create-intent', methods=['POST'])
def createIntent():
    intent = stripe.PaymentIntent.create(
        amount=1099,
        currency='usd',
        automatic_payment_methods={
            'enabled': True,
        },
    )
    return jsonify(client_secret=intent.client_secret)
