from autoscraper import AutoScraper
from flask import Flask, request, jsonify ,render_template

scraper = AutoScraper()
scraper.load('github')
app = Flask(__name__)

def get_github_result(search_query):
    url = f'https://github.com/topics/{search_query}'
    result = scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    for i in range(len(list(result.values())[0])):
        try:
            final_result.append({alias: result[alias][i] for alias in result})
        except IndexError:
            pass
    return final_result

@app.route('/<topic>', methods=['GET'])
def search_api(topic):
    result = get_github_result(topic)
    return jsonify(result)

@app.route('/')
def fornt():
    
    return render_template("hello")

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0',debug=True)
