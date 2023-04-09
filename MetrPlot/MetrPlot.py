import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from decimal import Decimal
import numpy as np

class MetrPlot:
    def __init__(self, ms=30, sc_x="log",sc_y="log", name_plot=None, x_name="X", y_name="Y",save_name="Plot",x_s=12,y_s=7):
        self.ms = ms
        self.sc_x = sc_x
        self.sc_y = sc_y
        self.name_plot = name_plot
        self.x_name = x_name
        self.y_name = y_name
        self.save_name = save_name
        self.x_s = x_s
        self.y_s = y_s

    def my_round(self,step,ma,mi,num,str):
        lis = list()
        lis_n=list()
        step = round(step, num)
        start = math.floor(mi / step)
        for i in range(start, start + 18):
            s = i * step
            lis.append(Decimal(s).quantize(Decimal(str)))
            lis_n.append(s)
            if s >= ma:
                break
        return lis,lis_n
    
    def ax(self, array):
        ma=max(array)
        mi=min(array)
        delta=(ma-mi)
        step=delta/6
        if delta<=0.5:
            return self.my_round(step,ma,mi,2,"1.01")
        if delta >0.5 and delta < 5:
            return self.my_round(step, ma, mi, 1, "1.1")
        if delta >=5 and delta <= 15:
            return self.my_round(step, ma, mi, 0, "1")

    def logger(self, arr, sc):
        if sc=="log":
            return np.log10(arr)
        return arr
    
    def pr_axes(self,arr):
        d=0.25*(arr[1]-arr[0])
        return [arr[0]-d,arr[-1]+d]
    
    def format_lab_ax(self, arr,arr_num, sc):
        if sc=="log":
            arr=['10$^{'+i+'}$' for i in arr]
            arr_num=np.power(10,arr_num)
        return arr,arr_num
    
    def main(self, x, y,save=False):
        mpl.rc('font',family='Times New Roman')
        fig, axs = plt.subplots(figsize=(self.x_s, self.y_s))
        plt.xscale(self.sc_x)
        plt.yscale(self.sc_y)
        axs.plot(x, y, ".", color="red", ms=self.ms)

        x_copy=self.logger(x, self.sc_x)
        y_copy=self.logger(y, self.sc_y)

        lis_x, lis_x_num = self.ax(x_copy)
        lis_y, lis_y_num = self.ax(y_copy)

        y_pr=self.pr_axes(lis_y_num)
        x_pr=self.pr_axes(lis_x_num)
        axs.set_ylim(ymin=10**y_pr[0],ymax=10**y_pr[1])
        axs.set_xlim(xmin=10**x_pr[0],xmax=10**x_pr[1])

        lis_x, lis_x_num =self.format_lab_ax(lis_x, lis_x_num, self.sc_x)
        lis_y, lis_y_num =self.format_lab_ax(lis_y, lis_y_num, self.sc_y)

        axs.set_xticks(lis_x_num)
        axs.set_yticks(lis_y_num)

        axs.set_ylabel(self.y_name, fontsize=25, labelpad=8)
        axs.grid(color="black", linewidth=0.7)
        axs.set_xlabel(self.x_name, fontsize=25, labelpad=15)
        axs.set_title(self.name_plot, fontsize=28, loc="center", pad=15)
        axs.tick_params(which='major', length=10, width=2)

        axs.set_xticklabels(lis_x, fontsize=20)
        axs.set_yticklabels(lis_y, fontsize=20)

        axs.get_xaxis().set_tick_params(direction='in')
        axs.get_yaxis().set_tick_params(direction='in')

        if save:
            plt.savefig(self.save_name+'.png', format='png', dpi=300)
            plt.savefig(self.save_name+".svg", format="svg")
        plt.show()
        return 0





        
        



