# 2023-11-03T11:50:35.700+0000 [JettyHttpPool-197] gid:65449b33a064331ae2689533 INFO  backup.jobs.65449b33a064331ae2689533.config-configRS-65449d79a064331ae268a0ea [WTAgentTargetingSvc.java:updateWTCheckpointTarget:402] - Updating checkpoint targeting selection from TargetingSelection{_sessionKey='65449b9000116c9138d6d287', _hostnameAndPort='ip-172-31-36-151.eu-west-1.compute.internal:27018', _info=Info{_numCores=1, _memSizeMB=970}, _tailOwnerSince='null'} to TargetingSelection{_sessionKey='6544de7be063c1b7ce5cd53f', _hostnameAndPort='ip-172-31-36-151.eu-west-1.compute.internal:27018', _info=Info{_numCores=1, _memSizeMB=970}, _tailOwnerSince='null'}
# 2023-11-03T11:50:35.699+0000 [JettyHttpPool-197] gid:65449b33a064331ae2689533 DEBUG com.xgen.svc.brs.slurp.svc.WTAgentTargetingSvc [WTAgentTargetingSvc.java:getWTAgentTargetedForCheckpoint:717] - Ideal backup module is available for WT checkpointing: ip-172-31-36-151.eu-west-1.compute.internal:27018 Sorted candidate sessions: [AgentSessionSortWrapper{agentAudit=BackupAgentAudit{Id: 65449c7801422209e8b5fbef, GroupId: 65449b33a064331ae2689533, Hostname: ip-172-31-36-151.eu-west-1.compute.internal, Version: 12.0.23.7711}, canonicalHostname='ip-172-31-36-151.eu-west-1.compute.internal:27018', member=Member{_id=0, _host='ip-172-31-36-151.eu-west-1.compute.internal:27018', _hostId='2047a30f4a0cae036b980c49a3e87a93', _arbiterOnly=false, _buildIndexes=true, _hidden=false, _priority=1.0, _tags={}, _slaveDelaySec=0, _votes=1, _state=PRIMARY, _errorMessage='null', _optimeDate=Fri Nov 03 11:48:13 GMT 2023 (1699012093000), _tooStale=false}, host=ip-172-31-36-151.eu-west-1.compute.internal:27018}], lastSnapshotHostnameAndPort null, currentSnapshottingHostnameAndPort null, userTargetedHostnameAndPort: null
# 2021-03-09T13:45:39.071+0000 [JettyHttpPool-404] gid:5696632ff1c01bc1953f4dee INFO  backup.jobs.5696632ff1c01bc1953f4dee.ClerkTestrs [WTCheckpointTargetedConfigCallSvc.java.shouldForceFullIncrementalSnapshot:918] - fullIncrementalDayOfWeek not set; not forcing full incremental snapshot.
#2021-06-15T07:36:24.764+0000 [JettyHttpPool-127] gid:60c7658302534d25555243c6 DEBUG backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointTargetedConfigCallSvc.java.shouldForceFullIncrementalSnapshot:924] - lastFullIncrementalTimestamp is empty; should take full snapshot now.
#2021-07-17T00:04:21.111+0000 [JettyHttpPool-333] gid:60b60fa642da8716b7368572 INFO  backup.jobs.60b60fa642da8716b7368572.DCRT [WTCheckpointTargetedConfigCallSvc.java.shouldForceFullIncrementalSnapshot:931] - Forcing full incremental snapshot: because today is SATURDAY and last full incremental snapshot was 2021-07-10T00:02:12Z.
#2021-08-10T05:31:33.249+0000 [JettyHttpPool-405] gid:5984e55dbcc7062ebafc960a INFO  backup.jobs.5984e55dbcc7062ebafc960a.rs-pd-person01 [WTCheckpointTargetedConfigCallSvc.java.shouldForceFullIncrementalSnapshot:940] - Forcing full incremental snapshot: Last full incremental snapshot is too long ago (2021-07-29T04:17:36Z).
#2021-06-15T07:39:26.323+0000 [JettyHttpPool-205] gid:60c7658302534d25555243c6 INFO  com.xgen.svc.brs.slurp.res.WTCheckpointResource [WTCheckpointResource.java.description:295] - Description request from 60c7658302534d25555243c6/rs/75802d9c-5431-4792-bfc9-58a2024d5929 from ah=n2.omansible.int av=10.14.24.6508
#2021-06-15T07:40:25.468+0000 [JettyHttpPool-170] gid:60c7658302534d25555243c6 INFO  backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointResource.java.description:483] - Successful post /description for groupId: 60c7658302534d25555243c6, rsId: rs
#2021-06-14T18:08:26.123+0000 [JettyHttpPool-208] gid:60c7658302534d25555243c6 DEBUG backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointTargetedConfigCallSvc.java.getNext:1137] - Excluding replica set from checkpointing.next: BackupStatus lastStableRecoveryTimestamp (TS time:Mon Jun 14 18:06:39 GMT 2021 inc:1) is before the next snapshot time (TS time:Mon Jun 14 18:08:21 GMT 2021 inc:1)
#2021-06-14T18:12:23.321+0000 [JettyHttpPool-208] gid:60c7658302534d25555243c6 INFO com.xgen.svc.brs.slurp.res.WTCheckpointResource [WTCheckpointResource.java.fileList:696] - File List request 0 from 60c7658302534d25555243c6/rs/2350d4dc-01db-48ae-834d-a73e126cd73a extend=false empty=false for with 34 entries from ah=n2.omansible.int av=10.14.24.6508
#2021-06-14T18:12:23.342+0000 [JettyHttpPool-208] gid:60c7658302534d25555243c6 INFO  com.xgen.svc.brs.slurp.res.WTCheckpointResource [WTCheckpointResource.java.fileList:787] - Saved file list from 60c7658302534d25555243c6/rs/2350d4dc-01db-48ae-834d-a73e126cd73a with 34 entries
#2021-06-15T07:40:25.531+0000 [JettyHttpPool-170] gid:60c7658302534d25555243c6 INFO  com.xgen.svc.brs.slurp.res.WTCheckpointResource [WTCheckpointResource.java.fileList:773] - Finalized file list for 60c7658302534d25555243c6/rs/574fb4cc-87ea-45c2-9afd-6863433741c6 with extend=false
#2021-06-15T07:40:25.530+0000 [JettyHttpPool-170] gid:60c7658302534d25555243c6 INFO  backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointScheduleSvc.java.updateCursorExtendTsForSnapshot:288] - Backup cursor extend updated for a snapshot for 60c7658302534d25555243c6/rs backupId: 574fb4cc-87ea-45c2-9afd-6863433741c6 extendedTS: TS time:Tue Jun 15 07:39:53 GMT 2021 inc:1

