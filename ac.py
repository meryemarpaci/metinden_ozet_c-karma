import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import heapq

def extract_summary(text, language):
    # Metni cümlelere ayır
    sentences = sent_tokenize(text, language=language)
    
    # Stopwords'leri yükle
    stop_words = set(stopwords.words(language))
    
    # Kelimeleri ve cümleleri işle
    word_freq = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence.lower(), language=language)
        for word in words:
            # Gereksiz kelimeleri ve noktalama işaretlerini çıkar
            if word not in stop_words and word.isalpha():
                word_freq[word] += 1
    
    # Cümlelerin önemini hesapla
    sentence_scores = defaultdict(float)
    for sentence in sentences:
        words = word_tokenize(sentence.lower(), language=language)
        for word in words:
            # Gereksiz kelimeleri ve noktalama işaretlerini çıkar
            if word not in stop_words and word.isalpha():
                sentence_scores[sentence] += word_freq[word]
        sentence_scores[sentence] /= len(words)
    
    # Özeti oluştur
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary

def main():
    st.title("Metinden Özet Çıkarma Uygulaması")
    # Dil seçimi
    language = st.selectbox("Metni hangi dilde gireceksiniz?", ["İngilizce", "Türkçe"])

    # Metin giriş kutusu oluştur
    text = st.text_area("Metin Kutusu", "Metin buraya girilir...")

    if st.button("Özeti Bul"):
        # Özeti bul
        summary = extract_summary(text, "english" if language == "İngilizce" else "turkish")
        
        st.write("Özet:")
        st.write(summary)

if __name__ == "__main__":
    main()
