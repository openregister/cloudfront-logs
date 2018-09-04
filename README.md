#Processing Cloudfront logs for performance platform and Anonymising for retention.

#Downloading the data
in order to download the data you will need access to the cloudfront logs on AWS and the AWS command line tools setup and install.

Navigate through to the data folder and run:

aws s3 sync s3://cloudfront-logs-register-gov-uk . --exclude ".201[6-7]-" --exclude ".2018-0[1-2]"

substituting the --exclude perameters for your requirements at the time. This will download all of the relevant log files for every register in the time period into the /data folder.
This will take a long time. Once you have confirmed the command is working i would reccomend stoping it (cmd + c) and then running the command with the --quiet flag on the end to suppress terminal output. This will make the logs download faster

#Processing the logs files:

the first thing we need to do is normalise the log data from amazon. Amazon have a habit of adding aditional fields to the logs so if there is a new field this will need updating in both the headers.tsv file and in the headers variable within the script. If I will improve this so only the file needs updating at a later date.

The script will output 1 file for each register into the dataworker_files folder. This will be done once all the log files for a register have been processed. This means that any files in the dataworked_files folder are complete and should the script need restarting those registers can be deleted from the raw data folder.


