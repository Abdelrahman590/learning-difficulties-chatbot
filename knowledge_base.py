from arabic_normlizer import ArabicNormalizer

class SpecializedKnowledgeBase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.normalizer = ArabicNormalizer()
        self.content = self.load_file()
        self.knowledge_dict = self.build_specialized_knowledge()
    
    def load_file(self):
        """قراءة محتوى الملف النصي"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"تحذير: الملف {self.file_path} غير موجود")
            return "الملف غير موجود"
        except Exception as e:
            print(f"خطأ في قراءة الملف: {e}")
            return ""
    
    def build_specialized_knowledge(self):
        """بناء قاعدة المعرفة المتخصصة"""
        knowledge = {
            # الإدراك - متخصص
            "الإدراك": {
                "definition": {
                    "keywords": [
                        "ما هو الإدراك", "تعريف الإدراك", "مفهوم الإدراك",
                        "معنى الإدراك", "ايه هو الإدراك"
                    ],
                    "response": """**تعريف الإدراك:**

الإدراك هو قدرة الفرد على فهم المثيرات الحسية وتفسيرها. هو العملية النفسية التي تجعلنا نعطي معاني ودلالات للأشياء والأشخاص والمواقف التي نتعامل معها.

**خصائص الإدراك:**
• يعتمد على تنظيم المثيرات الحسية المتعلقة بالموضوع
• يتضمن تفسير وصياغة المعلومات في كليات ذات معنى
• يعتمد على المقارنات بين ما يألفه الطفل والشيء الجديد

**أنواع الإدراك الرئيسية:**
• **الإدراك البصري**: معالجة المعلومات المرئية
• **الإدراك السمعي**: معالجة المعلومات الصوتية
• **الإدراك اللمسي**: معالجة المعلومات عبر اللمس"""
                },
                "treatment": {
                    "keywords": [
                        "كيف أعالج مشاكل الإدراك", "علاج الإدراك", "تحسين الإدراك",
                        "طرق علاج الإدراك", "تدريب الإدراك", "معالجة مشاكل الإدراك"
                    ],
                    "response": """**برنامج علاج مشاكل الإدراك المتخصص:**

**أولاً: علاج مشاكل الإدراك البصري**

**1. علاج التمييز البصري:**
• **الأنشطة النمائية**: 
  - كروت "ما المختلف" بين الصور
  - مقارنة الأشكال المتشابهة والمختلفة
  - أنشطة إدراك السخافات في الصور
• **التدريبات الأكاديمية**: 
  - التمييز بين الحروف المتشابهة (ج، ح، خ)
  - التعرف على المتشابهات والمطابقة
  - مقارنة الخصائص الشكلية

**2. علاج التآزر البصري الحركي:**
• **الأنشطة النمائية**: 
  - ألعاب البازل والتركيب
  - اللعب بالصلصال والتشكيل
  - تلوين الأشكال بدقة
  - رسم دوائر داخل مستطيلات
• **التدريبات الأكاديمية**: 
  - الكتابة بفواصل بين الكلمات
  - استخدام ألوان مختلفة للكلمات
  - النقل التدريجي من السبورة

**3. علاج سرعة الإدراك البصري:**
• **التدريب بوقت محدد**: جميع الأنشطة مع ساعة إيقاف
• **أنشطة سريعة**: تركيب البازل، الكونكت 4، نقل الحبوب
• **التدرج الزمني**: تقليل الوقت المسموح تدريجياً

**4. علاج الإغلاق البصري:**
• **صور غير مكتملة**: تحديد الشيء الموجود أو الناقص
• **أشكال ناقصة**: إكمال الرموز والأشكال
• **تدريبات أكاديمية**: استخراج الحروف من الكلمات

**ثانياً: علاج مشاكل الإدراك السمعي**

**1. علاج الوعي الصوتي:**
• **تقليد الأصوات**: أصوات الطرق والنغمات
• **تحليل الكلمات**: تقسيم "مدرسة" إلى (م-د-ر-س-ة)
• **أنشطة الحروف**: إيجاد كلمات تبدأ بحرف معين

