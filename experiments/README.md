# Experiment Tracking

## How to Log Experiments

Add a new row to `experiments.csv` after each experiment:

```python
import pandas as pd
from datetime import datetime

def log_experiment(exp_data):
    df = pd.read_csv('experiments/experiments.csv')
    
    new_row = {
        'exp_id': f"{len(df) + 1:03d}",
        'date': datetime.now().strftime('%Y-%m-%d'),
        'person': exp_data['person'],
        'model': exp_data['model'],
        'preprocessing': exp_data.get('preprocessing', 'none'),
        'learning_rate': exp_data.get('lr', ''),
        'batch_size': exp_data.get('batch_size', ''),
        'epochs': exp_data.get('epochs', ''),
        'val_wer': exp_data.get('val_wer', ''),
        'public_lb': exp_data.get('public_lb', ''),
        'private_lb': '',  # Fill after competition
        'notes': exp_data.get('notes', ''),
        'commit_hash': exp_data.get('commit', ''),
        'config_file': exp_data.get('config', '')
    }
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv('experiments/experiments.csv', index=False)
    print(f"Logged experiment {new_row['exp_id']}")

# Usage
log_experiment({
    'person': 'chad',
    'model': 'whisper-large-v3-ft',
    'preprocessing': 'normalize',
    'lr': 1e-5,
    'batch_size': 16,
    'epochs': 3,
    'val_wer': 0.215,
    'notes': 'First fine-tune attempt',
    'commit': 'abc1234'
})
```

## Experiment Naming Convention

- `exp_id`: Sequential (001, 002, 003...)
- Format: Zero-padded 3 digits

## What to Track

**Required:**

- exp_id, date, person, model, val_wer

**Recommended:**

- preprocessing, hyperparameters, notes, commit_hash

**Optional:**

- public_lb (after submission)
- config_file (if using YAML configs)

## Quick Analysis

```python
# Load and analyze experiments
df = pd.read_csv('experiments/experiments.csv')

# Best validation WER
best_val = df.nsmallest(5, 'val_wer')[['exp_id', 'model', 'val_wer', 'notes']]
print("Top 5 by validation WER:")
print(best_val)

# Best public leaderboard
best_lb = df.dropna(subset=['public_lb']).nsmallest(5, 'public_lb')[['exp_id', 'model', 'public_lb', 'notes']]
print("\nTop 5 by public leaderboard:")
print(best_lb)

# By person
by_person = df.groupby('person')['val_wer'].agg(['count', 'min', 'mean'])
print("\nExperiments by person:")
print(by_person)
```

## Submission Strategy

Before submitting to Zindi:

1. Check experiment log for this exp_id
2. Note which model/config
3. After submission, update `public_lb` column
4. Track which 2 submissions selected for private LB

---

**Remember**: Commit and push experiments.csv after each new experiment!
