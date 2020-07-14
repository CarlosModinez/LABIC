from matplotlib import pyplot as plt
import csv
import numpy as np

def plot_single_line(csv_file, x_feature, y_feature):
    clothes_data = open(csv_file)
    data = csv.reader(clothes_data, delimiter=',', quotechar='"')
    titles = next(data)

    x_vector = []
    y_vector = []
    column_x = -1
    column_y = -1   

    for index, title in enumerate(titles):
        if title == x_feature:
            column_x = index
        
        elif title == y_feature:
            column_y = index
    
    if column_x == -1 or column_y == -1:
        print("feature not found")
        return  

    for row in data:
        x_vector.append(int(row[column_x]))
        y_vector.append(int(row[column_y]))

    return(titles[column_x], titles[column_y], x_vector, y_vector)


# plot do lucro das vendas
x_label, y_label, x_vector, y_vector = plot_single_line('clothes_data.csv', 'month', 'total_profit')
plt.plot(x_vector, y_vector)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()


# plot de todos os produtos
_, pants_legend, x_pants, y_pants = plot_single_line('clothes_data.csv', 'month', 'pants')
plt.plot(x_pants, y_pants, label = pants_legend) 

_, skirt_legend, x_skirt, y_skirt = plot_single_line('clothes_data.csv', 'month', 'skirt')
plt.plot(x_skirt, y_skirt, label = skirt_legend)

_, coat_legend, x_coat, y_coat = plot_single_line('clothes_data.csv', 'month', 'coat')
plt.plot(x_coat, y_coat, label = coat_legend)

_, jersey_legend, x_jersey, y_jersey = plot_single_line('clothes_data.csv', 'month', 'jersey')
plt.plot(x_jersey, y_jersey, label = jersey_legend)

_, hoodie_legend, x_hoodie, y_hoodie = plot_single_line('clothes_data.csv', 'month', 'hoodie')
plt.plot(x_hoodie, y_hoodie, label = hoodie_legend)

_, skarf_legend, x_scarf, y_scarf = plot_single_line('clothes_data.csv', 'month', 'scarf')
plt.plot(x_scarf, y_scarf, label = skarf_legend)

plt.xlabel('months')
plt.ylabel('products')
plt.legend()
plt.show()


#plot da comparacao entre pants e skirt com grafico de barras
matrix_comparation = [y_pants, y_skirt]   
X = np.arange(len(y_pants))
print(matrix_comparation)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, matrix_comparation[0], color = 'r', width = 0.25)
ax.bar(X + 0.25, matrix_comparation[1], color = 'b', width = 0.25)

plt.ylabel('Units')
plt.title('Units per product')
plt.show()


#Adicional - plot de comparacoes entre produtos
width = 0.55
p1 = plt.bar(x_pants, y_pants, width, label="pants")
p2 = plt.bar(x_pants, y_skirt, width, label="skirt", 
                         bottom=np.array(y_pants))
p3 = plt.bar(x_pants, y_coat, width, label="coat", 
                         bottom=np.array(y_pants)+np.array(y_skirt))    
p4 = plt.bar(x_pants, y_jersey, width, label="jersey", 
                         bottom=np.array(y_pants)+np.array(y_skirt)+np.array(y_coat)) 
p5 = plt.bar(x_pants, y_hoodie, width, label="hoodie", 
                         bottom=np.array(y_pants)+np.array(y_skirt)+np.array(y_coat)+np.array(y_jersey))
p4 = plt.bar(x_pants, y_scarf, width, label="jersey", 
                         bottom=np.array(y_pants)+np.array(y_skirt)+np.array(y_coat)+np.array(y_jersey)+np.array(y_hoodie))
                                 
plt.ylabel('Units')
plt.title('Units per product')
plt.xticks(x_pants, x_pants)
plt.yticks(np.arange(0, 4000, 500))
plt.legend()

plt.show()