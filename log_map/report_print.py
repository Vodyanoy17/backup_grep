#from collections import namedtuple
from termcolor import colored

# Define a namedtuple to hold information about each cluster
#ClusterInfo = namedtuple("ClusterInfo", ["id", "member_shards", "sh0_timframe","backup_events", "successful_events", "detected_errors"])

#ProjectInfo = ("ProjectInfo",["projectName","projectId", "ClusterId","ClusterName"])
# Create sample data for three clusters
'''
[
ClusterInfo(
  group_id='65449b33a064331ae2689533', 
  cluster_id='65449d79a064331ae268a0ea,', 
  timestamp=datetime.datetime(2023, 11, 3, 12, 3, 33, 156000, tzinfo=datetime.timezone.utc), 
  shards=[
    ShardInfo(
      rs_id='myShard_1',
      shard_name='myShard_1', 
      backup_events=[
          [46011, 
          datetime.datetime(2023, 11, 3, 12, 3, 33, 186000, tzinfo=datetime.timezone.utc), 
          'updating_checkpoint_targeting'
          ], 
          [48548, 
          datetime.datetime(2023, 11, 3, 12, 33, 49, 486000, tzinfo=datetime.timezone.utc), 
          'successfully_released_lock']], 
        detected_errors=[]
          ), 
    ShardInfo(
      rs_id='myShard_0', 
      shard_name='myShard_0', 
      backup_events=[
          [46008, 
          datetime.datetime(2023, 11, 3, 12, 3, 33, 176000, tzinfo=datetime.timezone.utc), 
          'updating_checkpoint_targeting'
          ], 
          [49378, 
          datetime.datetime(2023, 11, 3, 12, 34, 26, 235000, tzinfo=datetime.timezone.utc), 
          'successfully_released_lock']
          ], 
        detected_errors=[]
          ), 
    ShardInfo(
      rs_id='config-configRS-65449d79a064331ae268a0ea', 
      shard_name='configRS', 
      backup_events=[
          [46005, 
          datetime.datetime(2023, 11, 3, 12, 3, 33, 166000, tzinfo=datetime.timezone.utc), 
          'updating_checkpoint_targeting'
          ], 
          [48780, 
          datetime.datetime(2023, 11, 3, 12, 33, 50, 492000, tzinfo=datetime.timezone.utc),
          'successfully_released_lock']
          ], 
      detected_errors=[])
    ]
  ),
'''
from datetime import datetime

def print_date(dt):
    # Your time string
    #time_str = "2023-11-03 12:32:40.443000+00:00"

    # Parse the string to a datetime object
    #dt = datetime.fromisoformat(time_str)

    # Format the datetime object to a string up to seconds
    formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")

    return(formatted_time)  # This will print "2023-11-03 12:32:40"


# Define a function to print the report for each cluster
def print_cluster_report(cluster):

    print(f"\nProject id:{cluster.group_id}")
    print(f"Cluster id:{cluster.cluster_id}")
    print(f"Backup start time: {cluster.timestamp}")

    print("\n\tBackup global events:")
    for event in cluster.backup_global_events:
        print(f"\t\t Line: {event[0]} , Time: {print_date(event[1])}, Event: {event[2]}")

    print("\n\tBackup shards:")
    there_is_error = False
    for shard in cluster.shards:
        print("\t\tShard Name:",colored(f"{shard.shard_name}",'white','on_green'))
        print("\t\tShard Id:",colored(f"{shard.shard_id}",'white','on_green'))

        print(colored ("\t\t\tBackup  events:",'white', 'on_magenta'))
        for event in shard.backup_events:
            print(f"\t\t\t\t Line: {event[0]} , Time: {print_date(event[1])}, Event: {event[2]}")

        if len(shard.detected_errors) > 0:
            print(colored("\t\t\tDetected Errors:",'green', 'on_red'))
        for error in shard.detected_errors:
            print(f"\t\t\t\t Line: {error[0]}, Time: {print_date(error[1])}")
            there_is_error = True
    if not(there_is_error):
        print(colored("\t\t\t*** FINISH ***", "green", attrs=["reverse", "blink"]))
    else:
        print(colored("\t\t\t*** FAILED ***", "red", attrs=["reverse", "blink"]))
def print_backup_report(clusters):
 # Print the report for each cluster
 for cluster in clusters:
     #print(colored('Hello, World!', 'green', 'on_red'))
     print_cluster_report(cluster)
