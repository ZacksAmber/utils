# utils

## [LeetCode](./LeetCode/)

- [leetcode_sql.py](./LeetCode/leetcode_sql.py): `leetcode_sql.py` parses LeetCode SQL test case from JSON to SQL DML(Data Manipulation Language).
  - Runtime: Python3
  - Dependencies: None
  - Usage: Run it directly then paste your test case JSON data into the `leetcode_sql.json` generated by `leetcode_sql.py`, then run it again.

---

## [iCloud](./iCloud/)

- [remove_duplicates.py](iCloud/remove_duplicates.py): `remove_duplicates.py` compares all of the files and subdirectories under the `path` you pass to the program. Then it removes the files or directories with a specific `mark` (defaults to `2`)
  - Notice: **ONLY works in MacOS!**
  - Runtime: Python3
  - Dependencies: None
  - Usage: `python3 remove_duplicates.py "path"`
    - Logic: The new file should larger than the duplicate that retrieved from iCloud.
    - Logic: Or the new file should has a newer modification time than the duplicate that retrieved from iCloud.

---

## [Anime](./Anime/)

- [anime_subtitles.py](./Anime/anime_subtitles.py): `anime_subtitles.py` converts animation subtitles file name to the same as the episodes' name.
  - Runtime: Python3
  - Dependencies: None
  - Usage: Put animations, subtitles, and the program in the same directory. Then run the program.
  - Possible Issues: The program only recognizes the following file extensions. For more extensions, you need to add `|(\.extension_name)` in the counterpart.
    - Videos: `.mkv`, `.mp4`, `.avi`, `.mov`
    - Subtitles: `.ssa`, `.ass`, `.srt`, `.smi`
