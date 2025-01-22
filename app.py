from flask import Flask, render_template
import numpy as np
from scipy import stats
from data import spending_data  # Import the spending data

app = Flask(__name__)

@app.route('/')
def home():
    statistics = {}
    
    for category, data in spending_data.items():
        mean = np.mean(data)
        median = np.median(data)
        mode_result = stats.mode(data)
        
        if isinstance(mode_result.mode, np.ndarray):
            mode = mode_result.mode[0] if mode_result.mode.size > 0 else 'No Mode'
        else:
            mode = mode_result.mode if mode_result.mode else 'No Mode'
        
        variance = np.var(data)
        std_dev = np.std(data)
        
        statistics[category] = {
            'mean': mean,
            'median': median,
            'mode': mode,
            'variance': variance,
            'std_dev': std_dev
        }

    return render_template('index.html', statistics=statistics)

if __name__ == '__main__':
    app.run(debug=True)