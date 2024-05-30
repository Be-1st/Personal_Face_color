import sys
import os
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
        try:
            result = personal_color.analysis(file_path)
            img_url = url_for('uploaded_file', filename=file.filename)
            return render_template('result.html', result=result, img_url=img_url)
        except ValueError as e:
            result = str(e)
            img_url = url_for('uploaded_file', filename=file.filename)
            return render_template('result.html', result=result, img_url=img_url)
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
