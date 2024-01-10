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
    vol_param = wall.LookupParameter('Volumen')    # Get the volume parameter of each wall
    print(vol_param.AsDouble())    # Prints the volume parameter of each wall

    if vol_param:
        total_volume = total_volume + vol_param.AsDouble()    # Add the volume of each wall to the total volume
    
print(total_volume)    # Prints the total volume of all walls in the project