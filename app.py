from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Modern HTML template with Chart.js and Bootstrap for styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>IDS Live Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <meta http-equiv="refresh" content="5"> </head>
<body class="bg-dark text-white">
    <div class="container mt-4">
        <h1 class="text-center mb-4">🛡️ IDS Monitor</h1>
        
        <div class="row">
            <div class="col-md-6 mb-4">
                <div class="card bg-secondary text-white">
                    <div class="card-body">
                        <h5 class="card-title">Threat Distribution</h5>
                        <canvas id="threatChart"></canvas>
                    </div>
                </div>
            </div>

            <div class="col-md-6 mb-4">
                <div class="card bg-secondary text-white">
                    <div class="card-body text-center">
                        <h5 class="card-title">Total Alerts Detected</h5>
                        <h1 class="display-1 text-danger">{{ total_alerts }}</h1>
                    </div>
                </div>
            </div>
        </div>

        <div class="card bg-secondary text-white">
            <div class="card-body">
                <h5 class="card-title">Recent Alerts</h5>
                <table class="table table-dark table-hover mt-3">
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>Source IP</th>
                            <th>Threat Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for row in rows %}
                        <tr>
                            <td>{{ row[0] }}</td>
                            <td><span class="badge bg-danger">{{ row[1] }}</span></td>
                            <td>{{ row[2] }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('threatChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: {{ labels|tojson }},
                datasets: [{
                    data: {{ data|tojson }},
                    backgroundColor: ['#ff6384', '#36a2eb', '#ffce56', '#4bc0c0']
                }]
            },
            options: { responsive: true, plugins: { legend: { labels: { color: 'white' } } } }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    conn = sqlite3.connect('ids_logs.db')
    cur = conn.cursor()
    
    # Get all alerts for the table
    cur.execute("SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 15")
    rows = cur.fetchall()
    
    # Get stats for the chart
    cur.execute("SELECT threat_type, COUNT(*) FROM alerts GROUP BY threat_type")
    chart_data = cur.fetchall()
    
    labels = [row[0] for row in chart_data]
    data = [row[1] for row in chart_data]
    total_alerts = sum(data)
    
    conn.close()
    return render_template_string(HTML_TEMPLATE, rows=rows, labels=labels, data=data, total_alerts=total_alerts)

if __name__ == "__main__":
    app.run(port=5000, debug=False)