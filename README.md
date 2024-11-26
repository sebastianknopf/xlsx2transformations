# xlsx2transformations
This repository contains a converter for generating transformations for ![onebusaway-transformer-cli](https://github.com/OneBusAway/onebusaway-gtfs-modules/tree/master) based on a XSLX file. The purpose is to specify your desired transformations and their sequence comfortably in Excel and then convert it to the correct transformation syntax.

## Usage
We recommend to run the converter in a virtual environment with dependencies installed locally. To run the converter, use the following command:

```shell
python -m xlsx2transformations -i ./transformations.xlsx -o ./transformations.txt
```

## Input Data Format
The input XLSX file needs to match the following constraints:

- Each worksheet represents a file to which the transformation should be applied. The name of the worksheet specifies the name of the corresponding file.
- Each worksheet needs to have a header row in first line and then the columns with the transformations.
- Each worksheet needs to have a column named 'op' in the first column which is used to specify the transformation type. Possible values are: add, update, remove, retain. This transformation type needs to be specified for each single transformation.
- All other columns in these worksheets contain the columns of the GTFS feed file. _Please note that depending on the transformation type, only the ID column of an entity might be considered._
- The last worksheet contains the sequence for the transformations to be applied to the GTFS feed. The first line contains a header row, the first column contains the transformation type and the second column the file to which the transformation shall be applied. This way it is possible to add, update, remove and finally retain entities.

Please see the example ![transformations.xlsx](transformations.xlsx) file and the generated ![transformations.txt](transformations.txt) file in this repository for reference. See the ![onebusaway-transformer-cli documentation](https://github.com/OneBusAway/onebusaway-gtfs-modules/blob/master/docs/onebusaway-gtfs-transformer-cli.md) for more information about the transformation syntax. 

# License
This project is licensed under the Apache 2.0 license. See ![LICENSE.md](LICENSE.md) for details.