import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    data = pd.read_pickle('./data/raw_data.pkl')
    print(data.shape)
    print(data.columns)
    # Change column names
    # data.columns = [
    #     'Q_1', 'Q_2', 'Q_3', 'Q_4', 'Q_5', 'Q_6', 'Q_7', 'Q_8', 'EC'
    # ]
    # # Add an offset of 10% to all the variables
    # data = data * 1.1
    # # Save the data
    # data.to_pickle('./data/raw_data.pkl')
