import shapefile  # pip install pyshp
import matplotlib.pyplot as plt
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

# def create_intersection(shapefile_path1, shapefile_path2, output_path):
#     # Read the shapefiles
#     sf1 = shapefile.Reader(shapefile_path1)
#     sf2 = shapefile.Reader(shapefile_path2)
    
#     # Extract shapes
#     shapes1 = [shape(record.shape.__geo_interface__) for record in sf1.iterShapeRecords()]
#     shapes2 = [shape(record.shape.__geo_interface__) for record in sf2.iterShapeRecords()]

#     # Find intersections
#     intersections = []
#     for shp1 in shapes1:
#         for shp2 in shapes2:
#             if shp1.intersects(shp2):
#                 intersection = shp1.intersection(shp2)
#                 intersections.append(intersection)
    
#     # Write intersections to a new shapefile
#     with shapefile.Writer(output_path) as writer:
#         writer.field('ID', 'N')
#         for i, inter in enumerate(intersections):
#             writer.shape(mapping(inter))
#             writer.record(i)

# File paths to Hurricane Harvey shapefiles
Harvey_Water = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\HurricaneHarvey_water.shp" 
Urban15 = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Urban_2015.shp" 
Cropland15 = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Cropland_2015.shp" 
# Harvey_Urban_Intersection = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Harvey_Water_Inter_Urban.shp"
# Harvey_Cropland_Intersection = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Harvey_Water_Inter_Cropland.shp"

# Create intersection shapefiles
# create_intersection(Harvey_Water, Urban15, Harvey_Urban_Intersection)
# create_intersection(Harvey_Water, Cropland15, Harvey_Cropland_Intersection)

# Plotting the shapefiles
def plot_shapefile(ax, shapefile_path, color, label=None):
    # Read the shapefile
    sf = shapefile.Reader(shapefile_path)
    
    for shape in sf.shapes():
        # Extract the points
        points = shape.points
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        # Plot the shape
        ax.plot(x, y, color=color, label=label)

# Create plot
fig, ax = plt.subplots(figsize=(10, 8))

# define colors for ease of change
urban_color = "#00008B" # Dark Blue 
cropland_color = "#FFFF00" # Bright Yellow 
floodwater_color = "#00FFFF" # cyan
# Plot each shapefile with different colors
plot_shapefile(ax, Harvey_Water, color=floodwater_color)
plot_shapefile(ax, Urban15, color=urban_color)
plot_shapefile(ax, Cropland15, color=cropland_color)
# plot_shapefile(ax, Harvey_Urban_Intersection, color='cyan')
# plot_shapefile(ax, Harvey_Cropland_Intersection, color='magenta')

# Add legend with labels
handles = [
    plt.Line2D([0], [0], color= floodwater_color, lw=1, label='Harvey Water'),
    plt.Line2D([0], [0], color=urban_color, lw=1, label='2015 Urban Land Coverage'),
    plt.Line2D([0], [0], color=cropland_color, lw=1, label='2015 Cropland Coverage'),
    # plt.Line2D([0], [0], color='cyan', lw=1, label='Harvey Water & Urban Land Intersection'),
    # plt.Line2D([0], [0], color='magenta', lw=1, label='Harvey Water & Cropland Intersection')
]
ax.legend(handles=handles, title="Categories", loc='upper right', frameon=False)

# Add title
ax.set_title("Hurricane Harvey Impact: Water, Urban, and Cropland Coverage")

# Add axes labels
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Add gridlines
ax.grid(True)

# Set background color
fig.patch.set_facecolor('darkgray')
ax.set_facecolor('darkgray')

# set text color
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white') 
ax.title.set_color('white') 

# Set tick color 
ax.tick_params(axis='x', colors='white') 
ax.tick_params(axis='y', colors='white') 

# Set grid color 
ax.grid(color='white')

saveFile = True # False= preview, True = save each preview to overrite the last with same name

if saveFile:  # Save file true
    plt.savefig("Hurricane_Harvey_impact.png")
else:  # Save file false
    # Show the plot
    plt.show()
