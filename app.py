import streamlit as st
import requests


# =========================================================
# CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="MR HÀO Bakery",
    page_icon="🍰",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #fff8f5;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    background: linear-gradient(
        135deg,
        #ffe5d9,
        #fff0e8
    );
    margin-bottom: 20px;
}

.hero h1 {
    color: #8b4513;
}

.price {
    font-size: 20px;
    font-weight: bold;
}

.chat-title {
    background-color: #ffe5d9;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 20 LOẠI BÁNH
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
    ("Bánh Kem Dâu", 180000, "🍓")
]


# =========================================================
# SESSION STATE
# =========================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Xin chào! Mình là trợ lý AI của "
                "MR HÀO Bakery.\n\n"
                "Bạn có thể hỏi mình tự nhiên về:\n"
                "🍰 bánh\n"
                "💰 giá\n"
                "🛒 đặt hàng\n"
                "🚚 giao hàng\n"
                "💳 thanh toán\n"
                "🎂 bánh sinh nhật\n"
                "⭐ gợi ý bánh"
            )
        }
    ]


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>🍰 MR HÀO BAKERY</h1>

<h3>Ngọt ngào trong từng chiếc bánh ❤️</h3>

<p>
20 loại bánh • Đặt hàng • Chatbot AI • Tính tiền tự động
</p>

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


# =========================================================
# GIỎ HÀNG
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
            f"🍰 {name} | "
            f"{item['quantity']} × "
            f"{item['price']:,} = "
            f"**{subtotal:,} VNĐ**"
        )

st.success(
    f"💰 TỔNG TIỀN: {total:,} VNĐ"
)


# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================

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


# =========================================================
# ĐẶT BÁNH
# =========================================================

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
            "Vui lòng nhập họ tên."
        )

    elif not phone:

        st.warning(
            "Vui lòng nhập số điện thoại."
        )

    elif not address:

        st.warning(
            "Vui lòng nhập địa chỉ."
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
            f"📝 Ghi chú: {note}"
        )

        st.write(
            f"💰 Tổng tiền: {total:,} VNĐ"
        )


# =========================================================
# TẠO THÔNG TIN MENU CHO AI
# =========================================================

menu_text = ""

for name, price, emoji in cakes:

    menu_text += (
        f"- {emoji} {name}: "
        f"{price:,} VNĐ\n"
    )


# =========================================================
# SYSTEM PROMPT CHO CHATBOT
# =========================================================

SYSTEM_PROMPT = f"""
Bạn là trợ lý AI chính thức của MR HÀO Bakery.

Nhiệm vụ:
- Tư vấn bánh.
- Trả lời giá bánh.
- Giới thiệu menu.
- Tư vấn bánh theo ngân sách.
- Tư vấn bánh sinh nhật.
- Hướng dẫn đặt hàng.
- Giải thích giỏ hàng.
- Giải thích cách tính tiền.
- Trả lời câu hỏi về giao hàng.
- Trả lời câu hỏi về thanh toán.
- Nói chuyện tự nhiên, thân thiện bằng tiếng Việt.

THÔNG TIN CỬA HÀNG:

MR HÀO Bakery có 20 loại bánh:

{menu_text}

QUY TẮC:

1. Không tự bịa ra sản phẩm không có trong menu.

2. Không tự bịa giá.

3. Nếu khách hỏi giá, dùng đúng giá trong menu.

4. Nếu khách hỏi:
"Mình có 50k nên mua gì?"
hãy dựa vào menu để gợi ý.

5. Nếu khách hỏi:
"Bánh nào hợp sinh nhật?"
hãy gợi ý Bánh Sinh Nhật hoặc Bánh Kem Dâu.

6. Nếu khách hỏi:
"Bánh nào rẻ nhất?"
hãy kiểm tra menu.

7. Nếu khách hỏi cách đặt:
Hướng dẫn:
Chọn bánh → chọn số lượng → kiểm tra giỏ hàng
→ nhập thông tin → xác nhận đặt bánh.

8. Phí giao hàng hiện chưa được tính tự động.

9. Thời gian giao hàng cần cửa hàng xác nhận.

10. Nếu không biết thông tin, nói rõ rằng thông tin
cần được cửa hàng xác nhận.

11. Không nói rằng bạn là con người.

12. Trả lời ngắn gọn, dễ hiểu.

13. Có thể sử dụng emoji phù hợp.

14. Không cần nói rằng bạn đang sử dụng API.

15. Khi khách hỏi câu hỏi thông thường,
hãy trả lời tự nhiên thay vì bắt họ phải dùng
đúng từ khóa.
"""