**2. علاج التمييز الصوتي:**
• **التمييز بين الأصوات**: (س، ص) و (ز، ظ)
• **استخدام التسجيلات**: أصوات مختلفة للتمييز
• **عد التكرار**: حساب تكرار كلمة في نص

**3. علاج المزج الصوتي:**
• **تجميع الأصوات**: (ب.ط.ة) → بطة
• **استخدام الرموز**: ربط كل صوت بلون أو شكل
• **التدرج**: من مقطعين إلى كلمات كاملة

**ثالثاً: خطة العلاج المتكاملة**
• **التقييم الأولي**: تحديد نوع مشكلة الإدراك المحددة
• **البرنامج الفردي**: 3-4 جلسات أسبوعياً لمدة 45 دقيقة
• **المتابعة والتقييم**: كل أسبوعين لقياس التقدم
• **التنسيق**: مع المدرسة والأهل لتطبيق التدريبات"""
                },
                "types": {
                    "keywords": [
                        "أنواع الإدراك", "تصنيف الإدراك", "أقسام الإدراك"
                    ],
                    "response": """**أنواع الإدراك وتصنيفاته:**

**أولاً: الإدراك البصري (5 أنواع)**

**1. التمييز البصري:**
- التعرف على المثيرات المتشابهة شكلاً
- التفريق بين الحروف المتشابهة (ج، ح، خ)

**2. التآزر البصري الحركي:**
- تنسيق حركة العين مع اليد
- مهم للكتابة والرسم

**3. سرعة الإدراك البصري:**
- الوقت المستغرق لفهم المثير البصري
- مهم للقراءة السريعة

**4. الإغلاق البصري:**
- التعرف على مثير غير مكتمل
- فهم الحروف في وسط وآخر الكلمة

**5. الإدراك البصري المكاني:**
- التعامل مع الفراغات والاتجاهات
- فهم المواقع النسبية للأشياء

**ثانياً: الإدراك السمعي (4 أنواع)**

**1. الوعي الصوتي:**
- إدراك أن الكلمة تتكون من أصوات منفصلة

**2. التمييز الصوتي:**
- التفريق بين الأصوات المتشابهة

**3. المزج الصوتي:**
- دمج الأصوات لتكوين كلمات

**4. الإغلاق السمعي:**
- فهم الكلمات غير الواضحة أو الناقصة"""
                }
            },

            # الانتباه - متخصص
            "الانتباه": {
                "definition": {
                    "keywords": [
                        "ما هو الانتباه", "تعريف الانتباه", "مفهوم الانتباه"
                    ],
                    "response": """**تعريف الانتباه:**

الانتباه هو استقبال الجهاز العصبي لمثير معين من خلال الحواس بشكل مقصود وتجاهل المثيرات الأخرى الموجودة في نفس الوقت.

**ملاحظات مهمة:**
• أي طفل في حالة انتباه دائمة لمنبهات داخلية وخارجية (عدا الحالات المرضية)
• المشكلة ليست في قدرة الطفل على الانتباه، بل في قدرتنا على جذب انتباهه للاهتمام المشترك
• يجب أن نبدأ بما يهتم به الطفل لإطالة مدة الانتباه

**أنواع مهارات الانتباه:**
• **مرونة الانتباه**: القدرة على التنقل بين مثيرات متعددة
• **مدة الانتباه**: الفترة الزمنية للتركيز على المهمة
• **الانتباه الانتقائي**: القدرة على التركيز على مثير واحد وسط عدة مثيرات"""
                },
                "treatment": {
                    "keywords": [
                        "كيف أعالج مشاكل الانتباه", "علاج الانتباه", "تحسين التركيز",
                        "علاج التشتت", "تدريب الانتباه", "معالجة مشاكل الانتباه"
                    ],
                    "response": """**برنامج علاج مشاكل الانتباه المتخصص:**

**أولاً: علاج مرونة الانتباه**

**المشكلة الشائعة**: صعوبة النقل من السبورة

**العلاج النمائي:**
• **استخراج الاختلافات**: بين الصور المتشابهة
• **أنشطة التوصيل**: ربط الصور بالكلمات
• **تدريب الكشاف**: في الظلام لتتبع الضوء
• **لصق الورق**: على الجسم وإزالته أمام المرآة
• **البحث في البيئة**: عن عناصر مطابقة لصور معينة

