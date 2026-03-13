# 🛡️ Axion Secure (v2.0)
### Digital Escrow & Trade Assurance System (Uganda - Sudan)
**نظام الضمان الرقمي وتأمين الوساطة التجارية (أوغندا - السودان)**

---

## 🌍 Overview | نبذة عن النظام
**Axion Secure** هو منصة تقنية مصممة لتأمين الصفقات التجارية بين المصدرين في أوغندا والمستوردين في السودان. يعمل النظام كوسيط رقمي يضمن حقوق الطرفين باستخدام بروتوكول **Dual-Key Encryption** (تشفير المفتاح المزدوج).

This system solves the trust issue in cross-border trade by ensuring that funds are only released when both parties confirm the transaction through secure, unique codes.

---

## 🛠️ Key Features | المميزات الرئيسية
* **Secure Code Generation:** Generation of unguessable 8-digit secure keys using the `secrets` library.
* **Dual-Key Protocol:** Money release requires two different keys (Buyer Key + Broker Key).
* **Offline Database:** Local transaction logging to ensure data safety even without an internet connection.
* **Professional Dashboard:** Easy-to-use interface built with **Streamlit**.
* **Digital Business Identity:** Integrated business card for credibility with merchants.

---

## 🔐 How it Works | كيف يعمل النظام
1.  **Locking (التشفير):** When a deal starts, the broker generates two unique keys.
2.  **Verification (التحقق):** The buyer in Sudan receives one key, while the broker keeps the second.
3.  **Release (التحرير):** Once goods arrive safely, the merchant provides the buyer's key to the broker to unlock the funds.

---

## 🚀 Tech Stack | التقنيات المستخدمة
* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Data Handling:** Pandas
* **Security:** Cryptographically strong random numbers (Secrets library).

---

## 👤 About the Founder | عن المؤسس
Developed by a professional software developer based in Kampala, Uganda, specialized in financial brokerage tools and agricultural technology solutions.

**Contact for Business Support:**
* Location: Kampala, Uganda.
* Project: Axion Pay Solutions.

---
© 2026 Axion Pay. All Rights Reserved.
