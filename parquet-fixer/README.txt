- make sure you have downloaded all relevant packages  
  
App Usage  
This code is designed to break down parquet files and output a csv, "cleaned" parquet and an analysis of any columns containing numbers in the form of a tsv file.  
These files are timestamped with the current date.  
The output "cleaned" parquet file has had all nan values replaced with 0  


To Use

Configure Download Folder  
To configure this app to run on your download folder change the user_config.json file  
enter your downlaod folder path in place of "/Users/user.name/Downloads"

 "config":{
        "filepath":"/Users/user.name/Downloads"
    }

run the program, it should show you a list of parquet files in your downloads folder,
type in the search bar to narrow the search or click on a file, if it is successful,
a textbox confirmation will appear, exit out of this text box and click the exit button on the search GUI.
This will finish the program and output your three files in the same directory where the code ran.