from osgeo import gdal
import numpy as np

# Call function using location of tiff_file to be processed, percentage of slope, and allowed error rate (Default = 0)
# Return -> np array
# Return Failed -> False -> Print ->  Failed to create the TIFF file
def get_possible_CCT_array(tiff_file :str, percent :int, error = 0) -> np:

    # Open Dataset to be processed
    dataset = gdal.Open(tiff_file)

    #Check if Dataset is readable
    if dataset is None:
        print("Failed to open the TIFF file.")
        return
    
    # Process Dataset to Slope
    gdal.DEMProcessing("temp.tif", dataset, "slope", computeEdges = True)

    # Close Main Dataset
    dataset = None

    # Open & Read dataset as an array
    slope_dataset = gdal.Open("temp.tif")
    slope_array = slope_dataset.GetRasterBand(1).ReadAsArray()
    
    # Close Slope Dataset
    slope_dataset = None

    #Slope % conversion
    slope_degree = np.tan(np.radians(percent))*100

    # Define your angle range for trench formation
    degree_max = slope_degree + error # Replace this with your maximum angle
    degree_min = max(0,slope_degree - error)  # Replace this with your minimum angle

    # Identify areas where the angle falls within your specified range
    suggested_areas = np.logical_and(slope_array >= degree_min, slope_array <= degree_max)

    # Return np array 
    return suggested_areas

# Call function using numpy array and output path for storage of tiff file
# Return -> True -> In Directory: <nameoffile>.tif
# Return Failed -> False -> Print ->  Failed to create the TIFF file
def array_to_tiff_file(input_array :np , output_path :str) -> True:

    # Get array shape
    rows, cols = input_array.shape

    # Create new TIFF file
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(output_path, cols, rows, 1, gdal.GDT_Float32)

    if dataset is None:
        print("Failed to create the TIFF file.")
        return False

    # Write array data into the TIFF file
    band = dataset.GetRasterBand(1)
    band.WriteArray(input_array)

    # Close the dataset
    dataset = None

    return True


# Call the function by passing location of DEM file
# Returns -> Tuple of Coordinates
# Returned Failed -> null -> i) Print -> Failed to Open Tiff File
#                            ii) Print -> Failed to Read Geotransform Info
def get_coordinates_from_tiff(tiff_file):

    # Open the TIFF file
    dataset = gdal.Open(tiff_file)

    if dataset is None:
        print("Failed to open the TIFF file.")
        return

    # Get the geotransform information
    geotransform = dataset.GetGeoTransform()

    if geotransform is None:
        print("Failed to get geotransform information.")
        return

    # Extract geotransform parameters
    origin_x = geotransform[0]
    origin_y = geotransform[3]
    pixel_width = geotransform[1]
    pixel_height = geotransform[5]

    # Calculate coordinates
    x = origin_x
    y = origin_y
    width = dataset.RasterXSize
    height = dataset.RasterYSize

    x_end = origin_x + width * pixel_width
    y_end = origin_y + height * pixel_height

    # Close the dataset
    dataset = None

    return (x, y, x_end, y_end)