# 2021-06-15T07:41:27.965+0000 [JettyHttpPool-205] gid:60c7658302534d25555243c6 INFO  backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointBackupSvc.java.saveBlockFilesForAllFileLists:1233] - Finished analyzing files. Snapshot: Snapshot: 60c7658302534d25555243c6/rs @ 1623742793000, Regular Files Left: 35, Files to Archive Left: 0 , Archive Files Left: 0.
# 2021-06-15T07:41:28.051+0000 [JettyHttpPool-205] gid:60c7658302534d25555243c6 INFO  backup.jobs.60c7658302534d25555243c6.rs [WTCheckpointBackupSvc.java.saveBlockFilesForAllFileLists:1297] - Saving block files complete for 35 files.


#2023-11-03T07:53:29.546+0000 [JettyHttpPool-305] gid:65449b33a064331ae2689533 INFO  com.xgen.svc.brs.slurp.res.AgentLogResource [AgentLogResource.java:handleLog:87] - 4.2 Snapshot progress: agent.wtsnapshot.myShard_1.1698995718 Snapshot progress: read 167772160 bytes total. (Last: 87091.86 kB/s. Cumulative: 87091.86 kB/s.) Exiting. ip-172-31-36-151.eu-west-1.compute.internal

import os
import re
import csv
import argparse
from pprint import pprint
from report_print import print_backup_report
from datetime import datetime
from collections import namedtuple

