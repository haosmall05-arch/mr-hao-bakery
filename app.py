import streamlit as st

# =========================================================
# 1. CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="MR HÀO Bakery",
    page_icon="🍰",
    layout="wide"
)

# =========================================================
# 2. CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #fff8f5;
}

h1 {
    text-align: center;
}

.hero {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    background: #ffe5d9;
    margin-bottom: 25px;
}

.price {
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. 20 SẢN PHẨM
# =========================================================

cakes = [
    {
        "name": "Bánh Dâu",
        "price": 45000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Chocolate Cake",
        "price": 50000,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Cheesecake",
        "price": 55000,
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187"
    },
    {
        "name": "Matcha Cake",
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


# =========================================================
# 4. GIỎ HÀNG
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}


# =========================================================
# 5. HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>🍰 MR HÀO BAKERY</h1>

<h3>Ngọt ngào trong từng chiếc bánh ❤️</h3>

<p>20 loại bánh • Đặt hàng nhanh • Tính tiền tự động</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 6. MENU
# =========================================================

st.header("🍰 MENU BÁNH")

search = st.text_input(
    "🔎 Tìm bánh",
    placeholder="Ví dụ: dâu, chocolate, cupcake..."
)

filtered_cakes = cakes

if search:
    filtered_cakes = [
        cake for cake in cakes
        if search.lower() in cake["name"].lower()
    ]


cols = st.columns(2)

for i, cake in enumerate(filtered_cakes):

    with cols[i % 2]:

        st.image(
            cake["image"],
            use_container_width=True
        )

        st.subheader(cake["name"])

        st.markdown(
            f"<div class='price'>💰 {cake['price']:,} VNĐ</div>",
            unsafe_allow_html=True
        )

        quantity = st.number_input(
            f"Số lượng",
            min_value=0,
            max_value=20,
            value=0,
            key=f"quantity_{cake['name']}"
        )

        if quantity > 0:

            st.session_state.cart[cake["name"]] = {
                "price": cake["price"],
                "quantity": quantity
            }

        elif cake["name"] in st.session_state.cart:

            del st.session_state.cart[cake["name"]]


# =========================================================
# 7. GIỎ HÀNG
# =========================================================

st.divider()

st.header("🛒 GIỎ HÀNG")

total = 0

if not st.session_state.cart:

    st.info("Giỏ hàng đang trống.")

else:

    for name, item in st.session_state.cart.items():

        subtotal = (
            item["price"] *
            item["quantity"]
        )

        total += subtotal

        st.write(
            f"🍰 **{name}** — "
            f"{item['quantity']} × "
            f"{item['price']:,} = "
            f"**{subtotal:,} VNĐ**"
        )


st.success(
    f"💰 TỔNG ĐƠN HÀNG: {total:,} VNĐ"
)


# =========================================================
# 8. THÔNG TIN KHÁCH
# =========================================================

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
    "Ghi chú đơn hàng"
)


if st.button(
    "🍰 XÁC NHẬN ĐẶT BÁNH",
    use_container_width=True
):

    if total <= 0:

        st.warning(
            "Bạn chưa chọn bánh."
        )

    elif customer_name.strip() == "":

        st.warning(
            "Bạn chưa nhập tên."
        )

    elif phone.strip() == "":

        st.warning(
            "Bạn chưa nhập số điện thoại."
        )

    else:

        st.success(
            "🎉 Đặt hàng thành công!"
        )

        st.write(
            f"👤 Người đặt: {customer_name}"
        )

        st.write(
            f"📞 SĐT: {phone}"
        )

        st.write(
            f"📍 Địa chỉ: {address}"
        )

        st.write(
            f"💰 Tổng tiền: {total:,} VNĐ"
        )


# =========================================================
# 9. CHATBOT FAQ
# =========================================================

st.divider()

st.header("🤖 CHATBOT MR HÀO")

st.caption(
    "Trợ lý tự động — miễn phí, không cần API AI"
)


# Lịch sử trò chuyện

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Xin chào 👋 Mình là trợ lý MR HÀO. "
            "Bạn có thể hỏi mình về bánh, giá, đặt hàng, "
            "giao hàng hoặc thanh toán nhé!"
        }
    ]


# Hiển thị lịch sử

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# Người dùng nhập

question = st.chat_input(
    "Ví dụ: Bánh dâu bao nhiêu tiền?"
)


# =========================================================
# 10. BỘ NÃO CHATBOT
# =========================================================

