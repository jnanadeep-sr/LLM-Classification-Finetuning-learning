import pandas as pd
import numpy as np

def append_target_column(df: pd.DataFrame, target_col_name: str = 'target') -> pd.DataFrame:
    """
    Appends a multi-class target column to the DataFrame based on model wins:
        0 -> Tie
        1 -> Model A wins
        2 -> Model B wins
    """
    # Define boolean conditions based on input win columns
    conditions = [
        df['winner_tie'] == 1,
        df['winner_model_a'] == 1,
        df['winner_model_b'] == 1
    ]
    
    # Target label encoding: 0 = Tie, 1 = Model A, 2 = Model B
    choices = [0, 1, 2]
    
    # Create target column
    df[target_col_name] = np.select(conditions, choices, default=0).astype(int)
    
    return df

if __name__ == "__main__":
    # Example usage: Replace 'your_data.csv' with your dataset path
    input_file = "data.csv"
    output_file = "data_with_target.csv"
    
    try:
        # 1. Load Data
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from {input_file}.")
        
        # 2. Append Target Column
        df = append_target_column(df)
        
        # 3. Print Value Counts Verification
        print("\nTarget Distribution:")
        print(df['target'].value_counts().sort_index())
        
        # 4. Save Processed Data
        df.to_csv(output_file, index=False)
        print(f"\nSuccessfully saved updated dataset to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please provide a valid CSV path.")