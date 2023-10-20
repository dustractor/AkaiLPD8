# name=AkaiLPD8
import midi
import transport
import patterns

bank_1_pad_1 = 3
bank_1_pad_2 = 4
bank_1_pad_3 = 5
bank_1_pad_4 = 6
bank_1_pad_5 = 7
bank_1_pad_6 = 8
bank_1_pad_7 = 9
bank_1_pad_8 = 10
bank_2_pad_1 = 11
bank_2_pad_2 = 12
bank_2_pad_3 = 13
bank_2_pad_4 = 14
bank_2_pad_5 = 15
bank_2_pad_6 = 16
bank_2_pad_7 = 17
bank_2_pad_8 = 18

def OnMidiMsg(event):
    event.handled = False
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data2 > 0:
            if event.data1 == bank_1_pad_1:
                print("Stop")
                transport.stop()
                event.handled = True
            if event.data1 == bank_1_pad_2:
                print("Play")
                transport.start()
                event.handled = True
            if event.data1 == bank_1_pad_3:
                print("Record")
                transport.record()
                event.handled = True
            if event.data1 == bank_1_pad_4:
                print("New Pattern")
                newpat = patterns.patternCount() + 1
                patterns.jumpToPattern(newpat)
                event.handled = True
            if event.data1 == bank_1_pad_5:
                print("Toggle Pattern/Song Mode")
                transport.setLoopMode()
                event.handled = True
            if event.data1 == bank_1_pad_6:
                print("Toggle LoopRecord")
                transport.globalTransport(midi.FPT_LoopRecord,113)
                event.handled = True
            if event.data1 == bank_1_pad_7:
                print("Toggle Overdub")
                transport.globalTransport(midi.FPT_Overdub,112)
                event.handled = True
            if event.data1 == bank_1_pad_8:
                print("Toggle WaitForInput")
                transport.globalTransport(midi.FPT_WaitForInput,111)
                event.handled = True
                """
            if event.data1 == bank_2_pad_1:
                event.handled = True
            if event.data1 == bank_2_pad_2:
                event.handled = True
            if event.data1 == bank_2_pad_3:
                event.handled = True
            if event.data1 == bank_2_pad_4:
                event.handled = True
            if event.data1 == bank_2_pad_5:
                event.handled = True
            if event.data1 == bank_2_pad_6:
                event.handled = True
            if event.data1 == bank_2_pad_7:
                event.handled = True
            if event.data1 == bank_2_pad_8:
                event.handled = True

"""

