ChannelConfigHasInterface = '''<?xml version="1.0" encoding="UTF-8" ?>
    <CycloneDDS>
        <Domain Id="any">
            <General>
                <Interfaces>
                    $__IF_LIST__$
                </Interfaces>
            </General>
            <Discovery>
                <!-- Same-host bus discovery rides unicast 127.0.0.1: every bus
                     process (dds_bind / cdds_bus.xml) carries the same Peer, and
                     multicast SPDP between the SDK's own cyclonedds and the ROS
                     rmw's did not meet on lo (0.10.2 vs 0.10.5, 2026-10-31).
                     Dog discovery stays multicast on the robot NIC. -->
                <Peers>
                    <Peer address="127.0.0.1"/>
                </Peers>
                <!-- default 100s: after we vanish the dog keeps ghost-reader
                     state and keeps uncasting into the dead link for the whole
                     lease -- spanning every flip recovery window. 0.5s purge
                     (announcements go to lease/3 ~ 0.17s). 2026-10-10. -->
                <LeaseDuration>500 ms</LeaseDuration>
            </Discovery>
            <Tracing>
                <Verbosity>config</Verbosity>
            <OutputFile>/tmp/cdds.LOG</OutputFile>
        </Tracing>
        </Domain>
    </CycloneDDS>'''

ChannelConfigAutoDetermine = '''<?xml version="1.0" encoding="UTF-8" ?>
    <CycloneDDS>
        <Domain Id="any">
            <General>
                <Interfaces>
                    <NetworkInterface autodetermine=\"true\" priority=\"default\" multicast=\"default\" />
                </Interfaces>
            </General>
            <Discovery>
                <LeaseDuration>500 ms</LeaseDuration>
            </Discovery>
        </Domain>
    </CycloneDDS>'''
