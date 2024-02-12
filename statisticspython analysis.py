import pandas as pd

def calculate_statistics(data):
    """
    Function to calculate basic statistics on the dataset.
    
    Args:
    - data (DataFrame): Pandas DataFrame containing the dataset.
    
    prints:
    - dict: Dictionary containing mean, median, minimum, maximum of each column.
    """

    """
        >The groupby function from Pandas is used to group the data by the specified column ('Origin' for 1 and 7, 'Cylinders' for 2).
        >We calculate the desired statistics (mean, median, and mode) for the relevant column ('MPG' for 1, 'Horsepower' for 2 and 7) using the agg function.
        >we use a lambda function to find the mode since Pandas mode() function returns a Series with multiple mode values, so we extract the first one.
    """
    mpg_by_origin = data.groupby('Origin')['MPG'].agg(['mean', 'median', lambda x: x.mode().iloc[0]])   
    print("MPG (Miles Per Gallon) by Origin:")
    print(mpg_by_origin)


    horsepower_by_cylinders = data.groupby('Cylinders')['Horsepower'].agg(['mean', 'median', lambda x: x.mode().iloc[0]])
    print("\n\nHorsepower by Cylinders:")
    print(horsepower_by_cylinders)



def main():
    # Load the dataset from CSV
    dataset_file = 'data.csv'
    data = pd.read_csv(dataset_file,sep=';')
    print(data)

    
    """
    # Calculate basic statistics

    # Print the results
    """
    print("Basic Statistics:")
    calculate_statistics(data)


if __name__ == "__main__":
    main()
