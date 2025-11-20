# Data Directory

## Structure

```txt
data/
├── raw/                    # Original Zindi data (gitignored)
│   ├── train/
│   │   ├── audio/
│   │   └── Train.csv
│   └── test/
│       ├── audio/
│       └── Test.csv
├── processed/              # Preprocessed audio (gitignored)
│   ├── train/
│   └── test/
└── splits/                 # Split indices (tracked in git)
    ├── train_ids.txt
    ├── val_ids.txt
    └── holdout_ids.txt
```

## Download Instructions

1. Go to [Zindi competition page](https://zindi.africa/competitions/...)
2. Download `Train.zip` and `Test.zip`
3. Extract to `data/raw/train/` and `data/raw/test/`

```bash
cd data/raw
unzip Train.zip -d train/
unzip Test.zip -d test/
```

## Data Splits

**Training:** 80% of original training data  
**Validation:** 15% of original training data  
**Holdout:** 5% of original training data (for final check)

Split strategy: Stratified by [TBD - audio quality, length, etc.]

Split files contain row IDs from Train.csv, one per line.

## Expected Structure After Download

```txt
data/raw/train/
├── audio/
│   ├── ID_IJLHYZ.wav
│   ├── ID_OFIPGR.wav
│   └── ... (28,000 files)
└── Train.csv

data/raw/test/
├── audio/
│   ├── ID_XXXXX.wav
│   └── ...
└── Test.csv
```

## Data Overview

- **Training samples**: ~28,000 audio clips
- **Duration**: ~30 seconds each
- **Format**: WAV files
- **Source**: BBC Caribbean broadcasts
- **Transcriptions**: Manual human transcriptions in Train.csv

---

**Note**: Raw data files are gitignored due to size. Each team member should download independently.
