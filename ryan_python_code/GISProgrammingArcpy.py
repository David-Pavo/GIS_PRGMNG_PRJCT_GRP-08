import arcpy

# Define the paths to your shapefiles
shapefile1 = r"C:/Users/ryanz/Downloads/392ProjectShp/TSBeta_water.shp"
shapefile2 = r"C:/Users/ryanz/Downloads/392ProjectShp/Urban_2015.shp"
shapefile3 = r"C:/Users/ryanz/Downloads/392ProjectShp/Cropland_2015.shp"

# Define the path to an existing ArcGIS Pro project (.aprx)
project_path = r"C:/Users/ryanz/OneDrive/Documents/ArcGIS/Projects/TestProject/TestProject.aprx"

# Open the ArcGIS Pro project
aprx = arcpy.mp.ArcGISProject(project_path)

# Get the first map in the project
map_obj = aprx.listMaps()[0]

# Add shapefiles to the map
map_obj.addDataFromPath(shapefile1)
map_obj.addDataFromPath(shapefile2)
map_obj.addDataFromPath(shapefile3)

# Save the project to reflect the changes
aprx.save()

print("Shapefiles added successfully to the map!")

# Clean up resources
del aprx
