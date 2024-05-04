"""This interface defines three main methods: ingest_data, transform_data, and store_data.
ingest_data: This method is responsible for receiving raw data from the data stream.
transform_data: This method takes raw data and transforms it into a format suitable for processing. This might involve data cleaning, normalization, or any other necessary preprocessing steps.
store_data: Once the data is processed, this method stores the processed data, which could be in a database, file system, or any other storage medium."""

class DataStreamInterface:
    def ingest_data(self, data):
        """
        Ingests raw data from external sources.
        
        Args:
            data: Raw data to be ingested.
        """
        pass
    
    def transform_data(self, data):
        """
        Transforms ingested data into a format suitable for storage or analysis.
        
        Args:
            data: Raw or processed data to be transformed.
            
        Returns:
            Transformed data.
        """
        pass
    
    def store_data(self, data):
        """
        Stores transformed data.
        
        Args:
            data: Transformed data to be stored.
        """
        pass
