import sys
import os
import re
from flask import Flask, request, render_template, send_from_directory, url_for

# src 디렉토리를 파이썬 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from personal_color_analysis import personal_color

app = Flask(__name__)

# 업로드된 파일을 저장할 디렉토리 경로 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        full_result = personal_color.analysis(file_path)
        
        # 정규 표현식을 사용하여 "퍼스널 컬러는 " 이후의 부분만 추출
        match = re.search(r'퍼스널 컬러는 (.+)', full_result)
        if match:
            result = match.group(1)
        else:
            result = "결과를 찾을 수 없습니다."

        # result에 따라 CSS 파일 경로 지정
        if '봄웜톤(spring)' in result:
            css_file = 'spring.css'
        elif '여름쿨톤(summer)' in result:
            css_file = 'summer.css'
        elif '가을웜톤(fall)' in result:
            css_file = 'fall.css'
        elif '겨울쿨톤(winter)' in result:
            css_file = 'winter.css'
        else:
            css_file = ''

        img_url = url_for('uploaded_file', filename=file.filename)
        css_url = url_for('static', filename=f'css/{css_file}')
        return render_template('result.html', result=result, img_url=img_url, css_url=css_url)
    return render_template('web.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/develop')
def develop():
    return render_template('develop.html')

if __name__ == '__main__':
    app.run(debug=True)
