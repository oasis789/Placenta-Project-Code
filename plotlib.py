import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import scipy.stats

def plot_ncs_earli_histogram(ncs_a,ncs_v,ea_a,ea_v,title,xlabel,scaled=False):
    '''Plot normed histogram with ncs and earli data on same axis'''
    plt.figure()
    scale = lambda x : [s/float(np.mean(x)) for s in x]
    if(scaled):
        data_list = [scale(ncs_a),scale(ncs_v),scale(ea_a),scale(ea_v)]
    else:
        data_list = [ncs_a,ncs_v,ea_a,ea_v]
    colors = ['r','b','g','k']
    (n_list, bins, p_list) = plt.hist(data_list,bins=10,normed=True,color=colors,label=['NCS A','NCS V','EARLI A','EARLI V'])
    for i,data in enumerate(data_list):
        #y = mlab.normpdf(bins,np.mean(data),np.std(data))
        shape,loc,scale = scipy.stats.lognorm.fit(data,floc=0)
        x_fit = np.linspace(min(data),max(data),100)
        #y_fit = scipy.stats.lognorm.pdf(x_fit,shape,loc=loc,scale=scale)
        y_fit = mlab.normpdf(x_fit,np.mean(data), np.std(data))
        plt.plot(x_fit,y_fit,colors[i]+'--',linewidth=1)
    plt.legend(loc='best')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency Density')

def plot_ncs_earli_xy(ncs_a,ncs_ax,ncs_v,ncs_vx,ea_a,ea_ax,ea_v,ea_vx,title,xlabel,ylabel,scaled=False):
    '''Plot ncs and earli data on y axis with some other data on x axis'''
    plt.figure()
    scale = lambda x : [s/float(np.mean(x)) for s in x]
    if scaled:
        plt.plot(scale(ncs_ax),scale(ncs_a),'r.',label='NCS A')
        plt.plot(scale(ncs_vx),scale(ncs_v),'b.',label='NCS V')
        plt.plot(scale(ea_ax),scale(ea_a),'g.',label='EARLI A')
        plt.plot(scale(ea_vx),scale(ea_v),'k.',label='EARLI V')
    else:
        plt.plot(ncs_ax,ncs_a,'r.',label='NCS A')
        plt.plot(ncs_vx,ncs_v,'b.',label='NCS V')
        plt.plot(ea_ax,ea_a,'g.',label='EARLI A')
        plt.plot(ea_vx,ea_v,'k.',label='EARLI V')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='best')

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(min(xdata),max(xdata),100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label)
    return m,c


def show():
    plt.show()