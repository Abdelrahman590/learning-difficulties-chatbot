import streamlit as st
import sys
import os
from datetime import datetime

# إضافة المسار للملفات المطلوبة
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from arabic_normlizer import ArabicNormalizer
    from question_intent_analyzer import QuestionIntentAnalyzer
    from knowledge_base import SpecializedKnowledgeBase
    from respond_handler import AdvancedResponseHandler
except ImportError as e:
    st.error(f"خطأ في استيراد الملفات المطلوبة: {e}")
    st.info("تأكد من وجود جميع الملفات المطلوبة في المستودع")
    st.stop()

class StreamlitChatBot:
    """شات بوت صعوبات التعلم مع Streamlit"""
    
    def __init__(self):
        self.initialize_session_state()
        
    def initialize_session_state(self):
        """تهيئة متغيرات الجلسة"""
        if 'chatbot_initialized' not in st.session_state:
            try:
                with st.spinner("🤖 جاري تحميل الشات بوت المحسن..."):
                    st.session_state.chatbot_initialized = True
                    st.session_state.normalizer = ArabicNormalizer()
                    st.session_state.intent_analyzer = QuestionIntentAnalyzer()
                    st.session_state.kb = SpecializedKnowledgeBase("after_cleaning.txt")
                    st.session_state.response_handler = AdvancedResponseHandler(st.session_state.kb)
                    st.session_state.messages = []
                    st.session_state.conversation_count = 0
                st.success("✅ تم تحميل الشات بوت بنجاح!")
            except Exception as e:
                st.error(f"❌ خطأ في تهيئة النظام: {e}")
                st.stop()
    
    def run(self):
        """تشغيل التطبيق"""
        # إعداد الصفحة
        st.set_page_config(
            page_title="شات بوت صعوبات التعلم المتقدم",
            page_icon="🎓",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # العنوان الرئيسي
        st.title("🎓 شات بوت صعوبات التعلم المتقدم")
        st.markdown("**مساعد ذكي متخصص مع نظام تحليل نية متقدم وردود متخصصة دقيقة**")
        st.markdown("---")
        
        # الشريط الجانبي
        self.create_sidebar()
        
        # المحتوى الرئيسي
        self.create_main_content()
    
    def create_sidebar(self):
        """إنشاء الشريط الجانبي"""
        with st.sidebar:
            st.header("🎯 معلومات المساعد")
            
            # معلومات النظام
            st.success("""
            **✨ المميزات الجديدة:**
            • فهم دقيق لنية السؤال
            • ردود متخصصة لكل موضوع
            • تطبيع متقدم للنصوص العربية
            • اقتراحات ذكية مرتبطة بالموضوع
            """)
            
            # المواضيع المتخصصة
            st.info("""
            **🎯 المواضيع المتخصصة:**
            • **الإدراك**: بصري، سمعي، تآزر
            • **الانتباه**: مرونة، مدة، انتقائي
            • **الذاكرة**: قصيرة، طويلة، عاملة
            • **الكتابة**: إملاء، خط، تآزر حركي
            • **صعوبات التعلم**: تعريف، أنواع، علاج
            """)
            
            # أمثلة على الأسئلة
            st.markdown("**💡 أمثلة على الأسئلة:**")
            example_questions = [
                "كيف أعالج مشاكل الإدراك؟",
                "ما هو الانتباه الانتقائي؟",
                "طرق تحسين الذاكرة العاملة",
                "كيف أحل مشكلة الإملاء؟",
                "أنواع صعوبات التعلم"
            ]
            
            for question in example_questions:
                if st.button(f"📝 {question}", key=f"example_{question}", use_container_width=True):
                    st.session_state.example_question = question
                    st.rerun()
            
            st.markdown("---")
            
            # أدوات التحكم
            st.subheader("🛠️ أدوات التحكم")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ مسح المحادثة", use_container_width=True):
                    st.session_state.messages = []
                    st.session_state.response_handler.conversation_history = []
                    st.session_state.conversation_count = 0
                    st.rerun()
            
            with col2:
                if st.button("🧪 اختبار النظام", use_container_width=True):
                    self.run_system_test()
            
            # إحصائيات
            st.markdown("---")
            st.subheader("📊 إحصائيات الجلسة")
            st.metric("عدد الرسائل", len(st.session_state.messages))
            st.metric("عدد المحادثات", st.session_state.conversation_count)
    
    def create_main_content(self):
        """إنشاء المحتوى الرئيسي"""
        # عرض المحادثات السابقة
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # معالجة السؤال من الأمثلة
        if hasattr(st.session_state, 'example_question'):
            self.process_question(st.session_state.example_question)
            del st.session_state.example_question
        
        # مربع إدخال الرسالة
        if prompt := st.chat_input("اكتب سؤالك هنا... (يمكن أن يحتوي على أخطاء إملائية)"):
            self.process_question(prompt)
    
    def process_question(self, user_input):
        """معالجة السؤال وعرض الرد"""
        # إضافة رسالة المستخدم
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # معالجة السؤال وإظهار التحليل
        with st.chat_message("assistant"):
            with st.spinner("🤖 جاري تحليل السؤال والبحث عن الإجابة..."):
                # تحليل السؤال
                intent = st.session_state.intent_analyzer.analyze_intent(user_input)
                topic = st.session_state.intent_analyzer.extract_main_topic(user_input)
                confidence = st.session_state.intent_analyzer.get_confidence_score(user_input, intent, topic)
                
                # عرض تحليل السؤال (اختياري)
                with st.expander("🔍 تحليل السؤال (اضغط للعرض)", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("النية المكتشفة", intent)
                    with col2:
                        st.metric("الموضوع المكتشف", topic or "غير محدد")
                    with col3:
                        st.metric("مستوى الثقة", f"{confidence:.2f}")
                
                # الحصول على الرد
                response = st.session_state.response_handler.process_user_input(user_input)
                
                # عرض الرد
                st.markdown(response)
                
                # حفظ الرد
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.conversation_count += 1
    
    def run_system_test(self):
        """تشغيل اختبار النظام"""
        st.sidebar.markdown("### 🧪 نتائج اختبار النظام")
        
        test_cases = [
            ("كيف أعالج مشاكل الإدراك؟", "treatment", "الإدراك"),
            ("ما هو الانتباه الانتقائي؟", "definition", "الانتباه"),
            ("طرق تحسين الذاكرة العاملة", "treatment", "الذاكرة"),
            ("كيف أحل مشكلة الإملاء؟", "treatment", "الكتابة"),
        ]
        
        success_count = 0
        
        for i, (test_input, expected_intent, expected_topic) in enumerate(test_cases, 1):
            intent = st.session_state.intent_analyzer.analyze_intent(test_input)
            topic = st.session_state.intent_analyzer.extract_main_topic(test_input)
            
            intent_correct = intent == expected_intent
            topic_correct = topic == expected_topic
            
            if intent_correct and topic_correct:
                success_count += 1
                status = "✅"
            else:
                status = "❌"
            
            st.sidebar.text(f"{status} اختبار {i}: {intent_correct and topic_correct}")
        
        accuracy = (success_count / len(test_cases)) * 100
        st.sidebar.metric("دقة النظام", f"{accuracy:.1f}%")
        
        if accuracy >= 80:
            st.sidebar.success("🎉 النظام يعمل بكفاءة عالية!")
        else:
            st.sidebar.warning("⚠️ النظام يحتاج تحسينات")

def main():
    """الدالة الرئيسية للتطبيق"""
    chatbot = StreamlitChatBot()
    chatbot.run()

if __name__ == "__main__":
    main()
