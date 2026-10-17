import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6, label='Datos')

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )

    # Create second line of best fit
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    line1 = intercept1 + slope1 * years_extended
    ax.plot(years_extended, line1, 'r', label='Ajuste 1880-2050')
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    # Add labels and title
    years_recent = pd.Series(range(2000, 2051))
    line2 = intercept2 + slope2 * years_recent
    ax.plot(years_recent, line2, 'green', label='Ajuste 2000-2050')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()