import matplotlib.pyplot as plt

labels = ' sin' , 'cos' , 'tan'
data = [ 35, 35, 30] #grafik

figl, axl = plt.subplots () #grafik
axl.pie (data, labels= labels, shadow=True)
plt.show()


