from flask import Flask, render_template, request, jsonify
from index import main_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    sort_by = request.form.get('sort', 'relevance')
    limit = int(request.form.get('limit', 10))
    search_type = request.form.get('type', 'all')
    
    results = main_query(query)
    
    # Apply sorting
    if sort_by == 'title':
        results.sort(key=lambda x: x[1].lower())
    elif sort_by == 'date':
        # For now, keep original order since we don't have dates
        pass
    
    # Apply limit
    results = results[:limit]
    
    return jsonify({"data": results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)