# Bercow

The Speaker

## Build

    docker buildx bake

## Prerequisites

- Stick a load of audio files in the Audio folder, samples included!
- You might want to force headphone jack for audio using `sudo raspi-config` (advanced menu)

## Message Spec

Format: \<channel> "message"

**Inputs**

* \<bercow> "\<filename>"
  * Play the file ./Audio/\<filename>.WAV out of the headphone socket

**Outputs**

None