import streamlit as st
import secrets
import string
import pandas as pd
from datetime import datetime
import os

# --- إعدادات المسار للحفظ الدائم على الهاتف ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'axion_database.csv')

# إعدادات واجهة التطبيق
st.set_page_config(page_title="Axion Secure | نظام الضمان التقني", page_icon="🛡️", layout="centered")

# دالة توليد الأكواد السرية
def generate_secure_key(length=8):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

# دالة حفظ الصفقة في قاعدة البيانات
def save_deal_to_db(deal_data):
    df = pd.DataFrame([deal_data])
    if not os.path.isfile(DB_FILE):
        df.to_csv(DB_FILE, index=False)
    else:
        df.to_csv(DB_FILE, mode='a', header=False, index=False)

# --- واجهة المستخدم ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛡️ AXION SECURE</h1>", unsafe_unit=True)
st.markdown("<p style='text-align: center;'>نظام التأمين الرقمي للوساطة التجارية (أوغندا - السودان)</p>", unsafe_unit=True)

tabs = st.tabs(["🚀 إنشاء ضمان", "🔍 تحقق وتحرير", "📊 سجل الصفقات", "👤 بطاقة العمل"])

# --- التبويب الأول: إنشاء صفقة جديدة ---
with tabs[0]:
    st.subheader("تسجيل عملية جديدة")
    with st.form("deal_form"):
        merchant_name = st.text_input("اسم التاجر (البائع)")
        buyer_location = st.selectbox("موقع الاستلام", ["بورتسودان", "الدمازين", "كسلا", "عطبرة", "أخرى"])
        amount_usd = st.number_input("قيمة الصفقة (USD)", min_value=0)
        submit_btn = st.form_submit_button("تفعيل القفل الرقمي وتوليد الأكواد")

    if submit_btn and merchant_name:
        b_key = generate_secure_key()  # كود المشتري
        v_key = generate_secure_key()  # كودك أنت (الوسيط)
        deal_id = f"AXN-{datetime.now().strftime('%d%m-%H%M')}"
        
        deal_info = {
            "ID": deal_id,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Merchant": merchant_name,
            "Location": buyer_location,
            "Amount": amount_usd,
            "Buyer_Key": b_key,
            "Broker_Key": v_key,
            "Status": "Locked"
        }
        save_deal_to_db(deal_info)
        
        st.success(f"✅ تم تأمين الصفقة برقم: {deal_id}")
        st.error(f"🔴 كود المشتري (يُرسل للسودان): {b_key}")
        st.warning(f"🟢 كود الوسيط (خاص بك وحدك): {v_key}")
        st.info("💡 نصيحة: خذ لقطة شاشة (Screenshot) للأكواد الآن.")

# --- التبويب الثاني: التحقق والتحرير ---
with tabs[1]:
    st.subheader("تحرير المبلغ المالي")
    st.write("أدخل الأكواد عند وصول البضاعة لتحرير الضمان:")
    code_in_1 = st.text_input("كود المشتري (القادم من السودان)")
    code_in_2 = st.text_input("كود الوسيط (الخاص بك)")
    
    if st.button("تأفيذ عملية التحقق"):
        if os.path.isfile(DB_FILE):
            df = pd.read_csv(DB_FILE)
            # التحقق من وجود تطابق
            match = df[(df['Buyer_Key'].astype(str) == code_in_1.strip()) & 
                       (df['Broker_Key'].astype(str) == code_in_2.strip())]
            
            if not match.empty:
                st.balloons()
                st.success("🎯 تطابق ناجح! تم تحرير الضمان.")
                st.write(f"المستحق للقبض: **{match.iloc[0]['Merchant']}**")
                st.write(f"المبلغ: **{match.iloc[0]['Amount']} USD**")
            else:
                st.error("❌ فشل التحقق. الأكواد غير متطابقة أو غير موجودة.")
        else:
            st.warning("لا توجد سجلات بعد.")

# --- التبويب الثالث: سجل الصفقات ---
with tabs[2]:
    st.subheader("الأرشيف الرقمي")
    if os.path.isfile(DB_FILE):
        full_df = pd.read_csv(DB_FILE)
        st.dataframe(full_df[['ID', 'Date', 'Merchant', 'Amount', 'Location']])
    else:
        st.info("السجل فارغ حالياً.")

# --- التبويب الرابع: بطاقة العمل الرقمية (للهيبة التقنية) ---
with tabs[3]:
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 2px solid #1E3A8A;'>
        <h2 style='color: #1E3A8A; margin-top: 0;'>Axion Pay Solutions</h2>
        <p><b>المؤسس:</b> مبرمج ومستشار تأمين تقني</p>
        <p><b>الخدمة:</b> تأمين الوساطة التجارية بأكواد التشفير الرقمية</p>
        <p><b>الموقع:</b> كمبالا - أوغندا</p>
        <hr>
        <p style='font-size: 12px;'>نظام Axion Secure يضمن حق البائع والمشتري عبر بروتوكول Dual-Key المتطور.</p>
    </div>
    """, unsafe_unit=True)
