# Audio and video: formats and significant properties

This page sets out, for sound and video recordings, which formats Anton prefers and accepts, which properties must be preserved, and what Anton measures or checks of them today. It belongs to the series per format category (anton#687), after [images](formate-bild.md), [PDF](formate-pdf.md) and [text](formate-text.md). The choices are provisional: they are being tried in practice and will be revised where they do not prove themselves.

Anton needs this for three things: to document what makes up a recording (NDSA Cn-1.1), to verify that it still does (Cn-2.1), and to prove after a migration that nothing significant was lost ([`media:migrate`](console-commands.md#mediamigrate)).

## Formats {#formate}

### Audio

| Level | Format | Condition |
|---|---|---|
| preferred | WAV or Broadcast Wave (BWF) with LPCM | |
| preferred | FLAC | |
| accepted | MP3, AAC (M4A), AIFF, Ogg Vorbis, Opus | as long as ffmpeg reads them |

### Video

| Level | Format | Condition |
|---|---|---|
| preferred | original codec in a common container, as delivered | born-digital video |
| preferred | MKV with FFV1 and FLAC | digitisation of analogue carriers |
| preferred | MP4 with H.264 | where storage is scarce |
| accepted | MOV (ProRes too), AVI, MPEG-2, MXF, WebM, WMV, MP4 with HEVC or AV1 | as long as ffmpeg reads them |

**Preferred** for sound are the uncompressed or losslessly compressed formats WAV/BWF and FLAC; this is what NARA and KOST recommend. For video the codec comes first: a born-digital video is not re-encoded, since every lossy re-encoding loses information and may produce artefacts (KOST). When analogue carriers are digitised, the master is made losslessly, as MKV with FFV1 for the picture and FLAC for the sound (KOST); for sound, Memoriav and the Swiss National Sound Archives recommend 96 kHz and 24 bits, NARA at least 44.1 kHz and 16 bits, better 96 kHz and 24 bits, and 10 bits for video. MP4 with H.264 is the choice where a lossless master needs too much storage; an appraisal decision, as with JPEG for images.

**Accepted** is, as with images, what widespread open-source tools can read and will in all likelihood go on reading; for sound and video that is ffmpeg, which also decodes ProRes, WMV and MXF. Recordings already compressed with loss (MP3, AAC, H.264) are not converted to a lossless format: the loss remains, the file only grows (KOST). NARA advises converting WMV to AVI; under the principle it stays until ffmpeg no longer reads it.

Changing the container is possible without loss: the streams are moved unchanged into another container, for instance from MOV to MKV (KOST). This is the gentlest form of normalisation.

Here too: an archive keeps [as few formats as possible](formate-bild.md#formate).

## Significant properties

Grouped as NARA does into appearance, structure, behaviour and context. NARA requires that a conversion of born-digital material keep the same sampling attributes, the same channel layout and, where the new format allows, the same compression.

| Group | Property | Applies to | Source |
|---|---|---|---|
| Appearance | width and height in pixels, aspect ratio | video | NARA |
| | frame rate, interlacing | video | NARA |
| | bit depth and chroma subsampling | video | NARA |
| | colour space | video | NARA |
| Structure | duration | audio, video | NARA |
| | number and kind of streams (picture, sound, subtitles) | audio, video | NARA |
| | channels and channel layout (mono, stereo, 5.1) | audio, video | NARA |
| | sample rate and bit depth | audio, video | NARA |
| | content of each stream, where the format is lossless | audio, video | Anton |
| | codec and compression: recorded, not preserved | audio, video | NARA, KOST |
| Behaviour | The recording can be played, picture and sound in sync. | audio, video | NARA |
| Context | embedded metadata (title, creator, recording date, for BWF the coding history) | audio, video | NARA |

Codec and compression are not properties that must be preserved. They are recorded because they tell whether the other properties are held losslessly; and a migration should change them only where necessary.

For lossless formats, the content of a stream can be proved with a checksum per stream, the counterpart of the pixel signature for images: if it stays the same after a change of container or a lossless conversion, no frame and no sample has changed.

## What Anton measures and checks

As of version 0.111.1.

| Property | Measured | Checked |
|---|---|---|
| Duration, codec, bit rate, resolution, sample rate, aspect ratio | with ffprobe at ingest, to be filled in with [`media:extract-av-metadata`](console-commands.md#mediaextract-av-metadata) | no |
| Channels, bit depth, frame rate, interlacing, colour space, streams | no (anton#717) | no |
| Content of each stream | no (anton#717) | no |
| Playable | – | at ingest ffprobe reads the container; nightly with [`media:validate-formats`](console-commands.md#mediavalidate-formats) ffmpeg decodes every frame and every sample, and every error message counts; also when the access copy is made |
| Embedded metadata | no | no |

Measured values appear on the medium with the sound and video details.

## Limits

- On umberto, on 2026-10-23, only 2 of 771 sound and video recordings had the measured values; the backfill has never run (anton#717).
- Anton does not measure channels, bit depth, frame rate, interlacing, colour space or the number of streams (anton#717).
- `media:migrate` proves nothing for sound and video; the pixel signature exists only for images (anton#717).
- An access copy is made for video only from MP4, MOV and MPEG, for sound only from WAV and MP3. For FLAC, M4A, AIFF, Ogg, MKV, AVI, WebM, MXF and WMV it is missing, and upload does not take FLAC, AIFF, Ogg, MKV, AVI, WebM, MXF and WMV (anton#718).
- «Playable» means ffmpeg decodes the recording without an error message. It does not check whether picture and sound are good.

## What a migration must check

When `media:migrate` converts a recording, afterwards:

- Duration, number and kind of streams, channels, sample rate, resolution and frame rate are the same.
- With a lossless target (change of container, FFV1, FLAC), the checksum of every stream is the same.
- The embedded metadata is carried over.
- The delivered file stays as an [original](preservation.md#behaltene-originale) when the target is lossy.

## Sources {#quellen}

- National Archives and Records Administration (NARA), Digital Preservation Framework: [Preservation Action Plan for Digital Audio](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalAudio.md) and [Preservation Action Plan for Digital Video](https://github.com/usnationalarchives/digital-preservation/blob/master/Digital_Preservation_Record_Categories/NARA_PreservationActionPlan_DigitalVideo.md), plan date 2024-11 (PDF versions of 2024-12-18). Significant properties, requirements for digitisation and conversion, transfer formats. As preferred video format the plan names «AV1 Image File Format (AVIF)», an image format; this is evidently a mistake and not adopted here.
- NARA: [Preservation Action Plan, format table](https://github.com/usnationalarchives/digital-preservation/tree/master/Digital_Preservation_Plan_Spreadsheet), as of 2026-03-20. Risk and action per format; it does not list Matroska or FFV1.
- NARA: [Bulletin 2014-04, Format Guidance for the Transfer of Permanent Electronic Records](https://www.archives.gov/records-mgmt/bulletins/2014/2014-04.html). Transfer formats the plans refer to.
- Federal Agencies Digital Guidelines Initiative (FADGI): [Significant Properties for Digital Video](https://www.digitizationguidelines.gov/guidelines/FADGI-SignificantPropertiesDigitalVideo2024.pdf), 2024. Named by NARA's video plan as its basis.
- KOST, Katalog archivischer Dateiformate (KaD), version 7.1, May 2026: [Audio, summary](https://kost-ceco.ch/cms/kad_audio_intro_de.html) and [Video, summary](https://kost-ceco.ch/cms/kad_video_intro_de.html). Recommended and accepted formats, no conversion of lossy recordings, codec before container, lossless change of container, MKV with FFV1 and FLAC as archival master.
- [FFmpeg](https://ffmpeg.org/): open-source tools to read, check and convert sound and video.
- NDSA: [Levels of Digital Preservation, version 2.1](https://ndsa.org/publications/levels-of-digital-preservation/), March 2026, requirements Cn-1.1 and Cn-2.1.
