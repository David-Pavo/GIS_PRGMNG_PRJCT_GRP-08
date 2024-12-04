import shapefile  # PyShp
import matplotlib.pyplot as plt

def plot_shapefile(ax, shapefile_path, color, label):
    # Read the shapefile
    sf = shapefile.Reader(shapefile_path)
    
    for shape in sf.shapes():
        # Extract the points
        points = shape.points
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        # Plot the shape
        ax.plot(x, y, color=color, label=label)

# File paths to your shapefiles
shapefile1 = "C:/Users/ryanz/Downloads/392ProjectShp/TSBeta_water.shp"
shapefile2 = "C:/Users/ryanz/Downloads/392ProjectShp/Urban_2015.shp"
shapefile3 = "C:/Users/ryanz/Downloads/392ProjectShp/Cropland_2015.shp"

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot each shapefile with different colors
plot_shapefile(ax, shapefile1, color='blue', label='Shapefile 1')
plot_shapefile(ax, shapefile2, color='green', label='Shapefile 2')
plot_shapefile(ax, shapefile3, color='red', label='Shapefile 3')

# Add title and legend
ax.set_title("Displaying Three Shapefiles")
ax.legend()

# Show the plot
plt.show()
