from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# # Pass the current document you want to search to the collector
# cl = FilteredElementCollector(doc)
# # Filter the collector to only include walls
# cl.OfCategory(BuiltInCategory.OST_Walls)
# # Filter the collector to only include elements that are not types
# cl.WhereElementIsNotElementType()


wall_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

for wall in wall_collector:
    print(wall)    # Prints the element ID of each wall in the project