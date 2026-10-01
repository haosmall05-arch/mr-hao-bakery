import streamlit as st

# =========================
# CẤU HÌNH WEBSITE
# =========================

st.set_page_config(
    page_title="MR HÀO Bakery",
    page_icon="🍰",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #fff8f5;
}

h1 {
    text-align: center;
}

.product {
    padding: 15px;
    border-radius: 15px;
    background: white;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# DỮ LIỆU 20 LOẠI BÁNH
# =========================

cakes = [
    {
        "name": "Bánh Dâu",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Bánh Chocolate",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Cheesecake",
        "price": 55000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Matcha",
        "price": 55000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Bánh Xoài",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Việt Quất",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Chuối",
        "price": 40000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Bánh Dừa",
        "price": 40000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Bánh Chanh",
        "price": 42000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Cam",
        "price": 42000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Táo",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Cupcake",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d"
    },
    {
        "name": "Donut",
        "price": 20000,
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b"
    },
    {
        "name": "Tiramisu",
        "price": 60000,
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9"
    },
    {
        "name": "Croissant",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1555507036-ab1f4038808a"
    },
    {
        "name": "Tart Trứng",
        "price": 30000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Flan",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1551024601-bec78aea704b"
    },
    {
        "name": "Bánh Sinh Nhật",
        "price": 250000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Bánh Mật Ong",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Bánh Kem Dâu",
        "price": 180000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    }
]


# =========================
# GIỎ HÀNG
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = {}


# =========================
# TIÊU ĐỀ
# =========================

st.title("🍰 MR HÀO BAKERY")
st.subheader("✨ Ngọt ngào trong từng chiếc bánh ✨")

st.divider()


# =========================
# MENU
# =========================

st.header("🍰 MENU 20 LOẠI BÁNH")

cols = st.columns(2)

for i, cake in enumerate(cakes):

    with cols[i % 2]:

        st.image(
            cake["image"],
            use_container_width=True
        )

        st.subheader(cake["name"])

        st.write(
            f"💰 {cake['price']:,} VNĐ"
        )

        quantity = st.number_input(
            f"Số lượng - {cake['name']}",
            min_value=0,
            max_value=20,
            value=0,
            key=f"qty_{i}"
        )

        if quantity > 0:
            st.session_state.cart[cake["name"]] = {
                "price": cake["price"],
                "quantity": quantity
            }


st.divider()


# =========================
# GIỎ HÀNG
# =========================

st.header("🛒 GIỎ HÀNG")

total = 0

if len(st.session_state.cart) == 0:

    st.info("Giỏ hàng đang trống.")

else:

    for name, item in st.session_state.cart.items():

        subtotal = item["price"] * item["quantity"]

        total += subtotal

        st.write(
            f"🍰 {name} — "
            f"{item['quantity']} × "
            f"{item['price']:,} = "
            f"**{subtotal:,} VNĐ**"
        )


st.divider()

st.subheader(
    f"💰 TỔNG TIỀN: {total:,} VNĐ"
)


# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================

st.header("👤 THÔNG TIN ĐẶT BÁNH")

customer_name = st.text_input(
    "Họ và tên"
)

phone = st.text_input(
    "Số điện thoại"
)

address = st.text_area(
    "Địa chỉ nhận bánh"
)

note = st.text_area(
    "Ghi chú"
)


# =========================
# ĐẶT HÀNG
# =========================

if st.button(
    "🍰 ĐẶT BÁNH",
    use_container_width=True
):

    if total == 0:

        st.warning(
            "Bạn chưa chọn bánh."
        )

    elif customer_name == "":

        st.warning(
            "Vui lòng nhập tên."
        )

    elif phone == "":

        st.warning(
            "Vui lòng nhập số điện thoại."
        )

    else:

        st.success(
            "🎉 Đặt bánh thành công!"
        )

        st.write(
            f"👤 Khách hàng: {customer_name}"
        )

        st.write(
            f"📞 Số điện thoại: {phone}"
        )

        st.write(
            f"📍 Địa chỉ: {address}"
        )

        st.write(
            f"💰 Tổng tiền: {total:,} VNĐ"
        )


# =========================
# CHATBOT
# =========================

st.divider()

st.header("🤖 CHATBOT MR HÀO")

question = st.text_input(
    "Bạn muốn hỏi gì?"
)

if question:

    q = question.lower()

    if "giá" in q:

        st.info(
            "🤖 Bạn có thể xem giá của từng bánh ngay "
            "trong menu phía trên nhé!"
        )

    elif "xin chào" in q or "hello" in q:

        st.success(
            "🤖 Xin chào! Mình là trợ lý của MR HÀO 🍰"
        )

    elif "bánh" in q:

        st.info(
            "🤖 MR HÀO hiện có 20 loại bánh. "
            "Bạn hãy xem menu phía trên nhé!"
        )

    elif "đặt" in q:

        st.info(
            "🤖 Bạn chọn bánh → nhập số lượng → "
            "điền thông tin → bấm ĐẶT BÁNH."
        )

    else:

        st.info(
            "🤖 Mình chưa hiểu câu hỏi. "
            "Bạn có thể hỏi về bánh, giá hoặc cách đặt bánh nhé!"
        )


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "© 2026 MR HÀO BAKERY | Made with ❤️ and Streamlit"
)
