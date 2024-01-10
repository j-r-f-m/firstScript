from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# Create collector instance and collect all walls in the project
# 1 Pass the current document you want to search to the collector
# FilteredElementCollector(doc)
# 2 Filter the collector to only include walls
# OfCategory(BuiltInCategory.OST_Walls)
# 3 Filter the collector to only include elements that are not types
# WhereElementIsNotElementType()
wall_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

# initiate variable to store the volume of all walls in the project
total_volume = 0.0

for wall in wall_collector:
    print(wall)    # Prints the element ID of each wall in the project
    
    # When you retrieve a parameter value using the Revit API, the value is given in internal units. 
    # It defaults to american units
    vol_param = wall.LookupParameter('Volumen')    # Get the volume parameter of each wall
    vol_param_cubicmeter = vol_param.AsDouble() * 0.0283168    # Convert the volume parameter to cubic meters
    print(f"Volume of Wall: {vol_param_cubicmeter} m³")    # Prints the volume parameter of each wall

    if vol_param:
        total_volume = total_volume + vol_param.AsDouble()    # Add the volume of each wall to the total volume
 
total_volume_cubicmeter = total_volume * 0.0283168    # Convert the total volume to cubic meters
# Prints the total volume of all walls in the project    
print(f"The total volume of the walls is: {total_volume_cubicmeter} m³")   