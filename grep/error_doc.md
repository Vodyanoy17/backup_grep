- _API validation failure on abort_

```
2023-09-18T04:15:43.798+0000 [JettyHttpPool-242] gid:5bc5723cf1ef7c446695ec30 INFO  backup.jobs.5bc5723cf1ef7c446695ec30.AO-SP-GWPCSP_0 [WTCheckpointResource.java:abort:1407] - 
	API validation failure on abort ({"resource":"Backup module session key 64b9032d4937f91da8e8d726 is not targeted.","errorCode":"TARGETING_MISMATCH","version":"1","status":"ERROR"}) allowed to proceed with resource cleanup (backupId: 1d3ff283-5a16-4503-9f73-ffc973cfced7) 
```

>The TARGETING_MISMATCH is typically caused by the WTAgentTargetingSvc function updating the WT checkpoint target host during the backup due to 
a communication issue from the Agent to Ops Manager or the Agent to the mongod process.

- _Cannot find blockfile with primary read preference_

```
2022-03-14T18:11:36.084+0000 [WTDataBlockInserter-21] DEBUG com.xgen.svc.brs.san.BlockFileSvc [BlockFileSvc.java.getUnionFromFileId:725] - Cannot find blockfile with primary read preference. Snapshot: 622f207c2fb0101b37a23aeb BlockFile: 622f207d2fb0101b37a23b1e BlockStore: blockstore TryNum: 1
```
>The above errors indicate that OpsManager is looking for the blocks in S3 blockstore but its unable to find it.
We suspect there could be some issues at the S3 blockstore layer. To further aid the troubleshooting please also help us with the following,

