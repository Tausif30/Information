import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def analyze_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found.")
    letters = [char for char in text if char.isalpha()]
    total_letters = len(letters)

    #Raw counts
    counter = Counter(letters)
    raw_counts = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

    #Frequencies
    frequencies = {char: count/total_letters for char, count in counter.items()}
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))

    return raw_counts, sorted_frequencies, total_letters

def histogram(counts, total_letters, frequencies):
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    bars = plt.bar(counts.keys(), counts.values())

    # Add value labels on top of each bar
    for bar in bars:
        x = bar.get_x() + bar.get_width()/2
        y = bar.get_height()
        plt.text(x, y, f'{int(y)}', ha='center', va='bottom', fontsize = 8)
    plt.title(f'Letter Counts in Text (Total Letters: {total_letters})')
    plt.xlabel('Letters')
    plt.ylabel('Count')
    plt.grid(True, alpha=0.1)

    plt.subplot(122)
    bars = plt.bar(frequencies.keys(), frequencies.values())

    # Add percentage labels on top of each bar
    for bar in bars:
        x = bar.get_x() + bar.get_width()/2
        y = bar.get_height()
        plt.text(x, y, f'{y:.1%}', ha='center', va='bottom')
    plt.title('Letter Frequencies in Text (Relative)')
    plt.xlabel('Letters')
    plt.ylabel('Relative Frequency')

    plt.tight_layout()
    plt.grid(True, alpha=0.1)
    plt.show()

def calculate_entropy(frequencies):
    entropy = -sum(p * np.log2(p) for p in frequencies.values())
    return entropy

# Main analysis
def main(filename='worddic.txt'):
    # Calculate both counts and frequencies
    raw_counts, frequencies, total_letters = analyze_text(filename)

    # Display raw counts
    print("\nLetter Counts (descending order):")
    for letter, count in raw_counts.items():
        print(f"{letter}: {count}")
    print(f"\nTotal Letters: {total_letters}")
    # Display relative frequencies
    print("\nLetter Frequencies (descending order):")
    for letter, freq in frequencies.items():
        print(f"{letter}: {freq:.4f} ({freq:.1%})")

    # Create both histograms
    histogram(raw_counts, total_letters, frequencies)
    # Calculate entropy
    entropy = calculate_entropy(frequencies)
    print(f"\nEntropy per character: {entropy:.4f} bits")

    # Calculate maximum possible entropy (uniform distribution)
    n_symbols = len(frequencies)
    max_entropy = np.log2(n_symbols)
    print(f"Maximum possible entropy: {max_entropy:.4f} bits")
    print(f"Entropy efficiency: {(entropy/max_entropy)*100:.2f}%")

if __name__ == "__main__":
    main()