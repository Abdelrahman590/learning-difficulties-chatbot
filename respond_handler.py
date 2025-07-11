import re
from datetime import datetime
from arabic_normlizer import ArabicNormalizer
from question_intent_analyzer import QuestionIntentAnalyzer
from knowledge_base import SpecializedKnowledgeBase

class AdvancedResponseHandler:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.normalizer = ArabicNormalizer()
        self.intent_analyzer = QuestionIntentAnalyzer()
        self.conversation_history = []
    
    def process_user_input(self, user_input):
        """معالجة متقدمة لمدخلات المستخدم مع التخصص الدقيق"""
        user_input = user_input.strip()
        
        # حفظ المحادثة
        self.conversation_history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_input": user_input,
            "response": None
        })
        
        # تحليل النية والموضوع
        intent = self.intent_analyzer.analyze_intent(user_input)
        topic = self.intent_analyzer.extract_main_topic(user_input)
        confidence = self.intent_analyzer.get_confidence_score(user_input, intent, topic)
        
        print(f"🔍 تحليل السؤال: النية={intent}, الموضوع={topic}, الثقة={confidence:.2f}")
        
        # البحث المتخصص
        response = self.get_specialized_response(user_input, intent, topic, confidence)
        
        # تحديث تاريخ المحادثة
        self.conversation_history[-1]["response"] = response
        
        return response
    
    def get_specialized_response(self, user_input, intent, topic, confidence):
        """الحصول على رد متخصص بناءً على التحليل"""
        
        # إذا كان التحليل واضح ومؤكد
        if confidence > 0.7 and topic and intent:
            specialized_response = self.kb.get_specialized_response(topic, intent)
            if specialized_response:
                return self.enhance_response_with_suggestions(specialized_response, topic, intent)
        
        # إذا كان الموضوع واضح لكن النية غير مؤكدة
        if topic and confidence > 0.5:
            return self.get_topic_based_response(topic, intent)
        
        # البحث التقليدي كخطة احتياطية
        fallback_response = self.fallback_search(user_input)
        if fallback_response:
            return fallback_response
        
        # الرد الافتراضي المحسن
        return self.get_enhanced_default_response(user_input, intent, topic)
    
    def get_topic_based_response(self, topic, intent):
        """الحصول على رد مبني على الموضوع حتى لو كانت النية غير واضحة"""
        
        # ترتيب أولوية النيات
        intent_priority = ["treatment", "definition", "types", "symptoms"]
        
        # جرب النية المحددة أولاً
        if intent != "general":
            response = self.kb.get_specialized_response(topic, intent)
            if response:
                return response
        
        # جرب النيات حسب الأولوية
        for priority_intent in intent_priority:
            response = self.kb.get_specialized_response(topic, priority_intent)
            if response:
                return f"**ملاحظة**: لم أجد معلومات محددة لسؤالك، لكن إليك معلومات مفيدة عن {topic}:\n\n{response}"
        
        return None
    
    def enhance_response_with_suggestions(self, response, topic, intent):
        """تحسين الرد بإضافة اقتراحات ذات صلة"""
        
        suggestions = self.get_related_suggestions(topic, intent)
        
        if suggestions:
            response += "\n\n💡 **اقتراحات إضافية قد تهمك:**\n"
            for suggestion in suggestions:
                response += f"• {suggestion}\n"
        
        return response
    
    def get_related_suggestions(self, topic, current_intent):
        """الحصول على اقتراحات ذات صلة بالموضوع"""
        
        suggestions_map = {
            "الإدراك": {
                "treatment": [
                    "هل تريد معرفة تدريبات التمييز البصري المحددة؟",
                    "هل تحتاج معلومات عن التآزر البصري الحركي؟",
                    "هل تريد تمارين للإدراك السمعي؟"
                ],
                "definition": [
                    "هل تريد معرفة طرق علاج مشاكل الإدراك؟",
                    "هل تحتاج معلومات عن أنواع الإدراك المختلفة؟"
                ]
            },
            "الانتباه": {
                "treatment": [
                    "هل تريد تدريبات لزيادة مدة الانتباه؟",
                    "هل تحتاج أنشطة لتحسين مرونة الانتباه؟",
                    "هل تريد علاج مشاكل التشتت المحددة؟"
                ],
                "definition": [
                    "هل تريد معرفة طرق علاج مشاكل الانتباه؟",
                    "هل تحتاج معلومات عن أنواع الانتباه المختلفة؟"
                ]
            },
            "الذاكرة": {
                "treatment": [
                    "هل تريد تدريبات الذاكرة قصيرة المدى؟",
                    "هل تحتاج تمارين الذاكرة العاملة المتقدمة؟",
                    "هل تريد نصائح لتحسين العوامل المؤثرة على الذاكرة؟"
                ],
                "definition": [
                    "هل تريد معرفة طرق علاج مشاكل الذاكرة؟",
                    "هل تحتاج معلومات عن أنواع الذاكرة المختلفة؟"
                ]
            },
            "الكتابة": {
                "treatment": [
                    "هل تريد تفاصيل أكثر عن طريقة التنقيط؟",
                    "هل تحتاج تدريبات للحروف المتشابهة؟",
                    "هل تريد برنامج أسبوعي للإملاء؟"
                ]
            }
        }
        
        if topic in suggestions_map and current_intent in suggestions_map[topic]:
            return suggestions_map[topic][current_intent]
        
        return []
    
    def fallback_search(self, user_input):
        """البحث الاحتياطي في حالة فشل التحليل المتخصص"""
        normalized_input = self.normalizer.normalize(user_input)
        
        # البحث في جميع المواضيع والنيات
        best_response = None
        max_score = 0
        
        for topic in self.kb.get_all_topics():
            for intent in self.kb.get_available_intents_for_topic(topic):
                topic_data = self.kb.knowledge_dict[topic][intent]
                score = 0
                
                for keyword in topic_data["keywords"]:
                    normalized_keyword = self.normalizer.normalize(keyword)
                    
                    if normalized_keyword in normalized_input:
                        score += 3
                    elif any(word in normalized_keyword for word in normalized_input.split()):
                        score += 1
                
                if score > max_score:
                    max_score = score
                    best_response = topic_data["response"]
        
        return best_response if max_score > 0 else None
    
    def get_enhanced_default_response(self, user_input, intent, topic):
        """رد افتراضي محسن مع اقتراحات ذكية"""
        
        base_message = "عذراً، لم أفهم سؤالك بوضوح."
        
        # اقتراحات بناءً على التحليل الجزئي
        suggestions = []
        
        if topic:
            suggestions.append(f"**يبدو أن سؤالك يتعلق بـ {topic}. يمكنك السؤال عن:**")
            if topic == "الإدراك":
                suggestions.extend([
                    "• كيف أعالج مشاكل الإدراك؟",
                    "• ما هو الإدراك البصري؟",
                    "• أنواع الإدراك السمعي"
                ])
            elif topic == "الانتباه":
                suggestions.extend([
                    "• كيف أعالج مشاكل الانتباه؟",
                    "• ما هو الانتباه الانتقائي؟",
                    "• طرق تحسين مدة الانتباه"
                ])
            elif topic == "الذاكرة":
                suggestions.extend([
                    "• كيف أعالج مشاكل الذاكرة؟",
                    "• ما هي الذاكرة العاملة؟",
                    "• تدريبات تقوية الذاكرة"
                ])
        
        if intent and intent != "general":
            if intent == "treatment":
                suggestions.append("**يبدو أنك تبحث عن طرق العلاج. جرب:**")
                suggestions.extend([
                    "• كيف أعالج مشاكل الإدراك؟",
                    "• طرق علاج الانتباه",
                    "• تدريبات تحسين الذاكرة"
                ])
        
        if not suggestions:
            suggestions = [
                "**💡 يمكنك السؤال عن:**",
                "",
                "**للعلاج والحلول:**",
                "• كيف أعالج مشاكل الإدراك؟",
                "• طرق علاج الانتباه",
                "• كيفية تحسين الكتابة والإملاء",
                "",
                "**للتعريفات:**",
                "• ما هو الإدراك؟",
                "• تعريف الانتباه",
                "• مفهوم الذاكرة",
                "",
                "**للأنواع والتصنيفات:**",
                "• أنواع الإدراك",
                "• أنواع مشاكل الانتباه"
            ]
        
        return f"{base_message}\n\n" + "\n".join(suggestions) + "\n\n🔄 **جرب إعادة صياغة السؤال بوضوح أكثر**"
    
    def get_conversation_history(self):
        """إرجاع تاريخ المحادثة"""
        return self.conversation_history
    
    def multi_level_search(self, user_input):
        """دالة للتوافق مع الكود القديم"""
        intent = self.intent_analyzer.analyze_intent(user_input)
        topic = self.intent_analyzer.extract_main_topic(user_input)
        
        if topic and topic in self.kb.knowledge_dict:
            return topic
        
        return None
