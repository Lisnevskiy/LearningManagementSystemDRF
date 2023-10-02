import stripe
from config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_url_payment(data: dict) -> str:
    """
    Создает URL для оплаты через Stripe Checkout.
    Args:
        data (dict): Словарь с данными для создания оплаты. Должен содержать следующие ключи:
            - 'name' (str): Название продукта или услуги.
            - 'amount' (int): Сумма оплаты в центах (например, 100 центов = 1 доллар).
    Returns:
        str: URL для оплаты через Stripe Checkout.
    """
    # Создание продукта в Stripe с указанным названием.
    product = stripe.Product.create(name=data['name'])

    # Создание цены для продукта с указанной суммой и валютой.
    price = stripe.Price.create(
        unit_amount=data['amount'],
        currency='usd',
        product=product.id
    )

    # Создание сессии оплаты через Stripe Checkout.
    payment_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': price.id,
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'http://127.0.0.1:8000/courses',  # URL для успешного завершения оплаты
        cancel_url=f'http://127.0.0.1:8000/courses',   # URL для отмены оплаты
    )

    # URL для оплаты.
    return payment_session.url