## The header of the sharded backup
wtc_clustershot_started_shards = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) INFO .+ Wtc clustershot started for groupId: (?P=gid), clusterId: (?P<clusterid>.+?), topology:"
building_status_map = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) DEBUG .+?Building status map$"
ideal_backup_module = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+ - Ideal backup module is available for WT checkpointing"
updating_checkpoint_targeting = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? backup.jobs.+?\.(?P<replica>(.+?)) \[.+?\] - Updating checkpoint targeting selection from"
full_incremental_day_of_week = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - fullIncrementalDayOfWeek not set"
supports_incremental_backup = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) INFO  backup.jobs.(?P=gid).(?P<replica>.+?) .+supports incremental backup$"
forcing_full_incremental1 = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Forcing full incremental snapshot: because today is SATURDAY"
forcing_full_incremental2 = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Forcing full incremental snapshot: Last full incremental snapshot is too long ago"
description_request_from = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Description request from (?P=gid)\/(?P<replica>\w+?)\/"
successful_post = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?Successful post /description for groupId: (?P=gid), rsId: (?P<replica>(.+?))$"
excluding_replica_set = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?\.(?P=gid)\.(?P<replica>.+?) .+? - Excluding replica set from checkpointing.next: BackupStatus lastStableRecoveryTimestamp "
file_list_request_0 = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - File List request 0 from (?P=gid)\/(?P<replica>.+?)\/"
saved_file_list_from = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Saved file list from (?P=gid)\/(?P<replica>.+?)\/"
finalized_file_list_for = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Finalized file list for (?P=gid)\/(?P<replica>.+?)\/"
backup_cursor_extend_updated = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?  backup.jobs.(?P=gid)\.(?P<replica>.+?) .+? - Backup cursor extend updated for a snapshot for (?P=gid)\/(?P=replica) backupId: (?P<bakupID>.+?) "
finished_analyzing_files = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?  backup.jobs.(?P=gid)\.(?P<replica>.+?) .+? - Finished analyzing files. Snapshot"
#fs_analiseinf_files = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[(?P<thread>.+?)\] gid:(?P<gid>.+?) (?P<log_level>.+?)  (backup.jobs.+?)\.(?P<replica>(.+?)) \[(?P<class_method>.+?)\] - (?P<message>.+ Regular Files Left: (?P<numFiles>\d+?)),"
updating_snapshot_with = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[(?P<thread>.+?)\] gid:(?P<gid>.+?) (?P<log_level>.+?) (backup.jobs.+?)\.(?P<replica>(.+?)) \[(?P<class_method>.+?)\] - Updating Snapshot with (?P<numFiles>\d+) fileId references.$"
saving_block_files_complete = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[(?P<thread>.+?)\] gid:(?P<gid>.+?) (?P<log_level>.+?) (backup.jobs.+?)\.(?P<replica>(.+?)) \[(?P<class_method>.+?)\] - Saving block files complete for (?P<numFiles>\d+) files.$"
completing_snapshot = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?  backup.jobs.(?P=gid)\.(?P<replica>.+?) .+? - Snapshot (?P<backupID>.+?) completing snapshot.$"
successfully_released_lock = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?  backup.jobs.(?P=gid)\.(?P<replica>.+?) .+? - Successfully released lock for Snapshot (?P<backupID>.+?). Snapshot is complete"
snapshot_progress = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) INFO .+? agent.wtsnapshot\.(?P<replica>\w+?)\.\w+? Snapshot progress: read \d+? bytes total"
loading_backupdeployment = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) DEBUG .+?Loading BackupDeployment$"
## STOP EVENTS PATTERNS
error_backup_jobd = "^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}).+ backup\.jobs\.(?P<gid>\w+)\.(?P<replica>\w+).+$"

##BACKUP SPEAD PATTERN
backup_params = "^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}).+ .+\.(?P<gid>\w+)\.(?P<replica>\w+).+maxWorkers=(?P<maxWorkes>\w+) maxNumUnitOfWorkBlocks=(?P<maxNumUnitOfWorkBlocks>\w+).+bandwidth=(?P<bandwidth>\w+)"
#TBD
cumulative = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) INFO .+ Snapshot progress: agent.wtsnapshot\.(?P<replica>.+)\.(\d*) Snapshot progress: read.+Cumulative: ([\d|\.]+.+) kB\/s\.\)"

