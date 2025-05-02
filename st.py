# import streamlit as st
# col1,col2=st.columns(2)

# with col1:
#  home = st.button("home")
# with col2:
#  setting = st.button("setting")

# st.title        ("hello fahad!")

# import streamlit as st

# # Sidebar navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# # Display different pages
# if page == "Home":
#     st.title("🏠 code with Fahad")
#     st.write("Welcome to the home page!")

# elif page == "About":
#     st.title("ℹ️ About Page")
#     st.write("This is an example Streamlit app to demonstrate navigation.")

# elif page == "Contact":
#     st.title("📞 Contact Page")
#     st.write("Reach us at: example@example.com")
#     import streamlit as st
# from PIL import Image

# # Load and display the image
# image = Image.open('code')  # Replace with your image file path
# st.image(image, caption='code', use_column_width=True)

import streamlit as st
from PIL import Image
import uuid
import datetime

# --------------------
# Configuration
# --------------------
st.set_page_config(page_title="Fast Food Order", page_icon="🍔", layout="centered")

# --------------------
# Logo
# --------------------
logo = Image.open("log.jpg")
st.image(logo, width=200)
st.title("🍟 Fast Food Delivery App")

# --------------------
# Sidebar Navigation
# --------------------
menu = st.sidebar.radio("Navigation", ["Home", "Menu", "Cart", "Checkout", "About"])

# --------------------
# Menu Items
# --------------------
menu_items = {
    "Burger": 300 ,
    "Pizza": 400,
    "Fries": 150,
    "Hotdog": 350,
    "Cola": 180,
}

# Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Initialize receipt
if "receipt" not in st.session_state:
    st.session_state.receipt = None

# --------------------
# Home Page
# --------------------
if menu == "Home":
    st.header("Welcome to our Fast Food App!")
    st.write("Quick, tasty meals delivered to your door.")

# --------------------
# Menu Page
# --------------------
elif menu == "Menu":
    st.header("🍔 Menu")

    for item, price in menu_items.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{item}** - {price}")
        with col2:
            if st.button(f"Add {item}", key=item):
                st.session_state.cart[item] = st.session_state.cart.get(item, 0) + 1
                st.success(f"{item} added to cart.")

# --------------------
# Cart Page
# --------------------
elif menu == "Cart":
    st.header("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for item, qty in st.session_state.cart.items():
            price = menu_items[item]
            st.write(f"{item} x {qty} = {price * qty:.2f}")
            total += price * qty
        st.write(f"**Subtotal: {total:.2f}**")
    else:
        st.info("Your cart is empty.")

# --------------------
# Checkout Page with Receipt
# --------------------
elif menu == "Checkout":
    st.header("💳 Checkout")

    if not st.session_state.cart:
        st.warning("Your cart is empty.")
    else:
        st.write("**Select payment method:**")
        payment = st.radio("Payment", ["Cash on Delivery"], index=0)

        delivery_fee = 150
        subtotal = sum(menu_items[item] * qty for item, qty in st.session_state.cart.items())
        total = subtotal + delivery_fee

        st.write(f"Subtotal: {subtotal:.2f}")
        st.write(f"Delivery Fee: {delivery_fee:.2f}")
        st.write(f"**Total: {total:.2f}**")

        if st.button("Place Order"):
            order_id = str(uuid.uuid4())[:8].upper()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            receipt = {
                "Order ID": order_id,
                "Time": timestamp,
                "Items": st.session_state.cart.copy(),
                "Payment": payment,
                "Delivery Fee": delivery_fee,
                "Subtotal": subtotal,
                "Total": total
            }

            st.session_state.receipt = receipt
            st.session_state.cart = {}
            st.success("✅ Order placed successfully!")
            st.balloons()

    # Show receipt
    if st.session_state.receipt:
        st.markdown("## 🧾 Order Slip / Receipt")
        st.markdown(f"**Order ID:** `{st.session_state.receipt['Order ID']}`")
        st.markdown(f"**Time:** {st.session_state.receipt['Time']}")
        st.markdown("### Items Ordered:")
        for item, qty in st.session_state.receipt["Items"].items():
            price = menu_items[item]
            st.markdown(f"- {item} x {qty} = {price * qty:.2f}")
        st.markdown(f"**Subtotal:** {st.session_state.receipt['Subtotal']:.2f}")
        st.markdown(f"**Delivery Fee:** {st.session_state.receipt['Delivery Fee']:.2f}")
        st.markdown(f"**Total:** {st.session_state.receipt['Total']:.2f}")
        st.markdown(f"**Payment Method:** {st.session_state.receipt['Payment']}")

# --------------------
# About Page
# --------------------
elif menu == "About":
    st.header("ℹ️ About Us")
    st.write("We deliver fast food with speed and love. Order now and enjoy!")

# --------------------
# Footer
# --------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2025 FastFood Express. All rights reserved.</div>",
    unsafe_allow_html=True
)

