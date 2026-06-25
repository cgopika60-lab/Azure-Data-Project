#Azure Data Engineering Project


This project demonstrates an end-to-end Azure Data Engineering pipeline built using Azure Data Lake Storage Gen2 (ADLS), Azure Databricks, PySpark, Delta Lake, and Power BI.                                      
The pipeline extracts Formula 1 driver data from the OpenF1 API, stores the raw data in Azure Data Lake Storage, processes and transforms the data using Databricks and PySpark, stores the processed data in Delta Lake format, and visualizes insights through Power BI dashboards.

__________________________________________________________________________________________________________________________________________________________________________________
##Technologies Used

Azure Data Lake Storage Gen2 (ADLS)           
Azure Databricks            
PySpark          
Delta Lake       
OpenF1 API       
Power BI        
Python          
Pandas        

_________________________________________________________________________________________________________________________________________________________________________________

##Architecture

OpenF1 API →  ADLS Raw Layer →  Azure Databricks (PySpark) →  Delta Lake (Ingested Layer) →  Transformation Layer →  Analysis Layer →  Power BI Dashboard

__________________________________________________________________________________________________________________________________________________________________________________

##Project Workflow

1. Data Ingestion
Extracted driver data from OpenF1 API.
Loaded data into Azure Data Lake Storage Raw Layer.
Converted JSON data into Spark DataFrame.                                                      
2. Data Storage
Stored raw data in ADLS Raw Layer.
Stored processed data in Delta Lake format within the Ingested Layer.                                       
3. Data Transformation
Cleaned null values.
Applied transformations using PySpark.
Stored transformed data in the presentation layer.                                          
4. Data Analysis
Team-wise driver distribution.
Driver nationality analysis.
Driver and team insights.                                      
5. Visualization
Built Power BI dashboard using Delta Lake data.

__________________________________________________________________________________________________________________________________________________________________________________

##Key Features

API Data Ingestion                            
Azure Data Lake Integration                      
Databricks-based Data Processing                       
Delta Lake Storage                   
Data Analysis using PySpark                   
Interactive Power BI Dashboard            

___________________________________________________________________________________________________________________________________________________________________________________

##Project Structure

Azure-Data-Engineering-Project/          
├──                                         
- data_ingestion.py                           
├──                                
- data_transformation.py                       
├──                                    
- data_analysis.py                                       
├── README.md                                
├── .gitignore                              
└── screenshots/

_______________________________________________________________________________________________________________________________________________________________________________________

##Security Note

Azure Storage Account keys, access credentials, and secrets have been removed from the source code for security purposes.                         

_______________________________________________________________________________________________________________________________________________________________________________________

##Future Enhancements

Azure Data Factory (ADF) pipeline automation                                    
Incremental data ingestion                                          
Automated scheduling and monitoring                                       

_______________________________________________________________________________________________________________________________________________________________________________________

##Author

Gopika C
