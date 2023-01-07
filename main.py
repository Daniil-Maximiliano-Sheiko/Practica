from flask import Flask, render_template, request
    
import re
from collections import Counter


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files['file'].read()
        txt = str(f.decode('utf-8'))
        
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips = re.findall(pattern, txt)
        
        result = Counter(ips).most_common(10)
        
        ban=[]
        for key, value in result:
            if value>100:
                ban.append({'ip': key, 'frequency': value})
        ipNoban=[]
        for key, value in result:
            if 1>=value<100:
                ipNoban.append({'ip': key, 'frequency': value})
        
        return render_template('index.html', ipban=ban, ipNoban=ipNoban)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