# =========================================================
# HÀM GỌI OPENROUTER
# =========================================================

def ask_ai(question):

    try:

        api_key = st.secrets["OPENROUTER_API_KEY"]

    except Exception:

        return (
            "⚠️ Chưa cấu hình OPENROUTER_API_KEY.\n\n"
            "Bạn hãy vào Streamlit Cloud → Settings → "
            "Secrets và thêm API key."
        )


    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://mr-hao-bakery.streamlit.app",
        "X-OpenRouter-Title": "MR HÀO Bakery"
    }


    # Chỉ gửi một phần lịch sử để tránh request quá dài
    history = st.session_state.messages[-12:]


    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


    messages.extend(history)


    messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    data = {
        "model": "openrouter/free",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }


    try:

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )


        if response.status_code != 200:

            return (
                "⚠️ Chatbot đang gặp lỗi kết nối.\n\n"
                f"Mã lỗi: {response.status_code}"
            )


        result = response.json()


        answer = (
            result["choices"][0]
            ["message"]
            ["content"]
        )


        return answer


    except requests.exceptions.Timeout:

        return (
            "⏳ Chatbot phản hồi hơi chậm. "
            "Bạn thử gửi lại câu hỏi nhé."
        )


    except Exception as e:

        return (
            "⚠️ Không thể kết nối chatbot lúc này.\n\n"
            f"Chi tiết: {str(e)}"
        )


# =========================================================
# CHATBOT
# =========================================================

st.divider()

st.markdown(
    """
    <div class="chat-title">
        <h2>🤖 CHATBOT MR HÀO AI</h2>
        <p>
        Hỏi tự nhiên như đang nói chuyện với nhân viên bán bánh.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HIỂN THỊ LỊCH SỬ
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar=(
            "🍰"
            if message["role"] == "assistant"
            else "👤"
        )
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# NHẬP CÂU HỎI
# =========================================================

question = st.chat_input(
    "Ví dụ: Mình có 100k thì nên mua bánh gì?"
)


if question:

    # Lưu câu hỏi
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # Hiển thị câu hỏi
    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(question)


    # Gọi AI
    with st.chat_message(
        "assistant",
        avatar="🍰"
    ):

        with st.spinner(
            "🍰 MR HÀO đang suy nghĩ..."
        ):

            answer = ask_ai(question)

        st.markdown(answer)


    # Lưu câu trả lời
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# =========================================================
# CÂU HỎI GỢI Ý
# =========================================================

st.caption(
    "💡 Bạn có thể hỏi: "
    "“Bánh nào rẻ nhất?” • "
    "“Mình có 100k nên mua gì?” • "
    "“Bánh nào hợp sinh nhật?” • "
    "“Cách đặt bánh?”"
)


# =========================================================
# QUẢN TRỊ
# =========================================================

st.divider()

st.header("🔐 KHU VỰC QUẢN TRỊ")

password = st.text_input(
    "Mật khẩu quản trị",
    type="password"
)


DEMO_PASSWORD = "MRHAO2026"


if st.button(
    "🔑 ĐĂNG NHẬP QUẢN TRỊ"
):

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


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🍰 MR HÀO BAKERY | "
    "Built with Python + Streamlit + AI"
        )
