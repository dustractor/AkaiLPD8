# name=AkaiLPD8
import midi
import transport
import patterns


# {{{1 CC assignments

bank_1_pad_1 = 3
bank_1_pad_2 = 4
bank_1_pad_3 = 5
bank_1_pad_4 = 6
bank_1_pad_5 = 7
bank_1_pad_6 = 8
bank_1_pad_7 = 9
bank_1_pad_8 = 10

# bank_2_pad_1 = xxx
# bank_2_pad_2 = xxx
# bank_2_pad_3 = xxx
# bank_2_pad_4 = xxx
# bank_2_pad_5 = xxx
# bank_2_pad_6 = xxx
# bank_2_pad_7 = xxx
# bank_2_pad_8 = xxx

# bank_3_pad_1 = xxx
# bank_3_pad_2 = xxx
# bank_3_pad_3 = xxx
# bank_3_pad_4 = xxx
# bank_3_pad_5 = xxx
# bank_3_pad_6 = xxx
# bank_3_pad_7 = xxx
# bank_3_pad_8 = xxx

# bank_4_pad_1 = xxx
# bank_4_pad_2 = xxx
# bank_4_pad_3 = xxx
# bank_4_pad_4 = xxx
# bank_4_pad_5 = xxx
# bank_4_pad_6 = xxx
# bank_4_pad_7 = xxx
# bank_4_pad_8 = xxx

# }}}1

#{{{1 dictionary of events and decorator function
events = dict()

def e(data1):
    def data1event(func):
        events[data1] = func
        return func
    return data1event
# }}}1


# {{{1 bank 1 pads

@e(bank_1_pad_1)
def stop(event):
    print("Stop")
    transport.stop()
    event.handled = True

@e(bank_1_pad_2)
def play(event):
    print("Play")
    transport.start()
    event.handled = True

@e(bank_1_pad_3)
def rec(event):
    print("Record")
    transport.record()
    event.handled = True

@e(bank_1_pad_4)
def new_pattern(event):
    print("New Pattern")
    newpat = patterns.patternCount() + 1
    patterns.jumpToPattern(newpat)
    event.handled = True

@e(bank_1_pad_5)
def songmode(event):
    print("Toggle Pattern/Song Mode")
    transport.setLoopMode()
    event.handled = True

@e(bank_1_pad_6)
def toggle_looprecording(event):
    print("Toggle LoopRecord")
    transport.globalTransport(midi.FPT_LoopRecord,113)
    event.handled = True

@e(bank_1_pad_7)
def toggle_overdub_recording(event):
    print("Toggle Overdub")
    transport.globalTransport(midi.FPT_Overdub,112)
    event.handled = True

@e(bank_1_pad_8)
def toggle_waitforinput(event):
    print("Toggle WaitForInput")
    transport.globalTransport(midi.FPT_WaitForInput,111)
    event.handled = True

# }}}1

# {{{1 bank 2 pads

# @e(bank_2_pad_1)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_2)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_3)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_4)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_5)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_6)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_7)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_2_pad_8)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# }}}1

# {{{1 bank 3 pads

# @e(bank_3_pad_1)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_2)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_3)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_4)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_5)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_6)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_7)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_3_pad_8)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# }}}1

# {{{1 bank 4 pads

# @e(bank_4_pad_1)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_2)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_3)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_4)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_5)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_6)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_7)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# @e(bank_4_pad_8)
# def xxx(event):
#     print("xxx")
#     xxx
#     event.handled = True

# }}}1

# {{{1 Midi Message Handler
def OnMidiMsg(event):
    event.handled = False
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data2 > 0:
            handler = events.get(event.data1,None)
            if handler:
                handler(event)
# }}}1
