# Reverse Engineering & CTF Solutions 🚩

> **[عربي](#القسم-العربي)** | **[English](#english-section)**

<a id="english-section"></a>
## 🇬🇧 English Section

### Overview
This repository contains a collection of Python scripts and tools I developed while solving 
Reverse Engineering (RE) and Binary Exploitation challenges (inspired by platforms like `pwn.college`). 

It serves as a personal portfolio showcasing my progression in:
* Static and Dynamic Analysis (using GDB, objdump, etc.).
* Binary data manipulation and memory parsing.
* Reversing C `structs` and memory layouts.
* Automating exploit payloads generation.

### Scripts Directory 📁
Below is a summary of the scripts currently available in this repository. 
*(This list will be updated as I solve more challenges)*:

* **`cimgV2_script.py`**:
A basic script to generate a dummy custom image (`.cimg`) file with a hardcoded header
to bypass initial structural checks in a binary.

* **`cimgV2.1_script.py`**: 
A script that uses the `struct` module to pack specific RGB and ASCII 
values (Little-Endian) to craft a precise payload that bypasses a 4-pixel `memcmp` check.

* **`cimgV2.2_script.py`**: 
An advanced memory-parsing script. It reads a raw memory dump extracted dynamically via **GDB**, 
parses the bytes into 24-byte RGB/ASCII chunks, and dynamically calculates valid integer 
factors (width/height < 256) to bypass strict `uint8_t` memory constraints and generate the final payload.

---

<a id="القسم-العربي"></a>
## 🇸🇦 القسم العربي

### نظرة عامة
يحتوي هذا المستودع على مجموعة من أدوات وسكربتات بايثون التي قمت بتطويرها أثناء
حل تحديات الهندسة العكسية واستغلال الثغرات .

يُعد هذا المستودع بمثابة معرض أعمال يوضح تطور مهاراتي في:
* التحليل الثابت والديناميكي للبرمجيات (باستخدام أدوات مثل GDB).
* التعامل مع البيانات الثنائية وتحليل الذاكرة.
* الهندسة العكسية لهياكل C (`structs`) وتوزيعها في الذاكرة.
* أتمتة وبناء ملفات الاستغلال (Payloads) برمجياً.

### فهرس السكربتات 📁
فيما يلي ملخص للسكربتات الموجودة حالياً في المستودع. *(سيتم تحديث هذه القائمة مع كل تحدٍ جديد أقوم بحله)*:

* **`cimgV2_script.py`**:
سكربت أساسي لإنشاء ملف صورة مخصص (`.cimg`) بهيدر (Header) ثابت، وظيفته تجاوز الفحوصات الهيكلية الأولية للبرنامج.

* **`cimgV2.1_script.py`**: 
سكربت يستخدم مكتبة `struct` لدمج قيم RGB و ASCII بصيغة Little-Endian لإنشاء Payload دقيق
يتجاوز فحص `memcmp` مخصص لـ 4 بكسلات فقط.

* **`cimgV2.2_script.py`**: 
سكربت متقدم لتحليل الذاكرة أوتوماتيكياً. يقوم بقراءة ملف تفريغ ذاكرة (Memory Dump) تم
استخراجه بواسطة **GDB**، ويحلل البيانات إلى بكسلات بحجم 24 بايت، ثم يحسب الأبعاد (الطول والعرض) ديناميكياً
لتجاوز قيود المتغيرات (أقل من 256) وتوليد الاستغلال النهائي.
