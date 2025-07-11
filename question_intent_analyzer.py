import re
from arabic_normlizer import ArabicNormalizer

class QuestionIntentAnalyzer:
    """محلل نية الأسئلة المتقدم"""
    
    def __init__(self):
        self.normalizer = ArabicNormalizer()
        self.intent_patterns = {
            "treatment": [
                "كيف أعالج", "كيفية علاج", "طرق علاج", "علاج", 
                "كيف أحل", "حل مشكلة", "طريقة حل", "أساليب علاج",
                "تدريب", "تأهيل", "تحسين", "تطوير", "معالجة",
                "كيف اعالج", "ازاي اعالج", "ايه العلاج", "طريقه علاج"
            ],
            "definition": [
                "ما هي", "تعريف", "مفهوم", "معنى", "شرح", "وضح",
                "ايه هي", "يعني ايه", "المقصود", "مفهوم"
            ],
            "types": [
                "أنواع", "أقسام", "تصنيف", "فئات", "مراحل", "تقسيم",
                "انواع", "اقسام", "تصنيفات"
            ],
            "symptoms": [
                "أعراض", "علامات", "مظاهر", "كيف أعرف", "ازاي اعرف",
                "اعراض", "علامات", "مظاهر"
            ],
            "causes": [
                "أسباب", "لماذا", "ليه", "السبب", "اسباب", "سبب"
            ],
            "identification": [
                "كيف أميز", "التمييز", "تحديد", "معرفة نوع", "ازاي اميز",
                "الفرق بين", "كيف افرق"
            ]
        }
        
        # خريطة المواضيع المتخصصة
        self.topic_keywords = {
            "الإدراك": [
                "إدراك", "ادراك", "تمييز", "فهم", "مثيرات", "بصري", "سمعي", 
                "حسي", "تآزر", "تازر", "إدراك بصري", "إدراك سمعي"
            ],
            "الانتباه": [
                "انتباه", "انتباة", "إنتباه", "تشتت", "تركيز", "تركيذ", 
                "مدة الانتباه", "مرونة", "الانتباه الانتقائي", "مش بيركز", 
                "بيتشتت", "شارد", "تشتيت"
            ],
            "الذاكرة": [
                "ذاكرة", "ذاكره", "حفظ", "استدعاء", "تذكر", "نسيان", 
                "ذاكرة قصيرة", "ذاكرة طويلة", "ذاكرة عاملة", "تذكر"
            ],
            "الكتابة": [
                "كتابة", "كتابه", "إملاء", "املاء", "خط", "تهجئة", "تهجئه",
                "أخطاء كتابية", "هجاء", "أخطاء إملائية", "اخطاء املائيه"
            ],
            "القراءة": [
                "قراءة", "قراءه", "حروف", "مقاطع", "نصوص", "كلمات", 
                "أخطاء القراءة", "تهجئة", "نطق", "فهم القراءة"
            ],
            "الحساب": [
                "حساب", "رياضيات", "رياضه", "أرقام", "ارقام", "جمع", "طرح", 
                "ضرب", "قسمة", "عمليات حسابية", "مفاهيم رياضية"
            ],
            "صعوبات_التعلم": [
                "صعوبات التعلم", "صعوبات التعليم", "مشاكل التعلم", 
                "إصعوبات التعلم", "صعوبات تعلم"
            ]
        }
    
    def analyze_intent(self, user_input):
        """تحليل نية السؤال"""
        normalized_input = self.normalizer.normalize(user_input)
        
        # البحث عن أنماط النية مع حساب الأولوية
        intent_scores = {}
        
        for intent, patterns in self.intent_patterns.items():
            score = 0
            for pattern in patterns:
                normalized_pattern = self.normalizer.normalize(pattern)
                if normalized_pattern in normalized_input:
                    # إعطاء نقاط أعلى للتطابق الدقيق
                    if normalized_pattern == normalized_input:
                        score += 5
                    else:
                        score += 2
            intent_scores[intent] = score
        
        # إرجاع النية ذات أعلى نقاط
        if intent_scores:
            best_intent = max(intent_scores, key=intent_scores.get)
            if intent_scores[best_intent] > 0:
                return best_intent
        
        return "general"
    
    def extract_main_topic(self, user_input):
        """استخراج الموضوع الرئيسي من السؤال"""
        normalized_input = self.normalizer.normalize(user_input)
        
        topic_scores = {}
        
        for topic, keywords in self.topic_keywords.items():
            score = 0
            for keyword in keywords:
                normalized_keyword = self.normalizer.normalize(keyword)
                if normalized_keyword in normalized_input:
                    # إعطاء نقاط أعلى للكلمات الأطول (أكثر تحديداً)
                    score += len(normalized_keyword.split())
            topic_scores[topic] = score
        
        # إرجاع الموضوع ذو أعلى نقاط
        if topic_scores:
            best_topic = max(topic_scores, key=topic_scores.get)
            if topic_scores[best_topic] > 0:
                return best_topic
        
        return None
    
    def get_confidence_score(self, user_input, intent, topic):
        """حساب مستوى الثقة في التحليل"""
        normalized_input = self.normalizer.normalize(user_input)
        
        intent_confidence = 0
        topic_confidence = 0
        
        # حساب ثقة النية
        if intent in self.intent_patterns:
            for pattern in self.intent_patterns[intent]:
                normalized_pattern = self.normalizer.normalize(pattern)
                if normalized_pattern in normalized_input:
                    intent_confidence += 1
        
        # حساب ثقة الموضوع
        if topic and topic in self.topic_keywords:
            for keyword in self.topic_keywords[topic]:
                normalized_keyword = self.normalizer.normalize(keyword)
                if normalized_keyword in normalized_input:
                    topic_confidence += 1
        
        # حساب النقاط الإجمالية
        total_words = len(normalized_input.split())
        confidence = (intent_confidence + topic_confidence) / max(total_words, 1)
        
        return min(confidence, 1.0)  # تحديد الحد الأقصى بـ 1.0
