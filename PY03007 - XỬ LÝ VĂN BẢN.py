import re
import sys

def process_text(text):
    # Thay thế các dấu ngắt câu bằng ký tự xuống dòng
    cleaned_text = re.sub(r'[.!?]', '\n', text)
    
    # Tách văn bản thành các câu dựa trên ký tự xuống dòng
    sentences = cleaned_text.splitlines()
    
    formatted_sentences = []
    for sentence in sentences:
        # Xóa khoảng trắng dư thừa trong câu
        sentence = ' '.join(sentence.split()).strip()
        if sentence:  # Chỉ thêm câu không rỗng
            # Định dạng câu: viết hoa ký tự đầu tiên và viết thường các ký tự còn lại
            formatted_sentence = sentence.lower().capitalize()
            formatted_sentences.append(formatted_sentence)
    
    return formatted_sentences

def main():
    text = ""
    while True:
        try:
            line = input()
            text += line  # Thêm ký tự xuống dòng để tách các dòng văn bản
        except EOFError:
            break
    
    formatted_sentences = process_text(text)
    
    for sentence in formatted_sentences:
        print(sentence)

if __name__ == "__main__":
    main()