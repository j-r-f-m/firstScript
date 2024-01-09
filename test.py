from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

cl = FilteredElementCollector(doc)
cl.OfCategory(BuiltInCategory.OST_Walls)
cl.WhereElementIsNotElementType()

for el in cl:
    print(el.Name)  # prints the name of each wall in the projectss