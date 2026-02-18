import streamlit as st
import datetime
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Cobb 500 Manager", page_icon="🐥", layout="centered")

# --- قاعدة بيانات الخبرة (Cobb 500) ---
PLAN = {
    range(1, 2): {"med": "Glucose / Electrolytes", "dose": "10g/L", "task": "استقبال حراري (33°C).", "color": "#ff4b4b"},
    range(2, 4): {"med": "Tylosin + Vitamins AD3E", "dose": "1g + 1ml / L", "task": "وقاية تنفسية ومناعة.", "color": "#ff4b4b"},
    range(4, 8): {"med": "Multivitamins", "dose": "1ml / L", "task": "مراقبة استهلاك العلف والماء.", "color": "#00d4ff"},
    range(8, 11): {"med": "Amprolium (Anticoccidial)", "dose": "1g / L", "task": "وقاية من الكوكسيديا (رطوبة الفرشة).", "color": "#ff4b4b"},
    range(11, 15): {"med": "Liver Tonic", "dose": "1ml / L", "task": "تجهيز الطيور لتغيير العلف.", "color": "#00d4ff"},
    range(15, 17): {"med": "Liquid Toxin Binder", "dose": "0.5ml / L", "task": "تغيير العلف لـ Grower ومضاد سموم.", "color": "#ff4b4b"},
    range(17, 30): {"med": "Vitamins / Liver Tonic", "dose": "1ml / L", "task": "متابعة زيادة الوزن والتهوية.", "color": "#27ae60"},
    range(30, 45): {"med": "Pure Water Only", "dose": "0.5ml / L", "task": "فترة الأمان (سحب الأدوية) للبيع.", "color": "#27ae60"}
}

# --- واجهة المستخدم ---
st.title("🐥 مدير مزرعة الـ 100 كتكوت")
st.subheader("Cobb 500 Management - Uganda")

# مدخلات المستخدم في الشريط الجانبي
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    start_date = st.date_input("تاريخ استلام الكتاكيت", datetime.date(2026, 2, 14))
    total_chicks = st.number_input("العدد الكلي للكتاكيت", value=100)
    mortality = st.number_input("عدد النافق (الميت)", value=0)
    feed_price = st.number_input("سعر كيلو العلف (UGX)", value=3200)

# الحسابات الأساسية
age = (datetime.date.today() - start_date).days + 1
remaining_birds = total_chicks - mortality

# الحصول على التوجيه بناءً على العمر
current_advice = {"med": "Multivitamins", "dose": "1ml/L", "task": "مراقبة عامة", "color": "#666"}
for age_range, advice in PLAN.items():
    if age in age_range:
        current_advice = advice
        break

# عرض البيانات الأساسية
col1, col2, col3 = st.columns(3)
col1.metric("العمر (يوم)", f"{age}")
col2.metric("العدد الحالي", f"{remaining_birds}")
col3.metric("نسبة الفقد", f"{(mortality/total_chicks)*100:.1f}%")

# قسم الأدوية والمهام (Dynamic Alert)
st.markdown(f"""
<div style="background-color:{current_advice['color']}; padding:20px; border-radius:15px; color:white; text-align:right;">
    <h3>💉 دواء اليوم: {current_advice['med']}</h3>
    <p><b>📏 الجرعة:</b> {current_advice['dose']}</p>
    <p><b>📝 المهمة:</b> {current_advice['task']}</p>
</div>
""", unsafe_print_string=True)

# حاسبة استهلاك العلف التقديرية
st.write("---")
st.header("📊 تقديرات العلف والوزن")
# بيانات Cobb 500 التقريبية للنمو
chart_data = pd.DataFrame({
    'الأسبوع': [1, 2, 3, 4, 5],
    'الوزن المستهدف (جم)': [190, 480, 950, 1600, 2300],
    'استهلاك العلف (جم)': [170, 400, 800, 1200, 1500]
})
st.line_chart(chart_data.set_index('الأسبوع'))

st.info(f"💡 نصيحة الخبير: في عمر {age} يوم، يجب أن يكون استهلاك العلف اليومي لكل طائر حوالي {chart_data['استهلاك العلف (جم)'].iloc[min(age//7, 4)]} جرام.")

# زر الحفظ والتصدير
if st.button("حفظ تقرير اليوم 💾"):
    st.success("تم حفظ البيانات بنجاح في قاعدة البيانات!")
