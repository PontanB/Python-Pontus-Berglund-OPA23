import pandas as pd
import matplotlib.pyplot as plt

def plot_missing_values(df):
    """
    Plot a barplot showing columns with missing values in the DataFrame.
    
    Parameters:
    - df (DataFrame): Input DataFrame
    
    Returns:
    - None
    """
    # Calculate the count of missing values in each column
    missing_values_count = df.isnull().sum()
    
    # Filter columns with missing values
    missing_columns = missing_values_count[missing_values_count > 0]
    
    if not missing_columns.empty:
        # Plotting
        plt.figure(figsize=(10, 6))
        missing_columns.plot(kind='bar', color='skyblue')
        plt.title('Columns with Missing Values')
        plt.xlabel('Columns')
        plt.ylabel('Number of Missing Values')
        plt.xticks(rotation=0, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("No missing values found in the DataFrame.")

# Test the function
if __name__ == "__main__":
    # Assuming df is your DataFrame
    df = pd.DataFrame({
        'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, None, 5],
        'C': [1, 2, 3, 4, 5]
    })
    
    plot_missing_values(df)

