import skydelsdx
from skydelsdx.commands import *

class SkydelManager:

    def __init__(self):

        self.sim = None
        self.connected = False
        self.configured = False

    def connectionToSkydelInstance(self):
        self.sim = skydelsdx.RemoteSimulator()
        self.sim.setVerbose(True)
        self.sim.connect()  # Connects to Skydel (defaults to localhost)
        self.connected = True
        print("Connection with Skydel established")

    def createNewConfiguration(self):
        self.sim.call(New(True)) # Create new configuration
        self.sim.call(SetModulationTarget("NoneRT", "", "", True, "uniqueId"))
        self.sim.call(ChangeModulationTargetSignals(0, 12500000, 100000000, "UpperL", "L1CA", -1, False, "uniqueId")) # Minimum required config
        self.sim.arm()
        self.configured = True
        return self.sim

    def sendCommand(self, command):

        if self.connected == False:
            self.connectionToSkydelInstance()

        if self.configured == False:
            self.createNewConfiguration()

        if command == "sim.start()":
            self.sim.start()

        elif command == "sim.stop()":
            self.sim.stop()