**العلاج الأكاديمي:**
• **النقل التدريجي**: من الورقة → السبورة الصغيرة → السبورة الكبيرة
• **ترك مسافات**: بين السطور والكلمات في البداية
• **استخدام الألوان**: كتابة كل كلمة بلون مختلف

**ثانياً: علاج مدة الانتباه**

**المشكلة الشائعة**: عدم إتمام المهام، فترات تركيز قصيرة

**العلاج النمائي:**
• **أنشطة التسلسل**: إكمال الأنماط من البسيط للمعقد
• **نشاط السبحة**: عد الخرز بتركيز
• **المتاهات المتدرجة**: من السهل للصعب
• **أنشطة حسية**: التعرف على الأشياء باللمس والشم

**العلاج الأكاديمي:**
• **فترات راحة**: كل 10 دقائق
• **تقليل الواجبات**: المدرسية
• **الشرح المزدوج**: سمعي وبصري معاً
• **استخدام ساعة الإيقاف**: لزيادة مدة التركيز تدريجياً

**ثالثاً: علاج الانتباه الانتقائي (التركيز)**

**المشكلة الشائعة**: قراءة نصف السؤال فقط، الاندفاعية

**العلاج النمائي:**
• **الاشتراط السمعي**: رفع اليد عند سماع كلمة معينة
• **الاشتراط البصري**: استخراج لون أو شكل محدد
• **تحديد مصدر الصوت**: في البيئة المحيطة
• **أنشطة التمييز**: بين الأصوات والأشكال المختلفة

**العلاج الأكاديمي:**
• **التدريب على الأسئلة المركبة**: فهم السؤال كاملاً
• **أنشطة "فين اللي شبه دي"**: تطوير التركيز البصري
• **التدريب على التعليل**: لماذا حدث هذا؟

**نصائح عامة للعلاج:**
• **البدء بما يهتم به الطفل**: لإطالة مدة الانتباه
• **استخدام الألعاب**: لجعل التدريب ممتعاً
• **التدرج في الصعوبة**: من البسيط للمعقد
• **التعزيز الإيجابي**: عند كل تحسن"""
                }
            },

            # الذاكرة - متخصص
            "الذاكرة": {
                "definition": {
                    "keywords": [
                        "ما هي الذاكرة", "تعريف الذاكرة", "مفهوم الذاكرة"
                    ],
                    "response": """**تعريف الذاكرة:**

الذاكرة هي قدرة الفرد على تنظيم الخبرات المتعلمة وتخزينها ثم استدعائها للاستفادة منها في موقف حياتي أو موقف اختباري.

**العوامل المؤثرة على الذاكرة:**
• **الأكل**: تناول الأوميجا 3 (السمك، المكسرات، عين الجمل)
• **النوم**: يجب أن يكون أكثر من 4 ساعات يومياً
• **النشاط البدني**: يحسن الدورة الدموية للمخ
• **البيئة المحيطة**: الهدوء والتنظيم مهمان للتذكر

**أنواع الذاكرة:**
• **الذاكرة البصرية**: (قصيرة المدى، طويلة المدى، عاملة)
• **الذاكرة السمعية**: (قصيرة المدى، طويلة المدى، عاملة)
• **الذاكرة العاملة**: معالجة المعلومات مع تنفيذ مهام أخرى"""
                },
                "treatment": {
                    "keywords": [
                        "كيف أعالج مشاكل الذاكرة", "علاج الذاكرة", "تحسين الذاكرة",
                        "تقوية الذاكرة", "تدريب الذاكرة", "معالجة مشاكل الذاكرة"
                    ],
                    "response": """**برنامج علاج مشاكل الذاكرة المتخصص:**

**أولاً: علاج الذاكرة البصرية**

**1. الذاكرة قصيرة المدى (أقل من 30 ثانية):**
• **تدريبات الحذف**: إخفاء كارت من 3 كروت
• **تدريبات الإضافة**: إضافة كارت جديد للمجموعة
• **تدريبات الإبدال**: تغيير موضع الكروت
• **التدرج**: من 3 كروت إلى 5 كروت فأكثر

