import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from metaflow.cards import Image
from metaflow import FlowSpec, step, card, current

class SimpleCardFlow(FlowSpec):
    """A simple flow that creates basic cards with data visualization."""

    @step
    def start(self):
        """Generate some simple data."""
        print("Creating simple dataset...")
        
        # Simple sales data
        self.data = pd.DataFrame({
            'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'sales': [100, 150, 130, 200, 180]
        })
        
        self.next(self.analyze)

    @card(type='html')
    @step
    def analyze(self):
        """Analyze data and create a simple card."""
        
        # Calculate basic stats
        total_sales = self.data['sales'].sum()
        avg_sales = self.data['sales'].mean()
        best_month = self.data.loc[self.data['sales'].idxmax(), 'month']
        
        # Create simple HTML card
        self.html = f"""
        <h2>Sales Report</h2>
        <p><strong>Total Sales:</strong> {total_sales}</p>
        <p><strong>Average Sales:</strong> {avg_sales:.1f}</p>
        <p><strong>Best Month:</strong> {best_month}</p>
        """
        
        # current.card.append(self.html)
        self.next(self.create_chart)

    @card(type='blank') 
    @step
    def create_chart(self):
        """Create a simple chart."""
        
        # Make a basic bar chart
        fig = plt.figure(figsize=(8, 15))
        plt.bar(self.data['month'], self.data['sales'], color='blue')
        plt.title('Monthly Sales')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        
        # Simple HTML with embedded image
        # self.html = f"""
        # <h2>Sales Chart</h2>
        # <img src="data:image/png;base64,{image_data}" style="width: 100%; max-width: 600px;">
        # """
        
        current.card.append(Image.from_matplotlib(fig))
        self.next(self.end)

    @step
    def end(self):
        """End the flow."""
        print("Done! Check your cards.")

if __name__ == "__main__":
    SimpleCardFlow()