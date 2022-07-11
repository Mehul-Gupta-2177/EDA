from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

def sayhello():
    myPlot = ggplot(economics) + aes(x="date", y="pop") + geom_line()
    myPlot.save("myplot.png", dpi=600)