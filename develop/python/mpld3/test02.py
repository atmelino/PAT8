import matplotlib.pyplot as plt, mpld3
fig = plt.figure()
fid=plt.plot([3,1,4,1,5])

mpld3.save_html(fig,"test.html")
mpld3.fig_to_html(fig,template_type="simple")
#mpld3.disable_notebook()
mpld3.show()
