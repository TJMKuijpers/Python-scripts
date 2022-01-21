######################################################################################################
################## Script used to identify outliers based on +/- cells versus total cells   ##########
######################################################################################################

## Input to function:
#   data_frame_object: data frame with the experimental data
#   column_selected_cells: column identifier of the +/- cells within a population of cells
#   column_total_cells: column identifier of the total amount of cells identified in the image

## Output from function:
# returns dataframe with the feature idx, array_selected cells and array_total_cells who are outliers

def identify_outliers_in_data(data_frame_object=None,column_selected_cells=None,column_total_cells=None):
    outliers_in_data=data_frame_object.loc[data_frame_object[column_selected_cells]>data_frame_object[column_total_cells],:]
    return outliers_in_data

