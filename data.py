import random

# Creating a fictional dataset based on average spending habits in USD
# Note: These numbers are illustrative and not based on real data

# Categories and their average monthly spending (fictional numbers)
categories = {
    "Housing": 1200,
    "Food": 600,
    "Transportation": 400,
    "Healthcare": 300,
    "Entertainment": 200,
    "Savings/Investments": 300,
    "Miscellaneous": 200
}

# Generate 100 entries for each category with some variation
def generate_data():
    data = {}
    for category, avg_spend in categories.items():
        # Add some random variation to simulate real-world spending
        data[category] = [round(random.uniform(avg_spend * 0.8, avg_spend * 1.2), 2) for _ in range(100)]
    return data

spending_data = generate_data()