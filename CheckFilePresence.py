# Petri.autio@wateraid.org 20/09/2013 Events Actions file checker
import os
print "Hello.\nI am checking the latest dates for which events actions files exist."

countJG = 0
countVMG = 0
countArtez = 0

jgFile = ""
vmgFile = ""
artezFile = ""

jgDir = ""
vmgDir = ""
artezDir = ""

jgDate = 0
vmgDate = 0
artezDate = 0

failCount = 0

actiondir = "G:\Database_Team\Regular Imports\Events"

for dirpath, dirnames, filenames in os.walk(actiondir):
    for filename in filenames:
        if filename.upper().startswith(('JG_EVENTSACTIONS')):
            try:
                jgFile = file
                jgEnd = dirpath[-6:]

                if int(jgEnd) > jgDate:
                    jgDate = int(dirpath[-6:])
                    jgDir = dirpath
                    countJG = countJG + 1
            except ValueError:
                countVMG = countVMG + 1
                        
        if filename.upper().startswith(('VMG_EVENTSACTIONS')):
            try:
                vmgFile = file
                vmgEnd = dirpath[-6:]

                if int(vmgEnd) > vmgDate:
                    vmgDate = int(dirpath[-6:])
                    vmgDir = dirpath
                    countVMG = countVMG + 1
                    
            except ValueError:
                countVMG = countVMG + 1
                    
        if filename.upper().startswith(('REGISTRANTS_DEDUPED')):
            try:
                artezFile = file
                artezEnd = dirpath[-6:]
                if int(artezEnd):
                    if artezEnd > artezDate:
                        artezDir = dirpath
                        artezDate = int(dirpath[-6:])
                        countArtez = countArtez + 1
                        
            except ValueError:
                countArtez = countArtez + 1

if not artezDate == 0:
    print '\nThe most recent Artez Registrants_Deduped-file is for |%s|\nYou can find it in %s' % (artezDate, artezDir) 
else:
    print '\nNo Artez Registrants_Deduped-file found.\nEither they are archived or someone has named the file in an unexpected manner.'
    failCount = failCount + 1

if not jgDate == 0:   
    print '\nThe most recent JG_EventsActions-file is for |%s|\nYou can find it in %s' % (jgDate, jgDir) 
else:
    print '\nNo JG EventsActions-file found.\nEither they are archived or someone has named the file in an unexpected manner.'
    failCount = failCount + 1

if not vmgDate == 0:
    print '\nThe most recent VMG_EventsActions-file is for |%s|\nYou can find it in %s' % (vmgDate, vmgDir)
else:
    print '\nNo VMG EventsActions-file found.\nEither they are archived or someone has named the file in an unexpected manner.'
    failCount = failCount + 1


if failCount < 3:
    print '\nIn total, I have found:\n\n%s Artez,\n%s JG and\n%s VMG Events Actions Files unarchived.' % (countArtez, countJG, countVMG)
    print '\nGood Bye.'
    exiter = raw_input()
else:
    print '\n#622 Epic fail. Unstoppable memory heap cascade alert. Good By'
    exiter = raw_input()



