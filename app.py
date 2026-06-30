import streamlit as st
import pandas as pd

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Trev Platform",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم بالكامل باستخدام CSS للطابع الداكن (Dark Vibes)
st.markdown("""
    <style>
    /* تغيير خلفية الموقع والألوان الأساسية */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    
    /* تعديل الهيدر والقوائم الجانبية */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    /* تصميم البطاقات الذكية للمشاريع والسير الذاتية */
    .custom-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .custom-card:hover {
        transform: translateY(-2px);
        border-color: #58a6ff;
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.2);
    }
    
    /* العناوين والأزرار */
    h1, h2, h3 {
        color: #f0f6fc !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .badge {
        background-color: #21262d;
        color: #58a6ff;
        padding: 4px 8px;
        border-radius: 5px;
        font-size: 12px;
        margin-right: 5px;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية للتنقل بين الأقسام
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #58a6ff;'>🌌 Trev</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px;'>بوابة الكفاءات والاستثمار</p>", unsafe_allow_html=True)
    st.write("---")
    choice = st.radio("انتقل إلى:", ["🏠 الرئيسية", "💼 بوابة التوظيف (CVs)", "🚀 حاضنة المشاريع", "➕ أضف سيرتك / مشروعك"])

# 1. الصفحة الرئيسية
if choice == "🏠 الرئيسية":
    st.markdown("<h1 style='text-align: center;'>منصة تريف التقنية</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #8b949e;'>منصة واحدة تجمع بين التوظيف والمهن من جهة، وبين الاستثمار والتجارة الرقمية من جهة أخرى.</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3>💼 قسم التوظيف والمهن</h3>
            <p>تصفح السير الذاتية لأبرز المطورين والمصممين، واطلب مقابلات عمل مباشرة بضغطة زر واحدة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="custom-card">
            <h3>🚀 قسم الاستثمار والتجارة</h3>
            <p>اكتشف مشاريع برمجية وتقنية مميزة جاهزة للاستثمار والتمويل، أو تصفح المنتجات الرقمية للشراء المباشر.</p>
        </div>
        """, unsafe_allow_html=True)

# 2. بوابة التوظيف
elif choice == "💼 بوابة التوظيف (CVs)":
    st.title("💼 قاعدة بيانات الكفاءات")
    st.write("ابحث عن المبرمجين والمصممين حسب المهارات:")
    
    search = st.text_input("🔍 ابحث عن تخصص أو مهارة (مثال: Python, UI/UX)...")
    
    st.markdown("""
    <div class="custom-card">
        <h3 style='margin-bottom: 5px;'>فراس حمد المعمري</h3>
        <p style='color: #8b949e; margin-top: 0;'>مطوّر برمجيات ومسؤول مجتمعات رقمية</p>
        <div>
            <span class="badge">Python</span>
            <span class="badge">Streamlit</span>
            <span class="badge">Discord.py</span>
        </div>
        <br>
        <p>مطور متخصص في بناء لوحات التحكم الذكية وبوتات إدارة السيرفرات بأسلوب عصري ومينيماليست.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🗓️ طلب مقابلة عمل"):
        st.success("تم إرسال طلب المقابلة بنجاح! سيتم تنبيه صاحب الحساب.")

# 3. حاضنة المشاريع
elif choice == "🚀 حاضنة المشاريع":
    st.title("🚀 معرض المشاريع والاستثمار")
    
    st.markdown("""
    <div class="custom-card">
        <h3>🌌 Black Phantom Dashboard</h3>
        <p style='color: #8b949e;'>أداة إنتاجية متكاملة للمطورين بنظام مظلم</p>
        <p>مشروع ذكي مبني بالكامل لإدارة المهام، البيانات، والربط مع سيرفرات الديسكورد بواجهات نيون فخمة.</p>
        <hr style='border-color: #30363d;'>
        <p><b>حالة المشروع:</b> مطلوب مستثمر للتمويل وتوسيع نطاق البرمجية.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("💰 تقديم عرض استثماري"):
            st.info("تم فتح قناة تواصل مباشرة مع صاحب المشروع.")
    with col_btn2:
        if st.button("🛒 شراء / تجربة الأداة"):
            st.success("جاري تحويلك لصفحة تجربة المنتج الجاهز...")

# 4. إضافة بيانات
elif choice == "➕ أضف سيرتك / مشروعك":
    st.title("➕ أضف بصمتك للمنصة")
    type_add = st.selectbox("ماذا تريد أن تضيف؟", ["سيرة ذاتية جديدة", "مشروع جديد لجذب المستثمرين"])
    
    if type_add == "سيرة ذاتية جديدة":
        name = st.text_input("الاسم الكامل")
        role = st.text_input("المسمى الوظيفي")
        skills = st.text_input("المهارات (افصل بينها بفاصلة)")
        bio = st.text_area("نبذة عنك")
        if st.button("نشر السيرة الذاتية"):
            st.success("تم نشر ملفك الشخصي بنجاح في قسم الكفاءات!")
            
    else:
        proj_name = st.text_input("اسم المشروع")
        proj_desc = st.text_area("شرح فكرة المشروع وثغرات السوق التي يحلها")
        proj_status = st.selectbox("هدف العرض", ["مطلوب تمويل واستثمار", "منتج جاهز للبيع المباشر"])
        if st.button("إطلاق المشروع"):
            st.success("تم إطلاق مشروعك بنجاح في الحاضنة!")
        proj_desc = st.text_area("شرح فكرة المشروع وثغرات السوق التي يحلها")
        proj_status = st.selectbox("هدف العرض", ["مطلوب تمويل واستثمار", "منتج جاهز للبيع المباشر"])
        if st.button("إطلاق المشروع"):
            st.success("تم إطلاق مشروعك بنجاح في الحاضنة!")
