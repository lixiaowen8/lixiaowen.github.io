from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

# 不存在数据文件则自动创建
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

# 问卷首页路由
@app.route('/')
def index():
    return render_template("index.html")

# 接收表单提交
@app.route('/submit', methods=["POST"])
def submit():
    form_data = {
        "name": request.form.get("name"),
        "gender": request.form.get("gender"),
        "age": request.form.get("age"),
        "major": request.form.get("major"),
        "ai_use_freq": request.form.get("ai_use_freq"),
        "ai_tool": request.form.getlist("ai_tool"),
        "ai_satisfaction": request.form.get("ai_satisfaction"),
        "suggest": request.form.get("suggest")
    }
    # 读取旧数据
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data_list = json.load(f)
    data_list.append(form_data)
    # 保存新数据
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)
    return """
    <h3>问卷提交成功！感谢填写</h3>
    <a href="/">返回问卷首页</a>
    """

# 查看所有收集数据
@app.route('/data')
def show_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)