import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv("Datasets/wheat.data", index_col=0)


fig = plt.figure()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("area")
ax.set_ylabel("perimeter")
ax.set_zlabel("asymmetry")
ax.scatter(df.area, df.perimeter, df.asymmetry, c="red", marker="o")

fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("width")
ax.set_ylabel("groove")
ax.set_zlabel("length")
ax.scatter(df.width, df.groove, df.length, c="green", marker="o")

plt.show()


