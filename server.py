from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# استخدام مكتبة TMDB كقاعدة بيانات جلب أحدث المسلسلات والأفلام فور نزولها
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

@app.route('/api/latest', methods=['GET'])
def get_latest_content():
    """جلب أحدث المحتويات المضافة"""
    endpoint = f"{TMDB_BASE_URL}/trending/all/day?api_key={TMDB_API_KEY}&language=ar"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        data = response.json()
        results = []
        for item in data.get('results', []):
            results.append({
                'id': item.get('id'),
                'title': item.get('title') or item.get('name'),
                'type': item.get('media_type'),
                'poster': f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}",
                'stream_url': f"https://your-server.com/stream/{item.get('id')}" # رابط البث المباشر
            })
        return jsonify({"status": "success", "data": results})
    return jsonify({"status": "error", "message": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
