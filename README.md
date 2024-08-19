Mototrbo
========

Mototrbo ARS, TMS

Known Service Ports
-------------------

```
Not all of these ports are relevant but they should still be documented here. Location, ARS, TMS, and Battery Managment are the most relevant

Protocol    Port (Range)    Used for                            Used where
TCP         23*             Telnet                              Only used during setup/reconfig of routers and switches
TCP         80*             Repeater RDS pages                  Between radio sites (only needed to view repeater RDS page)
UDP         123*            NTP                                 All infrastructure elements.
TCP         443*            RM client login on RM server        Between RM client and server
TCP         5020            MNIS Control                        Between MNIS DG and Device Programmer
TCP         8080*           ESU                                 Between CMSS and network management PC
TCP         8675*           Radio Management                    Between RM Client and Server
TCP         9090*           System Advisor                      Between CMSS and network management PC
UDP         4001            Location                            Between radios and MNIS DG
UDP         4005            ARS                                 Between radios and MNIS DG
UDP         4007            TMS                                 Between radios and MNIS DG
UDP         4012            Battery Management                  Between MNIS Data Gateway and IMPRES Fleet Management Server
UDP         4502            System Advisor                      Between sites and CMSS
UDP         35003           System Advisor                      Between sites and CMSS
UDP         36002           System Advisor                      Between sites and CMSS
UDP         50000           Trunking Controller                 Between sites and CMSS
UDP         50005           Status Agent                        Between sites and CMSS and MNIS VRC
UDP         50015           Registrar                           Between sites; CMSS and dispatch
UDP         50111           Call Monitoring                     Between sites; CMSS and dispatch
UDP         51919           Trunking Controller Intermediary    Between sites; CMSS and dispatch
UDP         58041           IMPRES Fleet Management             Between MNIS DG and sites
UDP         60000 - 65535   Inter/Intrasite traffic             Between sites and CMSS
```