**2. الذاكرة طويلة المدى (أكثر من 30 ثانية):**
• **نفس التدريبات السابقة** لكن بفترات زمنية أطول
• **التدرج الزمني**: دقيقة → دقيقتان → 5 دقائق → 10 دقائق
• **التطبيق العملي**: تذكر ترتيب الأدوات على المكتب

**ثانياً: علاج الذاكرة السمعية**

**1. تدريبات الأرقام:**
• **التكرار المباشر**: (1-8-5-3) قول وراء المدرب
• **التكرار العكسي**: قول الأرقام بالعكس (3-5-8-1)
• **التدرج**: من 3 أرقام إلى 7 أرقام

**2. تدريبات الكلمات والجمل:**
• **الكلمات المفردة**: تفاحة، عنب، بطة، قطة
• **الجمل القصيرة**: "ذهب أحمد إلى المدرسة"
• **القصص**: تذكر أحداث قصة قصيرة بالتسلسل

**ثالثاً: علاج الذاكرة العاملة (الأهم)**

**1. تدريبات الحذف:**
• المثال: (6-8-6-2-6-3) قل الأرقام بدون (6)
• النتيجة: (8-2-3)

**2. تدريبات التصحيح:**
• المثال: (5+12=50 قلم) اترك الكلمة واحسب المعادلة صحيحة
• النتيجة: 5+12=17

**3. تدريبات العكس:**
• المثال: (4-5-8-3) قل الأرقام بالعكس
• النتيجة: (3-8-5-4)

**4. تدريبات العمليات:**
• **الجمع**: (2-6-9-5) اجمع الأرقام الزوجية فقط = 8
• **الطرح**: (2-9-6-3) اطرح 2 من الأرقام الفردية = (7-1)

**5. تدريبات التكميل:**
• **الجمل**: "السكر حلو والليمون..."
• **الكلمات**: "الأشجار الخضراء..."

**6. نشاط الطرق المتقدم:**
• اكتب أرقام على السبورة
• اطرق على كل رقم بطريقة مختلفة
• الطفل يكرر نفس الطرق على نفس الأرقام
• يربط البصري بالسمعي والحركي

**رابعاً: تحسين العوامل المساعدة**
• **التغذية السليمة**: أوميجا 3، كبدة الفراخ، عين الجمل
• **النوم الكافي**: أكثر من 4 ساعات يومياً
• **النشاط البدني**: تمارين تحسن الدورة الدموية
• **البيئة المناسبة**: هادئة ومنظمة للتدريب

**خطة التدريب الأسبوعية:**
• **الأحد والثلاثاء**: تدريبات الذاكرة البصرية
• **الاثنين والأربعاء**: تدريبات الذاكرة السمعية
• **الخميس والجمعة**: تدريبات الذاكرة العاملة
• **السبت**: مراجعة وأنشطة مختلطة"""
                }
            },

            # الكتابة - متخصص
            "الكتابة": {
                "treatment": {
                    "keywords": [
                        "كيف أعالج مشاكل الكتابة", "علاج الكتابة", "تحسين الكتابة",
                        "علاج الإملاء", "معالجة مشاكل الإملاء", "كيف أحل مشكلة الإملاء"
                    ],
                    "response": """**برنامج علاج مشاكل الكتابة والإملاء المتخصص:**

**أولاً: تشخيص مشاكل الكتابة الشائعة**
• أخطاء إملائية متكررة
• عدم الالتزام بالسطر
• صعوبة مسك القلم والتحكم فيه
• الكتابة المعكوسة أو الكبيرة غير المنتظمة
• بطء شديد في الكتابة

**ثانياً: طرق علاج الإملاء المتخصصة**

**1. الطريقة الأولى - الكتابة المتكررة:**
• **الخطوة 1**: اكتب الكلمة 20 مرة بقلم أزرق
• **الخطوة 2**: الطفل يكتب عليها بقلم أحمر
• **الخطوة 3**: كرر حتى يحفظ الشكل الصحيح
• **أمثلة للتطبيق**: "مدرسة، كتاب، قلم، بيت"

