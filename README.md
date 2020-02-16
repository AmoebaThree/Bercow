# Bercow

The Speaker

## Prerequisites

- `sudo apt-get install python-systemd`
- `pip install redis`

- Stick a load of audio files in the Audio folder, samples included!
- You might want to force headphone jack for audio using `sudo raspi-config` (advanced menu)

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<bercow> "\<filename>"
  * Play the file /home/pi/code/Bercow/Audio/\<filename>.WAV out of the headphone socket

**Outputs**

None