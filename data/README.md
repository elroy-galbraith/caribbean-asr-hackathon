# Data Directory

## Structure

```txt
data/
├── raw/                    # Original Zindi data (gitignored)
│   ├── Audio/              # All audio files (train + test)
│   ├── Train.csv
│   ├── Test.csv
│   └── SampleSubmission.csv
├── processed/              # Preprocessed audio (gitignored)
│   ├── train/
│   └── test/
└── splits/                 # Split indices (tracked in git)
    ├── train_ids.txt
    ├── val_ids.txt
    └── holdout_ids.txt
```

## Download Instructions

1. Go to [Zindi competition page](https://zindi.africa/competitions/caribbean-voices-hackathon)
2. Download `Audio.zip`, `Train.csv`, `Test.csv`, and `SampleSubmission.csv`
3. Place CSVs in `data/raw/`
4. Extract `Audio.zip` to `data/raw/`

```bash
cd data/raw
unzip Audio.zip
# This should create an 'Audio' folder containing all .wav files
```

## Data Splits

**Training:** 80% of original training data  
**Validation:** 15% of original training data  
**Holdout:** 5% of original training data (for final check)

Split strategy: Stratified by [TBD - audio quality, length, etc.]

Split files contain row IDs from Train.csv, one per line.

## Expected Structure After Download

```txt
data/raw/
├── Audio/
│   ├── ID_IJLHYZ.wav
│   ├── ID_OFIPGR.wav
│   └── ... (Mixed train and test files)
├── Train.csv
├── Test.csv
└── SampleSubmission.csv
```

## Data Overview

- **Total Audio**: ~4.5 GB
- **Format**: WAV files
- **Source**: BBC Caribbean broadcasts
- **Transcriptions**: Manual human transcriptions in Train.csv

---

**Note**: Raw data files are gitignored due to size. Each team member should download independently.