patterns = [wtc_clustershot_started_shards,
            #building_status_map, #NO cluster_ID inside
            #loading_backupdeployment, #NO cluster_ID inside
            #ideal_backup_module , #NO cluster_ID inside
            updating_checkpoint_targeting,#+
            full_incremental_day_of_week, 
            supports_incremental_backup, #+
            forcing_full_incremental1,
            forcing_full_incremental2,
            excluding_replica_set,#+
            description_request_from,#+
            successful_post,#+
            file_list_request_0, #+
            saved_file_list_from, #+
            backup_cursor_extend_updated,
            finalized_file_list_for,#+
            finished_analyzing_files, #+
 #           fs_analiseinf_files, not needed?
            updating_snapshot_with,#+
            saving_block_files_complete,#+
            completing_snapshot,#+
            snapshot_progress #+
            ]


#start_end_map_events = [
#     wtc_clustershot_started_shards,
#     updating_checkpoint_targeting,
#     full_incremental_day_of_week,
#     supports_incremental_backup,
#     forcing_full_incremental1,
#     forcing_full_incremental2,
#     description_request_from,
#     successful_post,
#     successfully_released_lock,
#     excluding_replica_set
# ]

def shard_backup_header_parser(input_string):
    #input_string = "[WtShardedClusterTopology.Shard(_rsId=myShard_1, _shardName=myShard_1, _aborted=false, _descriptionId=null), WtShardedClusterTopology.Shard(_rsId=myShard_0, _shardName=myShard_0, _aborted=false, _descriptionId=null)], _configs=[WtShardedClusterTopology.CSRS(_rsId=config-configRS-65449d79a064331ae268a0ea, _csrsId=configRS, _hostId=null, _aborted=false, _descriptionId=null)], _scheduledTimestamp=TS time:Fri Nov 03 07:15:18 GMT 2023 inc:1, _aborting=false)"
    
    # Regular expression to match entities with _rsId and _shardName
    pattern = re.compile(r"_rsId=([^,]+), _shardName=([^,]+)")

    # Find all matches
    matches = pattern.findall(input_string)

    # Extract values for _rsId and _shardName
    for match in matches:
        shard_id, shard_name = match


    # Regular expression to match the last entity with _rsId and _csrsId
    csrs_entity_pattern = re.compile(r"_rsId=([^,]+), _csrsId=([^,]+)")

    # Find the last match
    csrs_entity_match = csrs_entity_pattern.search(input_string)

        
    rs = []
    # Output the results
    for match in matches:
        shard_id, shard_name = match
        rs.append ((shard_id, shard_name, ))

    # Extract values for _rsId and _csrsId for the last entity
    if csrs_entity_match:
        shard_id, shard_name = csrs_entity_match.groups()
        rs.append ((shard_id, shard_name))
 
    return rs
    
