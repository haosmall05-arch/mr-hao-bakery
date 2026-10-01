
import streamlit as st
import requests
import re

# =========================================================
# MR HÀO BAKERY - STREAMLIT APP
# =========================================================

st.set_page_config(
    page_title="MR HÀO Bakery",
    page_icon="🍰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CSS - FIX FONT / TEXT INVISIBLE ON MOBILE
# =========================================================

st.markdown("""
<style>
/* Nền toàn trang */
.stApp {
    background: #fff8f5 !important;
    color: #3b2923 !important;
}

/* Tất cả chữ mặc định */
.stApp,
.stApp p,
.stApp span,
.stApp label,
.stApp div,
.stApp li,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #3b2923 !important;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #ffe0d2, #fff1ea);
    border: 1px solid #ffd0bd;
    border-radius: 22px;
    padding: 28px 18px;
    text-align: center;
    margin: 8px 0 22px 0;
    box-shadow: 0 5px 18px rgba(120, 70, 40, 0.08);
}

.hero h1 {
    color: #8b4513 !important;
    font-size: 34px !important;
    margin-bottom: 8px !important;
}

.hero h3,
.hero p {
    color: #6f4030 !important;
}

/* Tiêu đề */
h1, h2, h3 {
    color: #7b3f24 !important;
}

/* Input */
.stTextInput label,
.stTextArea label,
.stNumberInput label {
    color: #5b392d !important;
    font-weight: 600 !important;
}

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: #ffffff !important;
    color: #2d211d !important;
    -webkit-text-fill-color: #2d211d !important;
    border: 1px solid #e0b9a8 !important;
    border-radius: 12px !important;
}

/* Placeholder */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #8c7770 !important;
    opacity: 1 !important;
}

/* Select / expander */
[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1px solid #ead0c5 !important;
    border-radius: 15px !important;
    margin-bottom: 8px !important;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary p {
    color: #3b2923 !important;
}

/* Button */
.stButton > button {
    background: #c96f4b !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}

.stButton > button p,
.stButton > button span {
    color: #ffffff !important;
}

/* Thông báo */
.stAlert,
.stAlert p,
.stAlert span {
    color: #3b2923 !important;
}

/* Chat */
.chat-box {
    background: #ffe5d9;
    border: 1px solid #ffd0bd;
    border-radius: 18px;
    padding: 15px;
    margin-top: 10px;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div {
    color: #3b2923 !important;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: #ffffff !important;
}

[data-testid="stChatInput"] textarea {
    background: #ffffff !important;
    color: #2d211d !important;
    -webkit-text-fill-color: #2d211d !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #806d65 !important;
}

/* Giá */
.price {
    color: #b6532f !important;
    font-size: 20px;
    font-weight: 800;
}

/* Card bánh */
.cake-card {
    background: #ffffff;
    border: 1px solid #ead0c5;
    border-radius: 16px;
    padding: 14px;
    min-height: 130px;
    box-shadow: 0 3px 10px rgba(120, 70, 40, 0.05);
}

.cake-card h3,
.cake-card p {
    color: #3b2923 !important;
}

/* Divider */
hr {
    border-color: #e8cfc4 !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #76584c !important;
    padding: 20px 0 40px 0;
}

/* Mobile */
@media (max-width: 700px) {
    .hero h1 {
        font-size: 28px !important;
    }

    .hero {
        padding: 22px 12px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# MENU 20 BÁNH
# =========================================================

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
    ("Bánh Kem Dâu", 180000, "🍓"),
]

cake_map = {name.lower(): (name, price, emoji) for name, price, emoji in cakes}

# =========================================================
# SESSION
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Xin chào! Mình là trợ lý AI của MR HÀO Bakery.\n\n"
                "Bạn có thể hỏi tự nhiên như:\n"
                "• Bánh nào rẻ nhất?\n"
                "• Mình có 100k thì mua gì?\n"
                "• Bánh nào hợp sinh nhật?\n"
                "• Thêm 2 bánh dâu vào giỏ\n"
                "• Giỏ hàng của mình bao nhiêu?"
            ),
        }
    ]

# =========================================================
# HÀM GIỎ HÀNG
# =========================================================

def cart_total():
    return sum(
        item["price"] * item["quantity"]
        for item in st.session_state.cart.values()
    )

def cart_text():
    if not st.session_state.cart:
        return "Giỏ hàng đang trống."

    lines = []
    for name, item in st.session_state.cart.items():
        subtotal = item["price"] * item["quantity"]
        lines.append(
            f"- {name}: {item['quantity']} cái × "
            f"{item['price']:,} VNĐ = {subtotal:,} VNĐ"
        )

    lines.append(f"Tổng: {cart_total():,} VNĐ")
    return "\n".join(lines)

# =========================================================
# TÌM TÊN BÁNH TRONG CÂU
# =========================================================

def find_cake(question):
    q = question.lower().strip()

    # Tên đầy đủ trước
    for name, price, emoji in cakes:
        if name.lower() in q:
            return name, price, emoji

    # Từ khóa ngắn
    aliases = {
        "dâu": "Bánh Dâu",
        "dâu tây": "Bánh Dâu",
        "chocolate": "Chocolate Cake",
        "socola": "Chocolate Cake",
        "sô cô la": "Chocolate Cake",
        "matcha": "Matcha Cake",
        "cheese": "Cheesecake",
        "xoài": "Bánh Xoài",
        "việt quất": "Bánh Việt Quất",
        "chuối": "Bánh Chuối",
        "dừa": "Bánh Dừa",
        "chanh": "Bánh Chanh",
        "cam": "Bánh Cam",
        "táo": "Bánh Táo",
        "cupcake": "Cupcake",
        "donut": "Donut",
        "tiramisu": "Tiramisu",
        "croissant": "Croissant",
        "tart": "Tart Trứng",
        "flan": "Bánh Flan",
        "sinh nhật": "Bánh Sinh Nhật",
        "mật ong": "Bánh Mật Ong",
        "kem dâu": "Bánh Kem Dâu",
    }

    for alias, real_name in aliases.items():
        if alias in q:
            name, price, emoji = cake_map[real_name.lower()]
            return name, price, emoji

    return None

# =========================================================
# XỬ LÝ LỆNH GIỎ HÀNG
# =========================================================

def handle_cart_command(question):
    q = question.lower().strip()

    # Xóa toàn bộ giỏ
    if any(x in q for x in [
        "xóa giỏ", "xoá giỏ", "xóa hết", "xoá hết",
        "clear cart", "bỏ hết"
    ]):
        st.session_state.cart = {}
        return "🗑️ Mình đã xóa toàn bộ giỏ hàng."

    # Xem giỏ
    if any(x in q for x in [
        "giỏ hàng", "gio hang", "cart"
    ]) and not any(x in q for x in [
        "thêm", "them", "bỏ", "bo", "xóa", "xoá", "đổi"
    ]):
        return "🛒 Giỏ hàng hiện tại:\n\n" + cart_text()

    cake = find_cake(q)

    if not cake:
        return None

    name, price, emoji = cake

    # Xóa/bỏ sản phẩm
    if any(x in q for x in [
        "bỏ", "bo ", "xóa", "xoá", "remove"
    ]):
        if name in st.session_state.cart:
            del st.session_state.cart[name]
            return f"🗑️ Đã bỏ {emoji} {name} khỏi giỏ."
        return f"ℹ️ {name} hiện không có trong giỏ."

    # Số lượng: "2 bánh", "2 cái", "x2", "2"
    quantity_match = re.search(
        r"(?:x\s*)?(\d+)\s*(?:cái|chiếc|bánh)?",
        q
    )

    quantity = int(quantity_match.group(1)) if quantity_match else 1

    if quantity > 20:
        quantity = 20

    # Thêm / đặt / mua
    if any(x in q for x in [
        "thêm", "them", "mua", "đặt", "dat", "cho vào giỏ",
        "bỏ vào giỏ", "add"
    ]):
        if name in st.session_state.cart:
            st.session_state.cart[name]["quantity"] += quantity
        else:
            st.session_state.cart[name] = {
                "price": price,
                "quantity": quantity
            }

        new_qty = st.session_state.cart[name]["quantity"]

        return (
            f"✅ Đã thêm {quantity} {emoji} {name} vào giỏ.\n\n"
            f"Số lượng {name}: {new_qty}\n"
            f"💰 Tổng giỏ: {cart_total():,} VNĐ"
        )

    return None

# =========================================================
# SYSTEM PROMPT
# =========================================================

menu_text = "\n".join(
    f"- {emoji} {name}: {price:,} VNĐ"
    for name, price, emoji in cakes
)

SYSTEM_PROMPT = f"""
Bạn là trợ lý AI của MR HÀO Bakery.

Hãy nói tiếng Việt tự nhiên, thân thiện, ngắn gọn.
Không nói rằng bạn là con người.
Không bịa sản phẩm hoặc giá.

MENU:
{menu_text}

GIỎ HÀNG HIỆN TẠI:
{cart_text()}

Bạn có thể:
- Tư vấn bánh theo sở thích.
- Tư vấn theo ngân sách.
- Tư vấn bánh sinh nhật.
- Trả lời giá.
- Giới thiệu menu.
- Hướng dẫn đặt bánh.
- Giải thích tổng tiền.
- Nói chuyện tự nhiên.

Nếu thông tin giao hàng/thanh toán chưa có trong hệ thống,
hãy nói rằng khách cần xác nhận với cửa hàng.
"""

# =========================================================
# AI
# =========================================================

def ask_ai(question):
    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        return (
            "⚠️ Chatbot AI chưa được cấu hình API key.\n\n"
            "Bạn vào Streamlit → Settings → Secrets và thêm:\n\n"
            "OPENROUTER_API_KEY = \"API_KEY_CUA_BAN\""
        )

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://mr-hao-bakery.streamlit.app",
        "X-OpenRouter-Title": "MR HÀO Bakery",
    }

    # Không lấy câu hỏi hiện tại 2 lần
    history = st.session_state.messages[-10:]

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    messages.extend(history)

    data = {
        "model": "openrouter/free",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500,
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60,
        )

        if response.status_code != 200:
            return (
                "⚠️ Chatbot đang gặp lỗi kết nối.\n"
                f"Mã lỗi: {response.status_code}"
            )

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⏳ Chatbot phản hồi hơi chậm. Bạn thử lại nhé."

    except Exception:
        return "⚠️ Không thể kết nối chatbot lúc này. Bạn thử lại nhé."

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>🍰 MR HÀO BAKERY</h1>
    <h3>Ngọt ngào trong từng chiếc bánh ❤️</h3>
    <p>20 loại bánh • Đặt hàng • Tính tiền • Chatbot AI</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# MENU
# =========================================================

st.header("🍰 MENU 20 LOẠI BÁNH")

search = st.text_input(
    "🔎 Tìm bánh",
    placeholder="Ví dụ: dâu, chocolate, cupcake..."
)

for i, (name, price, emoji) in enumerate(cakes):

    if search and search.lower() not in name.lower():
        continue

    with st.expander(
        f"{emoji}  {name}  —  {price:,} VNĐ"
    ):
        st.markdown(
            f"""
            <div class="cake-card">
                <h3>{emoji} {name}</h3>
                <p class="price">💰 {price:,} VNĐ</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        quantity = st.number_input(
            "Số lượng",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key=f"cake_{i}",
        )

        if quantity > 0:
            st.session_state.cart[name] = {
                "price": price,
                "quantity": quantity,
            }
        elif name in st.session_state.cart:
            del st.session_state.cart[name]

# =========================================================
# CART
# =========================================================

st.divider()
st.header("🛒 GIỎ HÀNG")

if not st.session_state.cart:
    st.info("🛒 Giỏ hàng đang trống.")
else:
    for name, item in list(st.session_state.cart.items()):
        subtotal = item["price"] * item["quantity"]

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(
                f"🍰 **{name}** — "
                f"{item['quantity']} × "
                f"{item['price']:,} = "
                f"**{subtotal:,} VNĐ**"
            )

        with col2:
            if st.button(
                "Xóa",
                key=f"remove_{name}"
            ):
                del st.session_state.cart[name]
                st.rerun()

st.success(
    f"💰 TỔNG TIỀN: {cart_total():,} VNĐ"
)

# =========================================================
# CUSTOMER
# =========================================================

st.header("👤 THÔNG TIN KHÁCH HÀNG")

customer = st.text_input(
    "Họ và tên",
    placeholder="Nguyễn Văn A"
)

phone = st.text_input(
    "Số điện thoại",
    placeholder="09xxxxxxxx"
)

address = st.text_area(
    "Địa chỉ nhận bánh",
    placeholder="Nhập địa chỉ..."
)

note = st.text_area(
    "Ghi chú",
    placeholder="Ví dụ: giao buổi chiều..."
)

if st.button(
    "🍰 XÁC NHẬN ĐẶT BÁNH",
    use_container_width=True
):
    total = cart_total()

    if total == 0:
        st.warning("Bạn chưa chọn bánh.")

    elif not customer.strip():
        st.warning("Vui lòng nhập họ tên.")

    elif not phone.strip():
        st.warning("Vui lòng nhập số điện thoại.")

    elif not address.strip():
        st.warning("Vui lòng nhập địa chỉ.")

    else:
        st.success("🎉 Đặt bánh thành công!")

        st.write(f"👤 Người đặt: **{customer}**")
        st.write(f"📞 Số điện thoại: **{phone}**")
        st.write(f"📍 Địa chỉ: **{address}**")
        st.write(f"📝 Ghi chú: **{note or 'Không có'}**")
        st.write(f"💰 Tổng tiền: **{total:,} VNĐ**")

# =========================================================
# CHATBOT
# =========================================================

st.divider()

st.markdown("""
<div class="chat-box">
    <h2>🤖 CHATBOT MR HÀO AI</h2>
    <p>Hãy hỏi tự nhiên như đang nói chuyện với nhân viên.</p>
</div>
""", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar="🍰" if message["role"] == "assistant" else "👤"
    ):
        st.markdown(message["content"])

question = st.chat_input(
    "Ví dụ: Mình có 100k thì nên mua bánh gì?"
)

if question:
    # Lưu câu hỏi đúng 1 lần
    st.session_state.messages.append({
        "role": "user",
        "content": question,
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(question)

    # Ưu tiên lệnh giỏ hàng để không cho AI tự đoán số lượng
    cart_answer = handle_cart_command(question)

    with st.chat_message("assistant", avatar="🍰"):
        with st.spinner("🍰 MR HÀO đang suy nghĩ..."):

            if cart_answer:
                answer = cart_answer
            else:
                answer = ask_ai(question)

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
    })

st.caption(
    "💡 Ví dụ: “Bánh nào rẻ nhất?” • "
    "“Mình có 100k nên mua gì?” • "
    "“Thêm 2 bánh dâu vào giỏ” • "
    "“Giỏ hàng của mình bao nhiêu?”"
)

# =========================================================
# ADMIN
# =========================================================

st.divider()
st.header("🔐 KHU VỰC QUẢN TRỊ")

password = st.text_input(
    "Mật khẩu quản trị",
    type="password",
)

try:
    ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    ADMIN_PASSWORD = "MRHAO2026"

if st.button("🔑 ĐĂNG NHẬP QUẢN TRỊ"):

    if password == ADMIN_PASSWORD:
        st.success("✅ Đăng nhập thành công!")
        st.write(f"🍰 Số sản phẩm: {len(cakes)}")
        st.write(
            f"🛒 Số loại bánh trong giỏ: "
            f"{len(st.session_state.cart)}"
        )
        st.write(
            f"💰 Tổng giỏ: {cart_total():,} VNĐ"
        )
    else:
        st.error("❌ Mật khẩu không đúng.")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    🍰 MR HÀO BAKERY<br>
    Python + Streamlit + AI
</div>
""", unsafe_allow_html=True)