def chatbot_answer(question):

    q = question.lower().strip()

    # Chào hỏi

    if any(
        word in q
        for word in [
            "xin chào",
            "chào",
            "hello",
            "hi"
        ]
    ):

        return (
            "👋 Xin chào! "
            "Mình là trợ lý MR HÀO Bakery. "
            "Bạn muốn hỏi gì về bánh?"
        )


    # Giá bánh dâu

    if "dâu" in q:

        return (
            "🍓 Bánh Dâu: 45.000 VNĐ.\n\n"
            "Bạn có thể chọn số lượng ở MENU "
            "và thêm vào đơn hàng."
        )


    # Chocolate

    if "chocolate" in q:

        return (
            "🍫 Chocolate Cake: 50.000 VNĐ."
        )


    # Cheesecake

    if "cheesecake" in q:

        return (
            "🧀 Cheesecake: 55.000 VNĐ."
        )


    # Matcha

    if "matcha" in q:

        return (
            "🍵 Matcha Cake: 55.000 VNĐ."
        )


    # Tiramisu

    if "tiramisu" in q:

        return (
            "🍰 Tiramisu: 60.000 VNĐ."
        )


    # Cupcake

    if "cupcake" in q:

        return (
            "🧁 Cupcake: 25.000 VNĐ."
        )


    # Donut

    if "donut" in q:

        return (
            "🍩 Donut: 20.000 VNĐ."
        )


    # Sinh nhật

    if (
        "sinh nhật" in q
        or "sinh nhat" in q
    ):

        return (
            "🎂 MR HÀO có Bánh Sinh Nhật "
            "giá 250.000 VNĐ và Bánh Kem Dâu "
            "giá 180.000 VNĐ."
        )


    # Hỏi giá chung

    if "giá" in q:

        return (
            "💰 MR HÀO có bánh từ "
            "20.000 VNĐ đến 250.000 VNĐ. "
            "Bạn có thể xem MENU phía trên."
        )


    # Đặt hàng

    if (
        "đặt hàng" in q
        or "dat hang" in q
        or "mua" in q
    ):

        return (
            "🛒 Cách đặt bánh:\n\n"
            "1️⃣ Chọn bánh.\n"
            "2️⃣ Chọn số lượng.\n"
            "3️⃣ Nhập họ tên.\n"
            "4️⃣ Nhập số điện thoại.\n"
            "5️⃣ Nhập địa chỉ.\n"
            "6️⃣ Bấm XÁC NHẬN ĐẶT BÁNH."
        )


    # Giao hàng

    if (
        "giao hàng" in q
        or "giao hang" in q
        or "ship" in q
    ):

        return (
            "🚚 Thông tin giao hàng sẽ được "
            "MR HÀO xác nhận với khách khi nhận đơn. "
            "Phí giao hàng có thể phụ thuộc vào khu vực."
        )


    # Thanh toán

    if (
        "thanh toán" in q
        or "thanh toan" in q
        or "trả tiền" in q
    ):

        return (
            "💳 Bạn hãy xác nhận phương thức "
            "thanh toán với cửa hàng khi đặt đơn."
        )


    # Giờ mở cửa

    if (
        "mở cửa" in q
        or "mo cua" in q
        or "giờ" in q
    ):

        return (
            "⏰ Giờ hoạt động: "
            "08:00 – 21:00 mỗi ngày."
        )


    # Địa chỉ

    if "địa chỉ" in q:

        return (
            "📍 Địa chỉ cửa hàng sẽ được "
            "MR HÀO cập nhật tại phần thông tin cửa hàng."
        )


    # Liên hệ

    if (
        "liên hệ" in q
        or "lien he" in q
        or "số điện thoại" in q
    ):

        return (
            "📞 Bạn có thể nhập số điện thoại "
            "của mình trong phần ĐẶT BÁNH để cửa hàng liên hệ."
        )


    # Gợi ý

    if (
        "gợi ý" in q
        or "goi y" in q
        or "nên mua" in q
    ):

        return (
            "⭐ Nếu bạn thích vị trái cây: "
            "Bánh Dâu hoặc Bánh Xoài.\n\n"
            "🍫 Nếu thích vị đậm: Chocolate Cake.\n\n"
            "☕ Nếu thích vị cà phê: Tiramisu."
        )


    # Cảm ơn

    if (
        "cảm ơn" in q
        or "cam on" in q
    ):

        return (
            "❤️ MR HÀO cảm ơn bạn! "
            "Chúc bạn có một ngày thật ngọt ngào!"
        )


    # Không hiểu

    return (
        "🤖 Mình chưa hiểu câu hỏi này.\n\n"
        "Bạn có thể hỏi:\n"
        "• Bánh dâu bao nhiêu tiền?\n"
        "• Có bánh sinh nhật không?\n"
        "• Cách đặt hàng?\n"
        "• Có giao hàng không?\n"
        "• Thanh toán thế nào?\n"
        "• Giờ mở cửa?\n"
        "• Gợi ý bánh cho tôi."
    )


# =========================================================
# 11. XỬ LÝ CHAT
# =========================================================

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    answer = chatbot_answer(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()


# =========================================================
# 12. KHU VỰC QUẢN TRỊ
# =========================================================

st.divider()

st.header("🔐 KHU VỰC QUẢN TRỊ")

password = st.text_input(
    "Mật khẩu quản trị",
    type="password"
)

# Mật khẩu mẫu cho bản thử nghiệm
ADMIN_PASSWORD = "MRHAO2026"

if st.button("🔑 ĐĂNG NHẬP"):

    if password == ADMIN_PASSWORD:

        st.success(
            "✅ Đăng nhập quản trị thành công!"
        )

        st.write(
            f"📦 Số sản phẩm: {len(cakes)}"
        )

        st.write(
            f"🛒 Số loại bánh trong giỏ: "
            f"{len(st.session_state.cart)}"
        )

        st.write(
            f"💰 Tổng giỏ hiện tại: "
            f"{total:,} VNĐ"
        )

    else:

        st.error(
            "❌ Mật khẩu không đúng."
        )


# =========================================================
# 13. FOOTER
# =========================================================

st.divider()

st.caption(
    "🍰 MR HÀO BAKERY • Made with Streamlit"
)
