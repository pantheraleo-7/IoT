import gps


session = gps.gps(mode=gps.WATCH_ENABLE)

for report in session:
    if report["class"] == "TPV":
        print("Latitude:", session.fix.latitude)
        print("Longitude:", session.fix.longitude)
