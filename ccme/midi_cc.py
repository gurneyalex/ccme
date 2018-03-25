definitions = {
    '0': 'Bank Select (MSB)', #(followed by cc32 & Program Change)
    '1': 'Modulation Wheel',
    '2': 'Breath controller',
    '4': 'Foot Pedal (MSB)',
    '5': 'Portamento Time (MSB)', #Only use this for portamento time use cc65 to turn on/off
    '6': 'Data Entry (MSB)', #if you follow cc100=0 & cc101=0 this is pitch bend range
    '7': 'Volume (MSB)', #Note: CC7 and 11 both adjust the volume. Use cc7 as you would the control on the amplifier - set it and leave it at the beginning of the MIDI track
    '8': 'Balance (MSB) Some synths use it',
    '10': 'Pan position (MSB)',
    '11': 'Expression (MSB)', # Note: CC7 and 11 both adjust the volume. Use cc11 for volume changes during the track (crescendo, diminuendo, swells, etc.)
    '12': 'Effect Control 1 (MSB)',
    '13': 'Effect Control 2 (MSB)',
    '14': 'Undefined',
    '15': 'Undefined',
    '16': 'Ribbon Controller or General Purpose Slider 1',
    '17': 'Knob 1 or General Purpose Slider 2',
    '18': 'General Purpose Slider 3',
    '19': 'Knob 2 General Purpose Slider 4',
    '20': 'Knob 3 or Undefined',
    '21': 'Knob 4 or Undefined',
    '22': 'Undefined',
    '23': 'Undefined',
    '24': 'Undefined',
    '25': 'Undefined',
    '26': 'Undefined',
    '27': 'Undefined',
    '28': 'Undefined',
    '29': 'Undefined',
    '30': 'Undefined',
    '31': 'Undefined',
    '32': 'Bank Select (LSB) (see cc0)',
    '33': 'Modulation Wheel (LSB)',
    '34': 'Breath controller (LSB)',
    '36': 'Foot Pedal (LSB)',
    '37': 'Portamento Time (LSB)',
    '38': 'Data Entry (LSB)',
    '39': 'Volume (LSB)',
    '40': 'Balance (LSB)',
    '42': 'Pan position (LSB)',
    '43': 'Expression (LSB)',
    '44': 'Effect Control 1 (LSB) Roland Portamento on and rate',
    '45': 'Effect Control 2 (LSB)',
    '46': 'Undefined (LSB of 14)', #63 may be in use as the LSB for controllers 14-31 in some devices, but I have not seen one yet.
    '47': 'Undefined (LSB of 15)',
    '48': 'Ribbon Controller or General Purpose Slider 1 (LSB of 16)',
    '49': 'Knob 1 or General Purpose Slider 2 (LSB of 17)',
    '50': 'General Purpose Slider 3 (LSB of 18)',
    '51': 'Knob 2 General Purpose Slider 4 (LSB of 19)',
    '52': 'Knob 3 or Undefined (LSB of 20)',
    '53': 'Knob 4 or Undefined (LSB of 21)',
    '54': 'Undefined (LSB of 22)',
    '55': 'Undefined (LSB of 23)',
    '56': 'Undefined (LSB of 24)',
    '57': 'Undefined (LSB of 25)',
    '58': 'Undefined (LSB of 26)',
    '59': 'Undefined (LSB of 27)',
    '60': 'Undefined (LSB of 28)',
    '61': 'Undefined (LSB of 29)',
    '62': 'Undefined (LSB of 30)',
    '63': 'Undefined (LSB of31)',
    '64': 'Hold Pedal (on/off)', #Nearly every synth will react to 64 (sustain pedal)
    '65': 'Portamento (on/off)',
    '66': 'Sustenuto Pedal (on/off)',
    '67': 'Soft Pedal (on/off)',
    '68': 'Legato Pedal (on/off)',
    '69': 'Hold 2 Pedal (on/off)',
    '70': 'Sound Variation',
    '71': 'Resonance (aka Timbre)',
    '72': 'Sound Release Time',
    '73': 'Sound Attack Time',
    '74': 'Frequency Cutoff (aka Brightness )',
    '75': 'Sound Control 6',
    '76': 'Sound Control 7',
    '77': 'Sound Control 8',
    '78': 'Sound Control 9',
    '79': 'Sound Control 10',
    '80': 'Decay or General Purpose Button 1 (on/off)', # Roland Tone level 1
    '81': 'Hi Pass Filter Frequency or General Purpose Button 2 (on/off)', #Roland Tone level 2
    '82': 'General Purpose Button 3 (on/off)', #Roland Tone level 3
    '83': 'General Purpose Button 4 (on/off)', #Roland Tone level 4
    '91': 'Reverb Level',
    '92': 'Tremolo Level',
    '93': 'Chorus Level',
    '94': 'Celeste Level or Detune',
    '95': 'Phaser Level',
    }
