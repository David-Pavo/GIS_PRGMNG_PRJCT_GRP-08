import sys
sys.path.append(r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3")
import arcpy
print("arcpy is working!")


# Define the paths to Hurricane Harvey shapefiles
Harvey_Water = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\HurricaneHarvey_water.shp" 
Urban15 = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Urban_2015.shp" 
Cropland15 = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\GIS_PGM_Harvey_GEE-stuff-20241122T052703Z-001\GIS_PGM_Harvey_GEE-stuff\Cropland_2015.shp" 

# Define the path to an existing ArcGIS Pro project (.aprx)
project_path = r"C:\Users\thisr\OneDrive - Texas A&M University\2024-Fall\GIS_PROGRAMMING\GIS_PRGMNG_PRJCT_GRP-08\David_Harvey\HH\HH.aprx"

# Open the ArcGIS Pro project
aprx = arcpy.mp.ArcGISProject(project_path)

# Get the first map in the project
map_obj = aprx.listMaps()[0]

# Add shapefiles to the map
map_obj.addDataFromPath(Harvey_Water)
map_obj.addDataFromPath(Urban15)
map_obj.addDataFromPath(Cropland15)

# Save the project to reflect the changes
aprx.save()

print("Shapefiles added successfully to the map!")

# Clean up resources
del aprx
