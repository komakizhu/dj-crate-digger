# [老炮DJ](https://github.com/komakizhu/dj-crate-digger) Skill and `.w4dj` Handoff Guide: One-Click Set Download and RKB Import

[中文](README.md) | [English](README.en.md)

`.w4dj` is a playlist handoff file shared by [老炮DJ](https://github.com/komakizhu/dj-crate-digger) and [W4DJ RKB](https://github.com/komakizhu/W4DJ-RKB). It stores the playlist name, track order, complete official titles, and artist information, but it does not contain audio files.

The file always carries the fixed compatibility value `format_version: 2`. This machine field lets W4DJ RKB identify the contract; users do not select a version or fill the field manually.

The complete workflow is:

[老炮DJ](https://github.com/komakizhu/dj-crate-digger) generates a playlist → export `.w4dj` → import it into W4DJ RKB → create a playlist in NetEase Cloud Music and download the tracks → W4DJ RKB converts the audio and exports a playlist → import it into Rekordbox.

> `.w4dj` is not an audio file and cannot be imported directly into Rekordbox. W4DJ RKB does not obtain copyrighted audio for users; tracks must first be downloaded to the local computer through legal channels.

## Step 1: Get a `.w4dj` File from [老炮DJ](https://github.com/komakizhu/dj-crate-digger)

After completing track selection, reply with:

```text
导出到w4dj
```

[老炮DJ](https://github.com/komakizhu/dj-crate-digger) generates a file ending in `.w4dj`. Save it locally.

## Step 2: Download W4DJ RKB

Go to [W4DJ-RKB](https://github.com/komakizhu/W4DJ-RKB) and download and install the version suitable for your operating system.

After opening W4DJ RKB, click “导入 .w4dj” (Import `.w4dj`) in the upper-right corner.

![Click “导入 .w4dj”](./images/01-import-w4dj.png)

In the “DJ 歌单” (DJ Playlist) window that appears, click “导入 .w4dj” (Import `.w4dj`) again, then select the file you just saved.

![Select the `.w4dj` file](./images/02-import-button.png)

After the import succeeds, W4DJ RKB reads the playlist name, track order, and track information. The `.w4dj` file contains no NetEase song IDs; it provides complete titles, all known artists, version qualifiers, and playlist order for the later text-matching workflow.

## Step 3: Import the Playlist into NetEase Cloud Music

The currently verified workflow uses the mobile version of NetEase Cloud Music. Button locations and names may vary slightly between versions.

### 1. Get the Text Playlist

After importing `.w4dj`, follow the instructions in W4DJ RKB:

1. Open the QR code;
2. Scan the QR code with your phone;
3. Copy the text playlist generated on the page.

The text playlist generally contains track titles and artist names for automatic matching in NetEase Cloud Music.

> W4DJ RKB hands off titles, all known artists, and version information as text. The DJ Skill does not search for or guess NetEase song IDs; the user-selected NetEase records and actual output files are registered by the downstream workflow.

### 2. Open “我的” (My Music) in NetEase Cloud Music

Open the mobile version of NetEase Cloud Music and tap “我的” (My Music) in the bottom navigation bar.

![Open “我的” (My Music) in NetEase Cloud Music](./images/08-netease-my.png)

### 3. Open the Top-Right Menu

On the “我的” (My Music) page, tap the three dots `⋮` in the upper-right corner.

> Note: These are the three dots in the upper-right corner, not the menu button in the upper-left corner.

### 4. Select “一键导入外部音乐” (One-Click Import External Music)

In the menu that appears, tap “一键导入外部音乐” (One-Click Import External Music).

![Select “一键导入外部音乐”](./images/09-netease-external-import.png)

### 5. Switch to “文字导入” (Text Import)

On the “歌单导入” (Playlist Import) page, select “文字导入” (Text Import) at the top.

![Open “文字导入” (Text Import)](./images/10-netease-text-import.png)

### 6. Paste the Text and Start the Import

Paste the text playlist copied from W4DJ RKB into the input field, then tap “开始导入” (Start Import).

Before pasting, check that:

- Each track includes its title and artist;
- Each track occupies a separate line;
- Remix, Dub, Edit, Live, Radio Edit, Extended Mix, and other version qualifiers have not been removed;
- No unrelated explanatory text has been added.

### 7. Check the Matches and Download

NetEase Cloud Music automatically matches tracks based on their titles and artists. After matching is complete, check each track:

- Is the title and artist correct?
- Did it match the correct Remix, Dub, Edit, or Extended Mix?
- Is there a same-title track from a different version?
- Did any track fail to match because of copyright or regional availability?

After confirming the matches, create the playlist and download the tracks needed for DJ software to the local computer.

> NetEase Cloud Music's automatic matching does not guarantee an exact version match. Always verify manually before downloading.

## Step 4: Convert the Tracks in W4DJ RKB

After the tracks finish downloading, return to W4DJ RKB:

1. Select the NetEase Cloud Music track folder or the individual tracks to process;
2. Select the output directory for the converted tracks;
3. Choose the conversion method and output mode as needed;
4. Start scanning and conversion;
5. Wait for the task to finish and confirm that every track in the playlist was found.

If some tracks were not found, first check whether NetEase Cloud Music has finished downloading them and whether the downloaded versions match the complete official titles in the playlist. At this stage W4DJ RKB uses complete titles, all known artists, version information, and operation context to bind playlist positions to actual output files; the DJ Skill does not participate in that process or hide a wrong match by guessing a song ID.

## Step 5: Export the Playlist

After conversion is complete, click “导出播放列表” (Export Playlist) at the top of W4DJ RKB.

![Click “导出播放列表” (Export Playlist)](./images/03-export-playlist.png)

Select the playlist to export in the dialog.

![Select the recent playlist](./images/04-select-playlist.png)

Then select an export method.

![Select an export method](./images/05-export-mode.png)

### Copy Audio and Export

The tracks are copied to a new export folder and a playlist is generated at the same time. This is suitable when moving the set to another computer or keeping the audio and playlist in one directory, but it uses more disk space.

### Export Playlist Only

Only a playlist is generated; the audio files are not copied. This does not create duplicate audio files, but do not move, rename, or delete the original audio after exporting, or Rekordbox may not be able to find the tracks.

## Step 6: Import into Rekordbox

Open Rekordbox and select:

```text
File → Import → Import Playlist
```

![Import the playlist into Rekordbox](./images/06-rekordbox-import.png)

Select the `.m3u8` playlist exported by W4DJ RKB. After a successful import, the corresponding playlist appears in the playlist area on the left side of Rekordbox, with the same track order as the `.w4dj` file.

![Rekordbox import result](./images/07-rekordbox-result.png)

## FAQ

### Can `.w4dj` Be Imported Directly into Rekordbox?

No. First use W4DJ RKB to read `.w4dj`, prepare local audio, and export `.m3u8`; then import `.m3u8` into Rekordbox.

### Why Are There No Tracks After Importing into Rekordbox?

Common causes include:

- The local audio has not finished downloading or converting;
- The audio paths in the playlist are no longer valid;
- Tracks were moved or renamed after export;
- “仅导出歌单” (Export Playlist Only) was selected, but the original audio is no longer in its original location;
- Rekordbox does not have permission to read the directory containing the tracks.

If you cannot identify the cause, try selecting “复制音频并导出” (Copy Audio and Export) again.

### What Should I Do If an Imported Track Is the Wrong Version?

First check whether the track matched by NetEase Cloud Music is the correct version, such as Original, Remix, Dub, Edit, or Extended Mix. `.w4dj` preserves the complete official title, but the platform's automatic match still requires manual confirmation.

### Does W4DJ RKB Download Tracks Automatically?

No. It does not obtain audio for users. Users must first download or prepare local track files through legal channels. W4DJ RKB identifies, converts, organizes, and exports the playlist.
