import matplotlib.pyplot as plt



def smoothing(data:list, size_window:int=12)->list:
    x = [] #horizontal axis
    y = [] #smoothed version
    for i in range(0,len(data)-10,size_window):
        segment_mean = sum(data[i:i+size_window])/size_window
        y.append(segment_mean)
        x.append(i)
    return x,y

def plot_smoothed(data:list, size_window:int=12, title:str='Title', x_label:str='X', y_label:str='Y', color:str='blue', save:bool=False, name:str='plot.png'):
    x,y = smoothing(data, size_window)
    plt.plot(x,y, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save:
        plt.savefig(name)
    plt.show()

def plot(data:list, title:str='Title', x_label:str='X', y_label:str='Y', color:str='blue', save:bool=False, name:str='plot.png'):
    plt.plot(data, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save:
        plt.savefig(name)
    plt.show()
