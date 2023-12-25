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
# Define a function to print the report for each cluster
def print_cluster_report(cluster):

    print(f"\nProject id:{cluster.group_id}")
    print(f"Cluster id:{cluster.cluster_id}")
    print(f"Backup start time: {cluster.timestamp}")

    print("\n\tBackup global events:")
    for event in cluster.backup_global_events:
        print(f"\t\t Line: {event[0]} , Time {event[1]}, Event {event[2]}")

    print("\n\tBackup shards:")
    for shard in cluster.shards:
        print("\n\t\t",colored(f"Shard Name:{shard.shard_name}",'white','on_green'))
        print(colored(f"\t\tShard Id:{shard.rs_id}",'white','on_green'))

        print(colored ("\t\t\tBackup  events:",'white', 'on_magenta'))
        for event in shard.backup_events:
            print(f"\t\t\t\t Line: {event[0]} , Time {event[1]}, Event {event[2]}")

        print(colored("\t\t\tDetected Errors:",'green', 'on_red'))
        for error in shard.detected_errors:
            print(f"\t\t\t\t Line: {error[0]}, Time {error[1]}")

def print_backup_report(clusters):
 # Print the report for each cluster
 for cluster in clusters:
     #print(colored('Hello, World!', 'green', 'on_red'))
     print_cluster_report(cluster)