**2. الطريقة الثانية - التنقيط:**
• **الخطوة 1**: انقط الكلمة بنقاط صغيرة
• **الخطوة 2**: الطفل يمشي على النقاط بقلم ملون
• **الخطوة 3**: قلل النقاط تدريجياً حتى يكتب بدونها
• **أمثلة للتطبيق**: "شمس، قمر، نجمة، وردة"

**3. الطريقة الثالثة - التدرج في الطول:**
• **المرحلة 1**: كلمات من 3 حروف (بيت، قطة، ولد)
• **المرحلة 2**: كلمات من 4 حروف (كتاب، قلم، باب)
• **المرحلة 3**: كلمات أطول (مدرسة، مستشفى، مكتبة)

**ثالثاً: علاج مشاكل التآزر البصري الحركي**

**الأنشطة النمائية:**
• **ألعاب البازل**: تنمي التآزر والتركيز
• **الفك والتركيب**: تقوي عضلات اليد الدقيقة
• **اللعب بالصلصال**: يحسن مرونة الأصابع
• **تلوين الأشكال**: يطور التحكم في القلم
• **نقل الحبوب**: من طبق لآخر بالملقط

**التدريبات الأكاديمية:**
• **ترك فواصل**: بين الكلمات في البداية
• **كتابة ملونة**: كل كلمة بلون مختلف
• **الكتابة على كلمات**: مكتوبة بلون فاتح
• **النقل التدريجي**: ورقة → سبورة صغيرة → سبورة كبيرة

**رابعاً: تدريبات متقدمة للإملاء**

**1. الإملاء الصوتي:**
• اقرأ الكلمة بوضوح
• الطفل يكتبها من السماع فقط
• صحح الأخطاء فوراً مع التشجيع
• أمثلة: "شجرة، زهرة، طائر، سيارة"

**2. الإملاء البصري:**
• اعرض الكلمة لـ 5 ثوانٍ
• اخفها واطلب من الطفل كتابتها
• قارن النتيجة مع الأصل
• أمثلة: "طاولة، نافذة، مرآة، ساعة"

**3. الإملاء السياقي:**
• اقرأ جملة ناقصة
• الطفل يكمل الكلمة المفقودة كتابياً
• مثال: "الطائر يطير في ال..." (سماء)

**خامساً: علاج الحروف المتشابهة**

**الحروف البصرية المتشابهة:**
• (ب، ت، ث) - (ج، ح، خ) - (د، ذ) - (ر، ز)
• تدريب: اكتب "بيت" ثم "تين" ثم "ثوب"

**الحروف الصوتية المتشابهة:**
• (س، ص) - (ت، ط) - (ك، ق) - (ز، ظ)
• تدريب: "سمك، صقر" - "تين، طين"

**سادساً: برنامج أسبوعي للإملاء**
• **الأحد**: كلمات 3 حروف
• **الاثنين**: كلمات 4 حروف
• **الثلاثاء**: الحروف المتشابهة
• **الأربعاء**: الإملاء الصوتي
• **الخميس**: الإملاء البصري
• **الجمعة**: مراجعة الأسبوع
• **السبت**: أنشطة تفاعلية وألعاب

**نصائح مهمة للنجاح:**
• ابدأ بالكلمات المألوفة للطفل
• استخدم الألوان لجذب الانتباه
• اعط فترات راحة كل 10 دقائق
• احتفل بكل تقدم مهما كان صغيراً
• تواصل مع المدرسة لتطبيق نفس الطرق"""
                }
            }
        }
        
        return knowledge
    
    def get_specialized_response(self, topic, intent):
        """الحصول على رد متخصص للموضوع والنية"""
        if topic in self.knowledge_dict and intent in self.knowledge_dict[topic]:
            return self.knowledge_dict[topic][intent]["response"]
        return None
    
    def get_all_topics(self):
        """الحصول على جميع المواضيع المتاحة"""
        return list(self.knowledge_dict.keys())
    
    def get_available_intents_for_topic(self, topic):
        """الحصول على النيات المتاحة لموضوع معين"""
        if topic in self.knowledge_dict:
            return list(self.knowledge_dict[topic].keys())
        return []
