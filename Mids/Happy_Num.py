import matplotlib.pyplot as plt

def happy_list(n0):
    happy_list = [n0]
    while True:
        # Next Number = Sum of the digits squared
        next_number = sum(int(digit) ** 2 for digit in str(happy_list[-1]))
        # If number converges to 1 it is happy
        if next_number == 1:
            happy_list.append(next_number)
            return happy_list, True
        # If we get a loop number is unhappy
        elif next_number in happy_list:
            return happy_list, False
        else:
            happy_list.append(next_number)

print("Happy List for 7:", *happy_list(7))
print("Happy List for 17:", *happy_list(17))

def count_happy_numbers(limit):
    happy_count = 0
    for n in range(1, limit + 1):
        i, is_happy = happy_list(n)
        if is_happy:
            happy_count += 1
    happiness_rate = (happy_count / limit) * 100
    return happy_count, happiness_rate

for limit in [100, 1000, 1000000]:
    happy_count, happiness_rate = count_happy_numbers(limit)
    print(f"Under {limit}:")
    print(f"Happy Numbers: {happy_count}")
    print(f"Happiness Rate: {happiness_rate:.2f}%")
    print("---")

def plot_all_lists(limit):
    fig, axs = plt.subplots(nrows=5, ncols=4, figsize=(15, 15), sharex=True, gridspec_kw={'hspace': 0.4, 'wspace': 0.4})
    axs = axs.flatten() #Convert the 2D Array to 1D
    for i, n in enumerate(range(981, limit + 1)):
        if i >= len(axs):
            break
        current_list, is_happy = happy_list(n)
        axs[i].plot(current_list)
        axs[i].set_title(f"{'Happy' if is_happy else 'Unhappy'} List of {n}")
        axs[i].set_ylabel('Value')
        if is_happy:
            axs[i].set_facecolor('lightgreen')  # Green for happy numbers
        else:
            axs[i].set_facecolor('lightcoral')  # Red for unhappy numbers
    for ax in axs[i+1:]:
        ax.axis('off')
    plt.suptitle(f'Happy List', fontsize=14)
    plt.show()

plot_all_lists(1000)