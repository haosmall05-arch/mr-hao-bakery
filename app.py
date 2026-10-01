import streamlit as st

# =====================================================
# MR HÀO BAKERY
# =====================================================

st.set_page_config(
    page_title="MR HÀO Bakery",
    page_icon="🍰",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>
.stApp {
    background-color: #fff8f5;
}

.hero {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    background-color: #ffe5d9;
}

.price {
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 20 LOẠI BÁNH
# =====================================================

cakes = [
    ("Bánh Dâu", 45000, "🍓"),
    ("Chocolate Cake", 50000, "🍫"),
    ("Cheesecake", 55000, "🧀"),
    ("Matcha Cake", 55000, "🍵"),
    ("Bánh Xoài", 45000, "🥭"),
    ("Bánh Việt Quất", 50000, "🫐"),
    ("Bánh Chuối", 40000, "🍌"),
    ("Bánh Dừa", 40000, "🥥"),
    ("Bánh Chanh", 42000, "🍋"),
    ("Bánh Cam", 42000, "🍊"),
    ("Bánh Táo", 45000, "🍎"),
    ("Cupcake", 25000, "🧁"),
    ("Donut", 20000, "🍩"),
    ("Tiramisu", 60000, "🍰"),
    ("Croissant", 30000, "🥐"),
    ("Tart Trứng", 30000, "🥧"),
    ("Bánh Flan", 25000, "🍮"),
    ("Bánh Sinh Nhật", 250000, "🎂"),
    ("Bánh Mật Ong", 45000, "🍯"),
    ("Bánh Kem Dâu", 180000, "🍓")
]


# =====================================================
# GIỎ HÀNG
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero">

<h1>🍰 MR HÀO BAKERY</h1>

<h3>Ngọt ngào trong từng chiếc bánh ❤️</h3>

<p>20 loại bánh • Đặt hàng • Chatbot • Tính tiền tự động</p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# MENU
# =====================================================

st.header("🍰 MENU 20 LOẠI BÁNH")

search = st.text_input(
    "🔎 Tìm bánh",
    placeholder="Ví dụ: dâu, chocolate, cupcake..."
)

for i, (name, price, emoji) in enumerate(cakes):

    if search and search.lower() not in name.lower():
        continue

    with st.expander(
        f"{emoji} {name} — {price:,} VNĐ"
    ):

        st.subheader(
            f"{emoji} {name}"
        )

        st.write(
            f"💰 Giá: **{price:,} VNĐ**"
        )

        quantity = st.number_input(
            "Số lượng",
            min_value=0,
            max_value=20,
            value=0,
            key=f"cake_{i}"
        )

        if quantity > 0:

            st.session_state.cart[name] = {
                "price": price,
                "quantity": quantity
            }

        elif name in st.session_state.cart:

            del st.session_state.cart[name]


# =====================================================
# GIỎ HÀNG
# =====================================================

st.divider()

st.header("🛒 GIỎ HÀNG")

total = 0

if not st.session_state.cart:

    st.info(
        "Giỏ hàng đang trống."
    )

else:

    for name, item in st.session_state.cart.items():

        subtotal = (
            item["price"] *
            item["quantity"]
        )

        total += subtotal

        st.write(
            f"🍰 {name} | "
            f"{item['quantity']} × "
            f"{item['price']:,} = "
            f"**{subtotal:,} VNĐ**"
        )

st.success(
    f"💰 TỔNG TIỀN: {total:,} VNĐ"
)


# =====================================================
# THÔNG TIN KHÁCH
# =====================================================

st.header("👤 THÔNG TIN KHÁCH HÀNG")

customer = st.text_input(
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


if st.button(
    "🍰 XÁC NHẬN ĐẶT BÁNH",
    use_container_width=True
):

    if total == 0:

        st.warning(
            "Bạn chưa chọn bánh."
        )

    elif not customer:

        st.warning(
            "Vui lòng nhập tên."
        )

    elif not phone:

        st.warning(
            "Vui lòng nhập số điện thoại."
        )

    else:

        st.success(
            "🎉 Đặt bánh thành công!"
        )

        st.write(
            f"👤 Người đặt: {customer}"
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


# =====================================================
# CHATBOT
# =====================================================

st.divider()

st.header("🤖 CHATBOT MR HÀO")

st.caption(
    "Trợ lý tự động — 100 câu hỏi thường gặp"
)


# =====================================================
# 100 CÂU HỎI
# =====================================================

FAQ = [

# 1-10
("xin chào", "Xin chào 👋! MR HÀO rất vui được phục vụ bạn."),
("chào", "Xin chào 👋! Bạn muốn tìm loại bánh nào?"),
("hello", "Hello 👋! Chào mừng bạn đến MR HÀO Bakery."),
("mr hào là gì", "MR HÀO là cửa hàng bánh ngọt trong dự án này."),
("có những bánh gì", "MR HÀO hiện có 20 loại bánh trong menu."),
("có bao nhiêu loại bánh", "Hiện tại cửa hàng có 20 loại bánh."),
("menu", "Bạn hãy kéo lên phần MENU để xem đầy đủ sản phẩm."),
("bánh nào rẻ nhất", "Trong menu hiện tại, Donut có giá 20.000 VNĐ."),
("bánh nào đắt nhất", "Bánh Sinh Nhật hiện có giá 250.000 VNĐ."),
("giá bánh", "Giá bánh hiện dao động từ 20.000 đến 250.000 VNĐ."),

# 11-20
("bánh dâu", "🍓 Bánh Dâu có giá 45.000 VNĐ."),
("chocolate", "🍫 Chocolate Cake có giá 50.000 VNĐ."),
("cheesecake", "🧀 Cheesecake có giá 55.000 VNĐ."),
("matcha", "🍵 Matcha Cake có giá 55.000 VNĐ."),
("bánh xoài", "🥭 Bánh Xoài có giá 45.000 VNĐ."),
("việt quất", "🫐 Bánh Việt Quất có giá 50.000 VNĐ."),
("bánh chuối", "🍌 Bánh Chuối có giá 40.000 VNĐ."),
("bánh dừa", "🥥 Bánh Dừa có giá 40.000 VNĐ."),
("bánh chanh", "🍋 Bánh Chanh có giá 42.000 VNĐ."),
("bánh cam", "🍊 Bánh Cam có giá 42.000 VNĐ."),

# 21-30
("bánh táo", "🍎 Bánh Táo có giá 45.000 VNĐ."),
("cupcake", "🧁 Cupcake có giá 25.000 VNĐ."),
("donut", "🍩 Donut có giá 20.000 VNĐ."),
("tiramisu", "🍰 Tiramisu có giá 60.000 VNĐ."),
("croissant", "🥐 Croissant có giá 30.000 VNĐ."),
("tart trứng", "🥧 Tart Trứng có giá 30.000 VNĐ."),
("flan", "🍮 Bánh Flan có giá 25.000 VNĐ."),
("bánh sinh nhật", "🎂 Bánh Sinh Nhật có giá 250.000 VNĐ."),
("bánh mật ong", "🍯 Bánh Mật Ong có giá 45.000 VNĐ."),
("bánh kem dâu", "🍓 Bánh Kem Dâu có giá 180.000 VNĐ."),

# 31-40
("bánh dưới 30000", "Bạn có thể chọn Donut 20.000 VNĐ, Cupcake 25.000 VNĐ hoặc Flan 25.000 VNĐ."),
("bánh dưới 50000", "Có nhiều lựa chọn như Dâu, Xoài, Chuối, Dừa, Chanh, Cam, Táo, Cupcake, Donut và Flan."),
("bánh dưới 100000", "Phần lớn menu hiện tại có giá dưới 100.000 VNĐ."),
("bánh 50000", "Chocolate Cake có giá 50.000 VNĐ và Bánh Việt Quất cũng có giá 50.000 VNĐ."),
("bánh 60000", "Tiramisu có giá 60.000 VNĐ."),
("bánh 100000", "MR HÀO có nhiều bánh dưới 100.000 VNĐ."),
("bánh 200000", "Bánh Kem Dâu có giá 180.000 VNĐ."),
("bánh 250000", "Bánh Sinh Nhật có giá 250.000 VNĐ."),
("bánh rẻ", "Bạn có thể thử Donut, Cupcake hoặc Flan."),
("bánh cao cấp", "Bạn có thể tham khảo Bánh Sinh Nhật hoặc Bánh Kem Dâu."),

# 41-50
("bánh cho sinh nhật", "🎂 Bạn có thể chọn Bánh Sinh Nhật hoặc Bánh Kem Dâu."),
("bánh cho bạn bè", "🎁 Cupcake, Donut hoặc Chocolate Cake là những lựa chọn dễ chia sẻ."),
("bánh làm quà", "🎁 Bạn có thể tham khảo Tiramisu, Cheesecake hoặc Bánh Kem Dâu."),
("bánh cho gia đình", "🍰 Bạn có thể chọn Bánh Sinh Nhật hoặc Cheesecake."),
("bánh trái cây", "🍓 Bạn có thể chọn Bánh Dâu, Xoài, Việt Quất, Táo, Cam hoặc Chanh."),
("bánh chocolate", "🍫 Chocolate Cake là lựa chọn dành cho người thích chocolate."),
("bánh matcha", "🍵 Matcha Cake có giá 55.000 VNĐ."),
("bánh ngọt", "MR HÀO có nhiều loại bánh ngọt trong menu."),
("bánh nhỏ", "Bạn có thể chọn Cupcake, Donut hoặc Flan."),
("bánh lớn", "Bạn có thể tham khảo Bánh Sinh Nhật hoặc Bánh Kem Dâu."),

# 51-60
("cách đặt hàng", "🛒 Chọn bánh → chọn số lượng → nhập thông tin → bấm XÁC NHẬN ĐẶT BÁNH."),
("mua bánh", "Bạn hãy chọn bánh trong MENU rồi chọn số lượng."),
("thêm vào giỏ", "Chọn số lượng lớn hơn 0 ở sản phẩm muốn mua."),
("giỏ hàng ở đâu", "🛒 Giỏ hàng nằm bên dưới phần MENU."),
("tổng tiền ở đâu", "💰 Tổng tiền được hiển thị ngay dưới giỏ hàng."),
("tính tiền", "Website tự tính giá từng món và tổng đơn hàng."),
("tính tổng", "Website tự cộng tất cả sản phẩm trong giỏ hàng."),
("đổi số lượng", "Bạn có thể thay đổi số lượng tại ô Số lượng của sản phẩm."),
("xóa bánh", "Đưa số lượng của bánh về 0 để bỏ bánh khỏi giỏ."),
("đặt nhiều bánh", "Bạn có thể chọn số lượng cho nhiều loại bánh cùng lúc."),

# 61-70
("tên người mua", "Bạn nhập tên ở phần THÔNG TIN KHÁCH HÀNG."),
("nhập tên", "Hãy nhập họ và tên vào ô Họ và tên."),
("số điện thoại", "Bạn nhập số điện thoại ở phần thông tin khách hàng."),
("địa chỉ", "Bạn nhập địa chỉ nhận bánh vào ô Địa chỉ nhận bánh."),
("ghi chú", "Bạn có thể ghi yêu cầu thêm vào ô Ghi chú."),
("xác nhận đơn", "Sau khi kiểm tra thông tin, bấm XÁC NHẬN ĐẶT BÁNH."),
("đặt thành công", "Website sẽ hiển thị thông báo khi thông tin cơ bản hợp lệ."),
("đơn hàng của ai", "Đơn hàng thuộc về người có tên được nhập trong thông tin khách hàng."),
("thông tin khách hàng", "Website cần tên, số điện thoại và địa chỉ để tạo thông tin đơn."),
("sửa thông tin", "Bạn có thể sửa các ô thông tin trước khi xác nhận đơn."),

# 71-80
("giao hàng", "🚚 Thông tin giao hàng cần được cửa hàng xác nhận theo khu vực."),
("ship", "🚚 Phí giao hàng có thể phụ thuộc vào khu vực."),
("phí giao hàng", "Phí giao hàng chưa được tính tự động trong bản demo này."),
("thanh toán", "💳 Phương thức thanh toán cần được cửa hàng xác nhận khi nhận đơn."),
("tiền mặt", "Bạn có thể thỏa thuận thanh toán tiền mặt với cửa hàng."),
("chuyển khoản", "Bạn chỉ nên chuyển khoản theo thông tin thanh toán chính thức của cửa hàng."),
("nhận bánh", "Địa chỉ nhận bánh được nhập trong phần thông tin khách hàng."),
("thời gian giao", "Thời gian giao cần được cửa hàng xác nhận theo từng đơn."),
("đặt trước", "Bạn có thể liên hệ cửa hàng để hỏi về việc đặt bánh trước."),
("hủy đơn", "Nếu muốn hủy đơn, hãy liên hệ cửa hàng càng sớm càng tốt."),

# 81-90
("mở cửa", "⏰ Bản demo đặt giờ hoạt động từ 08:00 đến 21:00."),
("giờ mở cửa", "⏰ 08:00 – 21:00 mỗi ngày trong bản demo."),
("địa chỉ cửa hàng", "📍 Địa chỉ cửa hàng cần được chủ shop cập nhật."),
("liên hệ", "📞 Bạn có thể cập nhật số liên hệ chính thức của MR HÀO trong website."),
("chủ shop", "👨‍🍳 MR HÀO là tên thương hiệu của cửa hàng trong dự án."),
("chatbot là gì", "🤖 Đây là trợ lý tự động trả lời các câu hỏi thường gặp."),
("chatbot có miễn phí không", "Có. Phiên bản này sử dụng Python và Streamlit, không cần API AI."),
("chatbot có nhớ không", "Chatbot lưu lịch sử trong phiên sử dụng hiện tại."),
("chatbot trả lời thế nào", "Bot tìm các từ khóa trong câu hỏi và chọn câu trả lời phù hợp."),
("không hiểu câu hỏi", "Bạn hãy thử hỏi về giá, bánh, đặt hàng, giao hàng hoặc thanh toán."),

# 91-100
("cảm ơn", "❤️ MR HÀO cảm ơn bạn!"),
("thank you", "❤️ You're welcome!"),
("tạm biệt", "👋 Tạm biệt! Hẹn gặp lại tại MR HÀO Bakery."),
("gợi ý bánh", "⭐ Bạn thích trái cây có thể thử Bánh Dâu; thích chocolate thử Chocolate Cake."),
("nên mua bánh nào", "Bạn có thể chọn theo khẩu vị và ngân sách của mình."),
("bánh ngon nhất", "MR HÀO không xếp hạng bánh nào là ngon nhất; bạn có thể chọn theo sở thích."),
("bánh yêu thích", "Bạn có thể chọn bánh yêu thích bằng cách xem menu và thử từng loại."),
("có 20 bánh không", "Có. Menu demo hiện có đúng 20 loại bánh."),
("website này làm bằng gì", "Website được xây dựng bằng Python và Streamlit."),
("ai làm website", "Đây là dự án học tập MR HÀO Bakery được xây dựng bằng GitHub và Streamlit.")
]


# =====================================================
# HÀM CHATBOT
# =====================================================

def chatbot_answer(question):

    q = question.lower().strip()

    # Ưu tiên câu hỏi gần đúng
    for keyword, answer in FAQ:

        if keyword in q:
            return answer

    return (
        "🤖 Mình chưa tìm thấy câu trả lời phù hợp.\n\n"
        "Bạn có thể hỏi về:\n"
        "🍰 tên bánh\n"
        "💰 giá bánh\n"
        "🛒 đặt hàng\n"
        "🚚 giao hàng\n"
        "💳 thanh toán\n"
        "👤 thông tin khách hàng\n"
        "📞 liên hệ"
    )


# =====================================================
# LỊCH SỬ CHAT
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "👋 Xin chào! Mình là trợ lý MR HÀO.\n\n"
            "Bạn có thể hỏi mình hơn 100 câu về bánh và đặt hàng."
        }
    ]


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


question = st.chat_input(
    "Nhập câu hỏi..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    answer = chatbot_answer(
        question
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()


# =====================================================
# QUẢN TRỊ
# =====================================================

st.divider()

st.header("🔐 KHU VỰC QUẢN TRỊ")

password = st.text_input(
    "Mật khẩu",
    type="password"
)

# CHỈ DÙNG CHO BẢN DEMO
DEMO_PASSWORD = "MRHAO2026"

if st.button("🔑 ĐĂNG NHẬP QUẢN TRỊ"):

    if password == DEMO_PASSWORD:

        st.success(
            "✅ Đăng nhập thành công!"
        )

        st.write(
            f"🍰 Số sản phẩm: {len(cakes)}"
        )

        st.write(
            f"🛒 Số loại bánh trong giỏ: "
            f"{len(st.session_state.cart)}"
        )

        st.write(
            f"💰 Tổng giỏ: {total:,} VNĐ"
        )

    else:

        st.error(
            "❌ Mật khẩu không đúng."
        )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "🍰 MR HÀO BAKERY | Built with Python + Streamlit"
)
