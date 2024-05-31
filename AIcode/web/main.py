from flask import Flask, request, render_template, send_from_directory, url_for
import os
import re
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from personal_color_analysis import personal_color

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        try:
            full_result = personal_color.analysis(file_path)
            match = re.search(r'퍼스널 컬러는 (.+)', full_result)
            if match:
                result = match.group(1)
            else:
                result = "결과를 찾을 수 없습니다."

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
        except ValueError as e:
            result = str(e)
            return render_template('error.html', result=result, css_url='error.css')

        img_url = url_for('uploaded_file', filename=file.filename)
        css_url = url_for('static', filename=f'css/{css_file}') if css_file else ''
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


if __name__ == '__main__':
    app.run(debug=True)

