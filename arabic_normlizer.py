import re

class ArabicNormalizer:
    """مطبع النصوص العربية المتقدم"""
    
    def __init__(self):
        self.normalization_rules = {
            # تطبيع الهمزات - الأهم
            r'[أإآا]': 'ا',
            # تطبيع الياء
            r'ى': 'ي',
            # تطبيع التاء المربوطة
            r'ة': 'ه',
            # تطبيع الهمزة على الواو والياء
            r'ؤ': 'و',
            r'ئ': 'ي',
            # إزالة التشكيل
            r'[\u064B-\u0652\u0670\u0640]': '',
            # تطبيع المسافات
            r'\s+': ' '
        }
    
    def normalize(self, text):
        """تطبيع النص العربي"""
        if not text:
            return ""
        
        # تطبيق قواعد التطبيع
        for pattern, replacement in self.normalization_rules.items():
            text = re.sub(pattern, replacement, text)
        
        return text.strip().lower()
    
    def normalize_keywords(self, keywords_list):
        """تطبيع قائمة من الكلمات المفتاحية"""
        return [self.normalize(keyword) for keyword in keywords_list]
