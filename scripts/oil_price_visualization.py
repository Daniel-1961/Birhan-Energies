import pandas as pd
import plotly.express as px

def scatter_plot_with_color_coding(historical_file, change_points_file):
    # Read the .csv files
    historical_data = pd.read_csv(historical_file)
    change_points_data = pd.read_csv(change_points_file)

    # Convert 'Date' columns to datetime
    historical_data['Date'] = pd.to_datetime(historical_data['Date'])
    change_points_data['Date'] = pd.to_datetime(change_points_data['change_point_date'])

    # Merge the dataframes on 'Date'
    merged_data = pd.merge(historical_data, change_points_data, on='Date', how='left')

    # Create line chart for historical oil prices
    fig = px.line(merged_data, x='Date', y='Price', title='Historical Oil Prices with Change Points and Major Events')

    # Add scatter points for change points
    fig.add_scatter(x=merged_data[merged_data['change_point_date'].notna()]['Date'],
                    y=merged_data[merged_data['change_point_date'].notna()]['oil_price'],
                    mode='markers', name='Change Points', marker=dict(color='red', size=10))

    # Add text annotations for major events
    for index, row in merged_data[merged_data['event_description'].notna()].iterrows():
        fig.add_annotation(x=row['Date'], y=row['Price'], text=row['event_description'], showarrow=True, arrowhead=2)


# Show figure

    # Show figure
    fig.show()
