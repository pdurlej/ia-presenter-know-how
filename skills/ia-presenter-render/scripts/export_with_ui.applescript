on run argv
	if (count of argv) is not 3 then error "Expected: <deckPath> <exportKind> <outputDir>"
	set deckPath to item 1 of argv
	set exportKind to item 2 of argv
	set outputDir to item 3 of argv
	set exportLabel to my export_label(exportKind)
	
	tell application id "net.ia.presenter"
		activate
		open POSIX file deckPath
	end tell
	
	delay 1
	
	tell application "System Events"
		my wait_for_process("iA Presenter", 40)
		tell process "iA Presenter"
			set frontmost to true
			my wait_for_window(it, 40)
			if not my click_named_element(it, {"Share Presentation"}) then error "Could not find Share Presentation."
			delay 0.8
			if not my click_named_element(it, {exportLabel}) then error "Could not find export option: " & exportLabel
			delay 1.0
			my choose_output_folder(it, outputDir)
			my maybe_replace_existing(it)
		end tell
	end tell
	
	return "ok"
end run

on export_label(exportKind)
	set lowered to my lowercase_text(exportKind)
	if lowered is "images" then return "Images"
	if lowered is "html" then return "HTML"
	if lowered is "markdown" then return "Markdown"
	error "Unsupported export kind: " & exportKind
end export_label

on wait_for_process(procName, secondsLimit)
	tell application "System Events"
		repeat (secondsLimit * 4) times
			if exists process procName then return true
			delay 0.25
		end repeat
	end tell
	error "Timed out waiting for process: " & procName
end wait_for_process

on wait_for_window(procRef, secondsLimit)
	repeat (secondsLimit * 4) times
		try
			if (count of windows of procRef) > 0 then return true
		end try
		delay 0.25
	end repeat
	error "Timed out waiting for the iA Presenter window."
end wait_for_window

on choose_output_folder(procRef, outputDir)
	tell application "System Events"
		keystroke "g" using {shift down, command down}
		delay 0.7
		keystroke outputDir
		delay 0.2
		key code 36
		delay 0.9
	end tell
	
	if my click_named_element(procRef, {"Choose", "Open", "Select"}) then return true
	
	tell application "System Events"
		key code 36
	end tell
	return true
end choose_output_folder

on maybe_replace_existing(procRef)
	repeat 20 times
		if my click_named_element(procRef, {"Replace", "Replace All"}) then return true
		delay 0.25
	end repeat
	return false
end maybe_replace_existing

on click_named_element(procRef, needles)
	repeat 20 times
		repeat with aWindow in (windows of procRef)
			try
				tell application "System Events"
					set itemsList to entire contents of aWindow
				end tell
				repeat with needle in needles
					set foundElement to my first_matching_ui_element(itemsList, needle as text)
					if foundElement is not missing value then
						my press_element(foundElement)
						return true
					end if
				end repeat
			end try
		end repeat
		delay 0.25
	end repeat
	return false
end click_named_element

on first_matching_ui_element(itemsList, needle)
	set loweredNeedle to my lowercase_text(needle)
	repeat with itemRef in itemsList
		repeat with candidateText in my candidate_texts(itemRef)
			if candidateText is not "" and (my lowercase_text(candidateText)) contains loweredNeedle then return itemRef
		end repeat
	end repeat
	return missing value
end first_matching_ui_element

on candidate_texts(itemRef)
	set valuesList to {}
	tell application "System Events"
		try
			set end of valuesList to (name of itemRef as text)
		end try
		try
			set end of valuesList to (description of itemRef as text)
		end try
		try
			set end of valuesList to (value of itemRef as text)
		end try
	end tell
	return valuesList
end candidate_texts

on press_element(itemRef)
	tell application "System Events"
		try
			click itemRef
			return true
		end try
		try
			perform action "AXPress" of itemRef
			return true
		end try
	end tell
	error "Could not press UI element."
end press_element

on lowercase_text(valueText)
	return do shell script "/bin/echo " & quoted form of valueText & " | /usr/bin/tr '[:upper:]' '[:lower:]'"
end lowercase_text
