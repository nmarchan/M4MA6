import matplotlib.pyplot as plt #needed for plotting

num = [1, 2, 3, 4, 5]
numbers = list(range(1, 50001)) #lists of numbers

cube3 = [i**3 for i in num]
powers3 = [j**3 for j in numbers] #lists of cubes

print('Plotting first 5 cubic numbers...')
plt.scatter(num, cube3)
plt.title('First 5 Cubic Numbers')
plt.show()

print('Plotting first 5000 cubic numbers...')
while True:     #kept getting random "valueerrors" from within matplotlib
    try:        #put the try-except in to just keep trying until it happens
        plt.scatter(numbers, powers3)
        break
    except ValueError:
        continue

plt.title('First 5000 Cubic Numbers')
plt.show()
