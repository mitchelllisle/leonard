import numpy as np
from scipy.stats import gaussian_kde
import c3p0 as c3
import martha as mh
import altair as alt


class DensityPlot:
    def __init__(self, data, X):
        self.data = data
        self.x = X
        self.y_label = "Density"
        self.distf = None
        self.cumdistf = None

    def read(self):
        return self.__dict__

    def histogram(self, maxbins=10):
        self.data[self.x] = self.data[self.x].map(int)
        self.__data__ = self.data.groupby(self.x).agg({self.x: 'count'}).rename({self.x: 'count'}, axis=1).reset_index()
        self.__data__.sort_values(self.x)
        self.__data__['histogram_y'] = mh.normalise(self.__data__['count'])

        chart = alt.Chart(self.__data__).mark_bar(
            color="cornflowerblue"
        ).encode(
            x=alt.X(self.x, type="quantitative", bin=alt.Bin(maxbins=maxbins), title=self.x),
            y=alt.Y('histogram_y', type="quantitative", stack=None, title=self.y_label)
        )
        return chart

    def gaussianKernel(self):
        plot_color = "gray"
        X = np.array(self.data[self.x].map(int))
        de = gaussian_kde(X)

        self.__data__['gk_interpolated'] = de(np.array(self.__data__[self.x].map(int)))
        self.__data__['gk_interpolated_norm'] = mh.normalise(self.__data__['gk_interpolated'])

        chart = alt.Chart(self.__data__).mark_area(
            fill=plot_color,
            opacity=0.5,
            line={"color": plot_color, "strokeDash": [5, 2]}
        ).encode(
            x=alt.X(self.x, type="quantitative", title=self.x),
            y=alt.Y('gk_interpolated_norm', stack=None, title=self.y_label)
        )
        return chart

    def cumGaussianKernel(self):
        plot_color = "#7E52A8"

        self.__data__['cgk_interpolated'] = np.cumsum(self.__data__['gk_interpolated'])
        self.__data__['cgk_interpolated_norm'] = mh.normalise(self.__data__['cgk_interpolated'])

        chart = alt.Chart(self.__data__).mark_area(
            fill=plot_color,
            opacity=0.5,
            line={"color": plot_color, "strokeDash": [5, 2]}
        ).encode(
            x=alt.X(self.x, type="quantitative", title=self.x),
            y=alt.Y('cgk_interpolated_norm', stack=None, title=self.y_label)
        )
        return chart


def densityPlot(data, x, width=800, height=400):
    plot = DensityPlot(data, x)
    hist = plot.histogram()
    kdf = plot.gaussianKernel()
    cdf = plot.cumGaussianKernel()

    chart = alt.layer(
        hist,
        kdf,
        cdf
    ).properties(
        background="white",
        width=width,
        height=height,
        title='Coefficient of variation'
    ).configure_axis(

    )
    return chart


env = c3.source()
db = env['mlprojects']

data = c3.queryPostgres(
    db['host'],
    db['port'],
    db['username'],
    db['password'],
    "crashes",
    "select * from events limit 1000"
)

densityPlot(data, 'speed_limit')
