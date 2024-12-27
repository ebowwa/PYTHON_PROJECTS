import shopify
from config import SHOP_URL, API_KEY, PASSWORD

def initialize_session():
    shopify.ShopifyResource.set_site(SHOP_URL)
    shopify.Session.setup(api_key=API_KEY, secret=PASSWORD)

def get_all_products():
    return shopify.Product.find()

def get_discount_codes_for_product(product):
    discount_codes = []
    price_rules = shopify.PriceRule.find()
    for rule in price_rules:
        if rule.target_type == 'line_item' and rule.target_selection == 'entitled':
            entitled_product_ids = [collection.id for collection in rule.entitled_product_ids]
            if product.id in entitled_product_ids:
                codes = shopify.DiscountCode.find(price_rule_id=rule.id)
                discount_codes.extend(codes)
    return discount_codes

def get_product_details(product):
    variants = [
        {
            'title': variant.title,
            'sku': variant.sku,
            'price': variant.price,
            'inventory_quantity': variant.inventory_quantity
        } for variant in product.variants
    ]

    discount_codes = get_discount_codes_for_product(product)
    
    return {
        'id': product.id,
        'title': product.title,
        'handle': product.handle,
        'product_type': product.product_type,
        'vendor': product.vendor,
        'status': product.status,
        'variants': variants,
        'discount_codes': [
            {
                'code': code.code,
                'value': code.value,
                'value_type': code.value_type
            } for code in discount_codes
        ]
    }

def list_products_with_discount_codes():
    initialize_session()
    products = get_all_products()
    product_details = [get_product_details(product) for product in products]
    return product_details