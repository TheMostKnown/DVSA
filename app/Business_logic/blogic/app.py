from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super secret key'


# Sample products data
products = [
    {"id": 1, "name": "Warm gloves", "description": "Very useful during winter!", "price": 10},
    {"id": 2, "name": "Flag", "description": "TrY-To-GeT-MeEeE", "price": 100},
    {"id": 3, "name": "Shoes", "description": "Best of the market", "price": 40},
    {"id": 4, "name": "Cup of tee", "description": "Sit and have some rest", "price": 5},
    {"id": 5, "name": "Piece of Gold", "description": "Only for VERY RICH", "price": 20000},
    {"id": 6, "name": "Gift card ($15)", "description": "You can share with friends!", "price": 15}
]

# Sample user data
user = {"name": "User", "balance": 50}

# Cart to store products added by the user
cart = []

discount = 0

def get_product_by_id(id):
    for product in products:
    	if product["id"] == id:
    	    return product
    return None

@app.route('/')
def index():
    return render_template('index.html', products=products, user=user, cart_count=len(cart))

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Retrieve product information based on product_id (You may have a function for this)
    product = get_product_by_id(product_id)

    if product:
        cart.append(product)
        flash('Product added to cart!', 'success')
    else:
        flash('Product not found!', 'error')

    return redirect(url_for('index'))
    
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    cart.clear()

    return redirect(url_for('index'))
    
def total_price_counter(discount):
    base = sum([product['price'] for product in cart])
    if discount > base:
        discount = base
    if base > 1000000:
        base -= 2000000
    return base - discount
    

@app.route('/cart', methods=['GET', 'POST'])
def user_cart():
    global discount
    if request.method == 'GET':
        discount = 0

    if request.method == 'POST':
        discount_code = request.form.get('discount_code')
        if discount_code == 'DISCOUNT10':
            discount += 10

    total_price = total_price_counter(discount)

    return render_template('cart.html', user=user, products=cart, total_price=total_price, discount=discount)


@app.route('/buy')
def buy():
    global discount
    total_price = total_price_counter(discount)
         

    if user['balance'] >= total_price:
        message = "You can buy all the products in your cart!"
        user['balance'] -= max(total_price, 0)
        for item in cart:
            if item["id"] == 6:
                message += "\n You've bought a Gift Card! Your balance was enlarged!"
                user['balance'] += 15
        
        if discount > 10:
            discount = 0
            message += "\nFLAG1: sne{y0u_4r3_d1sc0unt_4bus3r_u72hd9ao0}"
        if (total_price < 0) and len(cart) > 50:
            message += "\nFLAG2: sne{0h_n0_y0u_h4v3_0v3rfl0w3d_my_c4rt_os8sdfy40df9}"
        if (user['balance'] >= 100):
            message += "\nFLAG3: sne{0h_l00k_h3r3_1s_4_g1ft_c0d3_3nj03r_sdas89s8df7}"
        cart.clear()
    else:
        message = "Insufficient balance to buy all the products in your cart."

    return render_template('purchase.html', message=message, user=user, total_price=total_price)

if __name__ == '__main__':    
    app.run(debug=True)
