import arcpy
import os 

# Access the currently open ArcGIS Pro project
project = arcpy.mp.ArcGISProject("Current")

# Reference the first map in the project's map list
my_map = project.listMaps("Map")[0]

# Define the root directory for scanning data
workspace = r"D:\Berlin_project"

# Use arcpy.da.Walk to iterate through the workspace and identify Feature Classes
walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    # Loop through each file found in the current directory path
    for filename in filenames:
        # Construct the absolute path to the feature class
        full_path = os.path.join(dirpath, filename)
        
        try:
            # Use arcpy.Describe to retrieve object properties
            desc = arcpy.Describe(full_path)
            
            # Filter for point features specifically
            if desc.shapeType == "Point":
                # Add the feature class to the map from its physical path
                my_map.addDataFromPath(full_path)
                print(f"Successfully added: {filename}")

        except Exception as e:
            # Handle potential errors (e.g., corrupted files or permission issues)
            print(f"Error processing {filename}: {e}")