dictMenu = {'Fruits': {'Apple': 1.99, 'Banana': 0.59, 'Kiwi': 1.1, 'Grapes': 2.99, 'Pear': 2.15},
            'Drinks': {'Water': 1.0, 'Juice': 3.5, 'Coffee': 1.5, 'Soda': 1.5, 'Tea': 1.25},
            'Dessert': {'Ice Cream': 2.99, 'Pie': 2.5, 'Cake': 2.75},
            'Main Dishes': {'Masala Dosa': 4.25, 'Jianbing': 2.88, 'Falafel': 5.15, 'Pizza': 8.5}}

print("----Fruits----")
for i in dictMenu['Fruits']:
    print(f"${dictMenu['Fruits'][f'{i}']:.2f} {i}")

print("----Drinks----")
for j in dictMenu['Drinks']:
    print(f"${dictMenu['Drinks'][f'{j}']:.2f} {j}")

print("----Dessert----")
for k in dictMenu['Dessert']:
    print(f"${dictMenu['Dessert'][f'{k}']:.2f} {k}")

print("----Main Dishes----")
for l in dictMenu['Main Dishes']:
    print(f"${dictMenu['Main Dishes'][f'{l}']:.2f} {l}")