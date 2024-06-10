from flask import Flask, render_template_string
import re

app = Flask(__name__)

# Path to the fail2ban log file
LOG_FILE_PATH = '/var/log/fail2ban.log'

# Regular expression to parse the log lines
LOG_PATTERN = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
    r'(?P<time>\d{2}:\d{2}:\d{2}),\d+\s+'
    r'(?P<service>\S+)\s+\[(?P<pid>\d+)\]:\s+'
    r'(?P<log_level>\w+)\s+'
    r'(?P<message>.*$)'
)

def parse_logs():
    logs = []
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            for line in file:
                match = LOG_PATTERN.match(line)
                if match:
                    log = match.groupdict()
                    # Extract IP address if present in the message
                    ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log['message'])
                    log['ip'] = ip_match.group(0) if ip_match else 'N/A'
                    logs.append(log)
                else:
                    # Print unmatched lines for debugging
                    print(f"No match for line: {line.strip()}")
    except FileNotFoundError:
        logs.append({'date': 'N/A', 'time': 'N/A', 'log_level': 'ERROR', 'service': 'fail2ban', 'message': 'Log file not found', 'ip': 'N/A'})
    return logs

@app.route('/')
def home():
    logs = parse_logs()
    return render_template_string("""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Fail2Ban Logs</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body>
        <div class="container">
          <h1 class="mt-5">Fail2Ban Logs</h1>
          <table class="table table-bordered mt-3">
            <thead>
              <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Log Level</th>
                <th>Service</th>
                <th>Message</th>
                <th>IP Address</th>
              </tr>
            </thead>
            <tbody>
              {% for log in logs %}
              <tr>
                <td>{{ log.date }}</td>
                <td>{{ log.time }}</td>
                <td>{{ log.log_level }}</td>
                <td>{{ log.service }}</td>
                <td>{{ log.message }}</td>
                <td>{{ log.ip }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
      </body>
    </html>
    """, logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
