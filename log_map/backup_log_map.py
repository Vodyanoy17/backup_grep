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

import os
import re
import csv
import argparse
from pprint import pprint

building_status_map = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) DEBUG .+?Building status map$"
ideal_backup_module = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) - Ideal backup module is available for WT checkpointing"
updating_checkpoint_targeting = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? backup.jobs.+?\.(?P<replica>(.+?)) \[.+?\] - Updating checkpoint targeting selection from"
full_incremental_day_of_week = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - fullIncrementalDayOfWeek not set"
last_full_incremental_timestamp = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) DEBUG backup.jobs.(?P=gid)\.(?P<replica>.+?) .+? - lastFullIncrementalTimestamp is empty; should take full snapshot now.$"
forcing_full_incremental1 = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Forcing full incremental snapshot: because today is SATURDAY"
forcing_full_incremental2 = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Forcing full incremental snapshot: Last full incremental snapshot is too long ago"
description_request_from = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+? - Description request from "
uccessful_post = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) .+?Successful post /description for groupId: (?P=gid), rsId: (?P<replica>(.+?))$"
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
snapshot_progress = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) INFO .+?Snapshot progress: read \d+? bytes total"
loading_backupdeployment = "(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{4}) \[.+?\] gid:(?P<gid>.+?) DEBUG .+?Loading BackupDeployment$"
## STOP EVENTS PATTERNS


patterns = [building_status_map,
            loading_backupdeployment,
            ideal_backup_module , 
            updating_checkpoint_targeting,
            full_incremental_day_of_week,
            last_full_incremental_timestamp,
            forcing_full_incremental1,
            forcing_full_incremental2,
#            excluding_replica_set, stop event
            description_request_from,
            uccessful_post,
            file_list_request_0,
            saved_file_list_from,
            backup_cursor_extend_updated,
            finalized_file_list_for,

            finished_analyzing_files,
 #           fs_analiseinf_files, not needed?
            updating_snapshot_with,
            saving_block_files_complete,
            completing_snapshot,
            snapshot_progress
            ]


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

def main():
    
    patterns_names = get_var_names(patterns)
    big_patterns = list(zip(patterns, patterns_names))

    # Create a dictionary where all values are zero
    patterns_counters = {key:[0,[]] for key in patterns_names} 
    stop_backup_errors = {}

    parser = argparse.ArgumentParser(description="Обработка лог-файла")
    parser.add_argument("file_name", help="Имя лог-файла для обработки")

    args = parser.parse_args()
    line_number = 0

    with open(args.file_name, 'r') as log_file:

        # Read all available backup errors
        script_directory = os.path.dirname(__file__)
        file_path = os.path.join(script_directory, 'backup_errors.csv')
        errors = read_errors(file_path)
        for line in log_file:
            line_number += 1 
            for pattern in big_patterns:
                match = re.search(pattern[0], line)
                if match:
                    patterns_counters[pattern[1]][0] += 1
                    patterns_counters[pattern[1]][1].append(line_number)
                for error in errors:
                    if error in line:
                        if error in stop_backup_errors:
                            stop_backup_errors[error].append(line_number)
                        else:
                            stop_backup_errors[str(error)] = [line_number]
            if line_number > 200000:
                break

    pprint (patterns_counters,sort_dicts=False)
    print("STOP EVENTS")
    #pprint (stop_backup_errors,sort_dicts=False)
    print (stop_backup_errors)

if __name__ == "__main__":
    main()