def read_errors(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # skip lines that start with ‘#’
        return [item for sublist in reader if not sublist[0].startswith('#') for item in sublist]

def get_var_names(var_list):
    globals_dict = globals()
    var_names = []

    for var in var_list:
        for var_name in globals_dict:
            if globals_dict[var_name] is var:
                var_names.append(var_name)
                break

    return var_names


# def scan_all_events(patterns):
#     patterns_names = get_var_names(patterns)
#     big_patterns = list(zip(patterns, patterns_names))

#     stop_backup_errors ={}
#     # Create a dictionary where all values are zero
#     patterns_counters = {key:[0,[]] for key in patterns_names} 

#     parser = argparse.ArgumentParser(description="Parsing log -file")
#     parser.add_argument("file_name", help="the name of the log-file")

#     args = parser.parse_args()
#     line_number = 0

#     with open(args.file_name, 'r') as log_file:
#         # Read all available backup errors
#         script_directory = os.path.dirname(__file__)
#         file_path = os.path.join(script_directory, 'backup_errors.csv')
#         errors = read_errors(file_path)
#         for line in log_file:
#             line_number += 1 
#             for pattern in big_patterns:
#                 match = re.search(pattern[0], line)
#                 if match:

#                     patterns_counters[pattern[1]][0] += 1


#                     try:
#                         replica_value = match.group("replica")
#                     except:
#                         replica_value = ""
#                          # TODO Not good need to change
#                         if pattern[1] == "wtc_clustershot_started_shards":  
#                             replica_value = shard_backup_header_parser(line)

#                     # Get Project ID
#                     gid_values = match.group("gid")

#                     # Get RS ID
#                     patterns_counters[pattern[1]][1].append([line_number,replica_value])

#             for error in errors:
#                 if error in line:
#                     #print(error,line_number,line)
#                     if error in stop_backup_errors:
#                         stop_backup_errors[error].append(line_number)
#                     else:
#                         stop_backup_errors[error] = [line_number]
#             # if line_number > 200000:
#             #     break
#     return patterns_counters ,stop_backup_errors


# Define a namedtuple to hold information about each cluster
ClusterInfo = namedtuple("ClusterInfo", ["group_id", "cluster_id", "timestamp","backup_global_events","shards"])
ShardInfo = namedtuple("ShardInfo", ["shard_id", "shard_name", "backup_events", "detected_errors"])

def scan_all_events_new(patterns,output_file):
    backupsInfo = []
    patterns_names = get_var_names(patterns)
    big_patterns = list(zip(patterns, patterns_names))

    # parser = argparse.ArgumentParser(description="Parsing log -file")
    # parser.add_argument("file_name", help="the name of the log-file")

    # args = parser.parse_args()
    line_number = 0
#   with open(args.file_name, 'r') as log_file:
    with open(output_file, 'r') as log_file:
        # Read all available backup errors
        script_directory = os.path.dirname(__file__)
        file_path = os.path.join(script_directory, 'backup_errors.csv')
        errors = read_errors(file_path)

        for line in log_file:
            line_number += 1 
            for pattern in big_patterns:
                match = re.search(pattern[0], line)
                if match:
                    #print(pattern[1])
                    # Get Project ID
                    gid_values = match.group("gid")
                    timestamp_str = match.group("timestamp")
                    timestamp_value = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%f%z')
                    rs_id = None
                    #print("!")
                    try:
                        rs_id = match.group("replica")
                    except:
      
                         # TODO Not good need to change
                         # handle the initial start backup event per cluster/project
                         # Fetch the sharding info

                        if pattern[1] == "wtc_clustershot_started_shards":  
                            clusterid = match.group("clusterid")
                            replica_value = []
                            replica_value = shard_backup_header_parser(line)
                            
                            backup = ClusterInfo(gid_values,clusterid, timestamp_value, [],[])
                            backup.backup_global_events.append([line_number,timestamp_value,pattern[1]])
                            for rs in replica_value:
                                backup.shards.append(ShardInfo(rs[0],rs[1],[],[]))    

                            backupsInfo.append(backup)

                    # TODO handle the case when we get the backup event with out handle the backup initial start event before this
                    # could be happen when we have partial data in the mmso log file    

                    # Add event to exiting backup timeline
                    # TODO change 
                    if rs_id is not None:
                        for backup in reversed(backupsInfo):
                            if backup.group_id == gid_values and backup.timestamp < timestamp_value :
                                #print("!!",rs_id,pattern[1])
                                if rs_id == backup.cluster_id:
                                    #print("!!!")
                                    backup.backup_global_events.append([line_number,timestamp_value,pattern[1]])
                                else:
                                    for shard in backup.shards:
                                        if shard.shard_id == rs_id:
                                            #print("!!!!")
                                            # TODO add time stamp instaed of line
                                            shard.backup_events.append([line_number,timestamp_value,pattern[1]])
                                
                            #we have found the backup candidate.Exit from the loop
                            break

            # TODO refactor extract
            ## Add error info
            for error in errors:  
                if error in line:
                    match = re.search(error_backup_jobd, line)
                    if match:
                        # Get Project ID
                        # TODO refactor extract the function of parsing
                        gid_values = match.group("gid")
                        rs_id = match.group("replica")
                        timestamp_str = match.group("timestamp")
                        timestamp_value = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%f%z')

                    for backup in reversed(backupsInfo):
                        if backup.group_id == gid_values and backup.timestamp < timestamp_value:
                            for shard in backup.shards:
                                # TODo it is not shard id it is cluster id
                                if shard.shard_id == rs_id:
                                    # TODO add time stamp instaed of line
                                    #print(line_number,timestamp_value)
                                    shard.detected_errors.append([line_number, timestamp_value])
                            #Exit from the loop
                            break
    return backupsInfo

# def check_stop(patterns ,stop_backup_errors):
#     # Find the start pattern
#     first_key = next(iter(patterns))
#     patterns_counters_first = patterns[first_key]
#     patterns_counters_lines  = [item[0] for item in patterns_counters_first[1]]

#     #Find the Finich pattren
#     stop_backup_errors_lines = [num for sublist in stop_backup_errors.values() for num in sublist]
#     stop_backup_errors_lines_sorted = sorted(stop_backup_errors_lines)

#     for i in range(len(patterns_counters_lines) - 1):
#         for error in stop_backup_errors_lines_sorted:
#             if patterns_counters_lines[i] < error < patterns_counters_lines[i + 1]:
#                 print(f"Start[{patterns_counters_lines[i]}] => STOP EVENT[{error}]" )
#                 break
#     print(f"Start[{patterns_counters_lines[-1]}] - No errors found")

import os
import gzip
from datetime import datetime

def concatenate_logs(directory):
  """
  This function scans a directory for log files, sorts them by modification date in descending order,
  unzips gzip compressed files, and concatenates their content into a single output file.

  Args:
      directory (str): Path to the directory containing log files.

  Returns:
      str: Path to the concatenated output file (mms0.log.concat), or None if no files found.
  """

  # Initialize empty list to store file paths
  log_files = []

  # Iterate through files in the directory
  for filename in os.listdir(directory):
    if filename.startswith("mms0") and (filename.endswith(".log") or filename.endswith(".log.gz")):
      # Construct full file path
      filepath = os.path.join(directory, filename)
      # Get modification time
      modification_time = os.path.getmtime(filepath)
      log_files.append((filepath, modification_time))

#   # Sort files by modification time in descending order
#   log_files.sort(key=lambda x: x[1], reverse=True)

  # Sort files by filename in ascending order
  log_files.sort()
#   for item in log_files:
#     print(item)

  # Check if any files were found
  if not log_files:
    print("No log files found in the directory.")
    return None

  # Open output file for writing in append mode
  with open(os.path.join(directory, "mms0.log.concat"), "a") as outfile:
    for filepath, _ in log_files:
      # Handle uncompressed files
      if filepath.endswith(".log"):
        with open(filepath, "r") as infile:
          outfile.write(infile.read())

      # Handle gzipped files
      elif filepath.endswith(".log.gz"):
        with gzip.open(filepath, "rb") as infile:
          outfile.write(infile.read().decode())  # Decode for text processing

  # Return path to the concatenated file
  return os.path.join(directory, "mms0.log.concat")

# Example usage
# directory = "/path/to/your/log/directory"
# output_file = concatenate_logs(directory)
# if output_file:
#   print(f"Concatenated logs into: {output_file}")

def log_scaner(output_file):
    global start_end_map_events
    global patterns

    lala = scan_all_events_new(patterns,output_file)
    print(lala)
    print_backup_report(lala)

def main():
    global start_end_map_events
    global patterns


    parser = argparse.ArgumentParser(description="Parsing log -directory")
    parser.add_argument("directory_name", help="the name of the log-file")

    args = parser.parse_args()
    #args.directory_name
    # directory = "/Users/gregory.vinopal/Downloads/iapp6918.randolph.ms.com/5/"
    output_file = concatenate_logs(args.directory_name)
    if output_file:
        print(f"Concatenated logs into: {output_file}")
    lala = scan_all_events_new(patterns,output_file)
    print_backup_report(lala)

if __name__ == "__main__":
    main()


#/Users/gregory.vinopal/tmp/code/backup_grep/.venv/bin/python /Users/gregory.vinopal/tmp/code/backup_grep/log_map/backup_log_map.py ./logs/mms0.log