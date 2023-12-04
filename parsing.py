import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import os


def browse_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    root.destroy()
    return file_path


def read_csv(file_path):
    if file_path.endswith('.xlsx'):
        csv_file_path = convert_to_csv(file_path)
        df = pd.read_csv(csv_file_path)
        os.remove(csv_file_path)
    else:
        df = pd.read_csv(file_path)
    return df


def convert_to_csv(file_path):
    csv_file_path = file_path.replace('.xlsx', '.csv')
    wb = pd.read_excel(file_path)
    wb.to_csv(csv_file_path, index=False)
    return csv_file_path


def calculate_statistics(df):
    statistics = {
        "Mean": df.mean(),
        "Median": df.median(),
        "Mode": df.mode().iloc[0],
        "Standard Deviation": df.std(),
        "Variation": df.var()
    }
    return statistics


def generate_plots(df):
    df.hist()
    plt.show()
    df.plot(kind='scatter', x=df.columns[0], y=df.columns[1])
    plt.show()
    df.plot(kind='line')
    plt.show()


def main():
    file_path = browse_file()
    df = read_csv(file_path)
    print("Data:\n", df)
    statistics = calculate_statistics(df)
    print("\nStatistics:\n", statistics)
    generate_plots(df)


if __name__ == "__main__":
    main()