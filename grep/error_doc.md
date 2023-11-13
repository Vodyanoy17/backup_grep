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

- _Retryable error saving data blocks for_ ... _Early EOF_

```
2023-11-01T16:40:22.344+0000 [JettyHttpPool-431] gid:62c9cab0e012f14fca238054 INFO  com.xgen.svc.brs.slurp.res.WTCheckpointResource [WTCheckpointResource.ja
va:dataBlocksV2:737] - Retryable error saving data blocks for 62c9cab0e012f14fca238054/Notification/a883032b-dbb9-4f79-a37e-b77edc126819: 
org.eclipse.jetty.io.EofException: Early EOF
```
>The Early EOF indicates that the Ops Manager Application server reached the end of the POST stream, but not all data was sent as per the size in the header.IPS (Intrusion Prevention System) and WAF (Web Application Firewall) ?